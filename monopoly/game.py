import random

from monopoly import board as B
from monopoly import cards as C
from monopoly.actions import (
    AUCTION_LEVELS,
    AUCTION,
    BUILD,
    BUY,
    JAIL,
    TRADE_OFFER,
    TRADE_REPLY,
    TRADE_MULTIPLIERS,
    Decision,
)
from monopoly.player import Player

from agents import features as F

START_CASH = 1500


class Game:
    def __init__(self, agents, seed=None, max_rounds=200, record_events=False,
                 names=None, start_cash=START_CASH):
        self.rng = random.Random(seed)
        self.seed = seed
        self.agents = list(agents)
        names = names or [a.name for a in agents]
        self.players = [Player(i, names[i], start_cash) for i in range(len(agents))]
        self.owner = [None] * 40
        self.houses = [0] * 40
        self.mortgaged = [False] * 40
        self.houses_left = B.MAX_HOUSES
        self.hotels_left = B.MAX_HOTELS
        self.chance = C.Deck(C.CHANCE_CARDS, self.rng)
        self.chest = C.Deck(C.CHEST_CARDS, self.rng)
        self.turn = 0
        self.record_events = record_events
        self.events = []
        self.stats = {p.pid: {"bought": 0, "auctions_won": 0, "rent_paid": 0,
                              "rent_received": 0, "houses_built": 0,
                              "trades_done": 0, "jail_visits": 0} for p in self.players}
        self.finished = False
        self.result = None

    # ---------- helpers ----------

    def alive_players(self):
        return [p for p in self.players if p.alive]

    def group_owner(self, group):
        owners = {self.owner[i] for i in B.GROUPS[group]}
        if len(owners) == 1:
            return owners.pop()
        return None

    def count_owned(self, pid, idxs):
        return sum(1 for i in idxs if self.owner[i] == pid)

    def net_worth(self, p):
        total = p.cash
        for i in p.props:
            sp = B.space(i)
            total += sp.mortgage if self.mortgaged[i] else sp.price
            lvl = self.houses[i]
            if lvl:
                total += lvl * sp.house_cost
        return total

    def advantage(self, p):
        alive = self.alive_players()
        total = sum(self.net_worth(x) for x in alive)
        if total <= 0 or not alive:
            return 0.0
        return self.net_worth(p) / total - 1.0 / len(alive)

    def log(self, kind, **kw):
        if self.record_events:
            kw["t"] = self.turn
            kw["e"] = kind
            self.events.append(kw)

    def decide(self, p, dtype, state, legal, meta=None):
        d = Decision(dtype, state, legal, self.advantage(p), meta)
        return self.agents[p.pid].act(d)

    # ---------- money ----------

    def sell_one_house(self, p):
        best = None
        for i in p.props:
            lvl = self.houses[i]
            if lvl <= 0:
                continue
            sp = B.space(i)
            peak = max(self.houses[j] for j in B.GROUPS[sp.group])
            if lvl < peak:
                continue
            key = (sp.house_cost, sp.price)
            if best is None or key < best[0]:
                best = (key, i)
        if best is None:
            return False
        i = best[1]
        sp = B.space(i)
        if self.houses[i] == 5:
            self.hotels_left += 1
            if self.houses_left >= 4:
                self.houses_left -= 4
                self.houses[i] = 4
                p.cash += sp.house_cost // 2
            else:
                self.houses[i] = 0
                p.cash += 5 * sp.house_cost // 2
        else:
            self.houses[i] -= 1
            self.houses_left += 1
            p.cash += sp.house_cost // 2
        self.log("sell_house", p=p.pid, prop=i, level=self.houses[i])
        return True

    def mortgage_one(self, p):
        best = None
        for i in p.props:
            if self.mortgaged[i] or self.houses[i]:
                continue
            sp = B.space(i)
            if best is None or sp.mortgage < B.space(best).mortgage:
                best = i
        if best is None:
            return False
        self.mortgaged[best] = True
        p.cash += B.space(best).mortgage
        self.log("mortgage", p=p.pid, prop=best)
        return True

    def raise_cash(self, p, needed):
        guard = 0
        while p.cash < needed and guard < 80:
            guard += 1
            if self.mortgage_one(p):
                continue
            if self.sell_one_house(p):
                continue
            break
        return p.cash >= needed

    def unmortgage_pass(self, p):
        for i in sorted(p.props, key=lambda x: -B.space(x).price):
            if not self.mortgaged[i]:
                continue
            cost = int(B.space(i).mortgage * 1.1)
            if p.cash - cost >= 300:
                p.cash -= cost
                self.mortgaged[i] = False
                self.log("unmortgage", p=p.pid, prop=i)

    def charge(self, p, amount, creditor=None):
        if amount <= 0:
            return True
        if p.cash < amount:
            self.raise_cash(p, amount)
        if p.cash >= amount:
            p.cash -= amount
            if creditor is not None:
                creditor.cash += amount
            return True
        self.bankrupt(p, creditor)
        return False

    def bankrupt(self, p, creditor):
        p.alive = False
        p.bankrupt_turn = self.turn
        while self.sell_one_house(p):
            pass
        props = list(p.props)
        self.log("bankrupt", p=p.pid, to=(creditor.pid if creditor else None),
                 props=len(props))
        if creditor is not None and creditor.alive:
            creditor.cash += max(0, p.cash)
            for i in props:
                self.owner[i] = creditor.pid
                creditor.props.add(i)
            creditor.jail_cards += p.jail_cards
        else:
            for i in props:
                self.owner[i] = None
                self.mortgaged[i] = False
        p.cash = 0
        p.props = set()
        p.jail_cards = 0
        if creditor is None or not creditor.alive:
            for i in props:
                if len(self.alive_players()) > 1:
                    self.auction(i)

    # ---------- movement ----------

    def dice(self):
        return self.rng.randint(1, 6), self.rng.randint(1, 6)

    def move_to(self, p, target, collect_go=True):
        if collect_go and target < p.position:
            p.cash += B.GO_SALARY
            self.log("pass_go", p=p.pid)
        p.position = target

    def go_to_jail(self, p):
        p.position = B.JAIL_IDX
        p.in_jail = True
        p.jail_turns = 0
        self.stats[p.pid]["jail_visits"] += 1
        self.log("go_to_jail", p=p.pid)

    # ---------- landing ----------

    def resolve(self, p, dice_total, rent_mult=1, util_force=0, depth=0):
        if not p.alive or depth > 3:
            return
        sp = B.space(p.position)
        self.log("land", p=p.pid, space=sp.idx, name=sp.name)
        if sp.kind in B.BUYABLE:
            owner = self.owner[sp.idx]
            if owner is None:
                self.offer_purchase(p, sp)
            elif owner != p.pid and not self.mortgaged[sp.idx]:
                rent = self.rent_for(sp, dice_total, util_force) * rent_mult
                creditor = self.players[owner]
                self.stats[p.pid]["rent_paid"] += rent
                self.stats[owner]["rent_received"] += rent
                self.log("rent", p=p.pid, to=owner, amount=rent, prop=sp.idx)
                self.charge(p, rent, creditor)
        elif sp.kind == B.TAX:
            self.charge(p, sp.amount)
        elif sp.kind == B.GOTOJAIL:
            self.go_to_jail(p)
        elif sp.kind == B.CHANCE:
            self.draw_card(p, self.chance, depth)
        elif sp.kind == B.CHEST:
            self.draw_card(p, self.chest, depth)

    def rent_for(self, sp, dice_total, util_force=0):
        owner = self.owner[sp.idx]
        if sp.kind == B.RAIL:
            n = self.count_owned(owner, B.RAIL_IDX)
            return B.RAIL_RENT[max(0, n - 1)]
        if sp.kind == B.UTIL:
            n = self.count_owned(owner, B.UTIL_IDX)
            mult = util_force or (10 if n == 2 else 4)
            return mult * dice_total
        lvl = self.houses[sp.idx]
        if lvl == 0:
            base = sp.rents[0]
            if self.group_owner(sp.group) == owner:
                return base * 2
            return base
        return sp.rents[lvl]

    def draw_card(self, p, deck, depth):
        card = deck.draw()
        self.log("card", p=p.pid, text=card.text)
        k = card.kind
        if k == C.JAIL_CARD:
            p.jail_cards += 1
            return
        deck.put_back(card)
        if k == C.MOVE:
            self.move_to(p, card.value)
            self.resolve(p, sum(self.dice()), depth=depth + 1)
        elif k == C.MOVE_BACK:
            p.position = (p.position - card.value) % 40
            self.resolve(p, sum(self.dice()), depth=depth + 1)
        elif k == C.MOVE_NEAREST:
            targets = B.UTIL_IDX if card.value == 1 else B.RAIL_IDX
            target = min(targets, key=lambda i: (i - p.position) % 40 or 40)
            self.move_to(p, target)
            if card.value == 1:
                self.resolve(p, sum(self.dice()), util_force=10, depth=depth + 1)
            else:
                self.resolve(p, sum(self.dice()), rent_mult=2, depth=depth + 1)
        elif k == C.GAIN:
            p.cash += card.value
        elif k == C.PAY:
            self.charge(p, card.value)
        elif k == C.GO_JAIL:
            self.go_to_jail(p)
        elif k == C.GAIN_EACH:
            for q in self.alive_players():
                if q is not p:
                    self.charge(q, card.value, p)
        elif k == C.PAY_EACH:
            for q in self.alive_players():
                if q is not p and p.alive:
                    self.charge(p, card.value, q)
        elif k == C.REPAIRS:
            houses = sum(self.houses[i] for i in p.props if self.houses[i] < 5)
            hotels = sum(1 for i in p.props if self.houses[i] == 5)
            self.charge(p, houses * card.value + hotels * card.extra)

    # ---------- purchase and auction ----------

    def give_property(self, p, idx):
        self.owner[idx] = p.pid
        p.props.add(idx)

    def offer_purchase(self, p, sp):
        legal = [True, p.cash >= sp.price]
        if not legal[1]:
            self.auction(sp.idx)
            return
        state = F.buy_state(self, p, sp)
        a = self.decide(p, BUY, state, legal, {"prop": sp.idx, "price": sp.price})
        if a == 1:
            p.cash -= sp.price
            self.give_property(p, sp.idx)
            self.stats[p.pid]["bought"] += 1
            self.log("buy", p=p.pid, prop=sp.idx, price=sp.price)
        else:
            self.auction(sp.idx)

    def auction(self, idx):
        sp = B.space(idx)
        bidders = self.alive_players()
        if not bidders:
            return
        bids = []
        for q in bidders:
            levels = [int(m * sp.price) for m in AUCTION_LEVELS]
            legal = [True] + [q.cash >= levels[i] for i in (1, 2, 3)]
            state = F.auction_state(self, q, sp)
            a = self.decide(q, AUCTION, state, legal, {"prop": idx, "price": sp.price})
            if a > 0:
                bids.append((levels[a], self.rng.random(), q))
        if not bids:
            self.log("auction_none", prop=idx)
            return
        bids.sort(reverse=True)
        top = bids[0][2]
        second = bids[1][0] if len(bids) > 1 else 0
        price = min(bids[0][0], max(10, second + 10))
        top.cash -= price
        self.give_property(top, idx)
        self.stats[top.pid]["auctions_won"] += 1
        self.log("auction_won", p=top.pid, prop=idx, price=price)

    # ---------- building ----------

    def buildable_groups(self, p):
        out = []
        for g in B.STREET_GROUPS:
            if self.group_owner(g) != p.pid:
                continue
            idxs = B.GROUPS[g]
            if any(self.mortgaged[i] for i in idxs):
                continue
            lo = min(self.houses[i] for i in idxs)
            if lo >= 5:
                continue
            cost = B.space(idxs[0]).house_cost
            if p.cash < cost + 100:
                continue
            if lo == 4:
                if self.hotels_left <= 0:
                    continue
            elif self.houses_left <= 0:
                continue
            out.append((g, lo))
        return out

    def build_phase(self, p):
        for _ in range(4):
            options = self.buildable_groups(p)
            if not options:
                return
            built = False
            for g, lvl in options:
                state = F.build_state(self, p, g, lvl)
                a = self.decide(p, BUILD, state, [True, True], {"group": g})
                if a == 1:
                    self.develop(p, g)
                    built = True
                    break
            if not built:
                return

    def develop(self, p, g):
        idxs = B.GROUPS[g]
        cost = B.space(idxs[0]).house_cost
        for _ in range(5):
            if p.cash < cost + 200:
                return
            lo = min(self.houses[i] for i in idxs)
            if lo >= 5:
                return
            if lo == 4:
                if self.hotels_left <= 0:
                    return
            elif self.houses_left <= 0:
                return
            target = min(idxs, key=lambda i: (self.houses[i], i))
            p.cash -= cost
            if self.houses[target] == 4:
                self.houses[target] = 5
                self.hotels_left -= 1
                self.houses_left += 4
            else:
                self.houses[target] += 1
                self.houses_left -= 1
            self.stats[p.pid]["houses_built"] += 1
            self.log("build", p=p.pid, prop=target, level=self.houses[target])

    # ---------- trading ----------

    def trade_phase(self, p):
        target = None
        for g in B.STREET_GROUPS:
            idxs = B.GROUPS[g]
            mine = [i for i in idxs if self.owner[i] == p.pid]
            missing = [i for i in idxs if self.owner[i] not in (p.pid, None)]
            if len(mine) == len(idxs) - 1 and len(missing) == 1:
                i = missing[0]
                if self.houses[i] == 0:
                    target = i
                    break
        if target is None:
            return
        sp = B.space(target)
        seller = self.players[self.owner[target]]
        legal = [True] + [p.cash >= int(m * sp.price) for m in TRADE_MULTIPLIERS[1:]]
        if not any(legal[1:]):
            return
        state = F.trade_offer_state(self, p, sp, sp.price)
        a = self.decide(p, TRADE_OFFER, state, legal, {"prop": target, "price": sp.price})
        if a == 0:
            return
        price = int(TRADE_MULTIPLIERS[a] * sp.price)
        rstate = F.trade_reply_state(self, seller, sp, price, p.pid)
        r = self.decide(seller, TRADE_REPLY, rstate, [True, True],
                        {"prop": target, "price": price})
        if r == 1:
            p.cash -= price
            seller.cash += price
            seller.props.discard(target)
            self.give_property(p, target)
            self.stats[p.pid]["trades_done"] += 1
            self.log("trade", buyer=p.pid, seller=seller.pid, prop=target, price=price)

    # ---------- jail ----------

    def jail_phase(self, p):
        legal = [True, p.cash >= B.JAIL_FINE, p.jail_cards > 0]
        state = F.jail_state(self, p)
        a = self.decide(p, JAIL, state, legal, {"turn": self.turn})
        if a == 1:
            p.cash -= B.JAIL_FINE
            p.in_jail = False
            p.jail_turns = 0
            return "out", None
        if a == 2:
            p.jail_cards -= 1
            p.in_jail = False
            p.jail_turns = 0
            return "out", None
        d1, d2 = self.dice()
        if d1 == d2:
            p.in_jail = False
            p.jail_turns = 0
            return "doubles", (d1, d2)
        p.jail_turns += 1
        if p.jail_turns >= 3:
            p.in_jail = False
            p.jail_turns = 0
            if self.charge(p, B.JAIL_FINE):
                return "out_forced", (d1, d2)
            return "stay", None
        return "stay", None

    # ---------- turn ----------

    def take_turn(self, p):
        if not p.alive:
            return
        self.unmortgage_pass(p)
        self.build_phase(p)
        self.trade_phase(p)
        if not p.alive:
            return
        if p.in_jail:
            res, roll = self.jail_phase(p)
            if res == "stay" or not p.alive:
                return
            if res in ("doubles", "out_forced"):
                self.advance(p, sum(roll))
                return
        doubles = 0
        while p.alive:
            d1, d2 = self.dice()
            if d1 == d2:
                doubles += 1
                if doubles == 3:
                    self.go_to_jail(p)
                    return
            self.advance(p, d1 + d2)
            if not p.alive or p.in_jail or d1 != d2:
                return

    def advance(self, p, steps):
        target = (p.position + steps) % 40
        self.move_to(p, target)
        self.resolve(p, steps)

    # ---------- main loop ----------

    def play(self, max_rounds=200):
        order = list(self.players)
        while self.turn < max_rounds and len(self.alive_players()) > 1:
            self.turn += 1
            for p in order:
                if p.alive and len(self.alive_players()) > 1:
                    self.take_turn(p)
        return self.finish()

    def finish(self):
        self.finished = True
        alive = self.alive_players()
        if len(alive) == 1:
            winner = alive[0].pid
            reason = "last_standing"
        else:
            winner = max(alive, key=lambda p: self.net_worth(p)).pid
            reason = "round_limit"
        ranking = sorted(
            self.players,
            key=lambda p: (p.alive, self.net_worth(p) if p.alive else 0,
                           p.bankrupt_turn or 0),
            reverse=True,
        )
        self.result = {
            "winner": winner,
            "reason": reason,
            "rounds": self.turn,
            "ranking": [p.pid for p in ranking],
            "players": [
                {
                    "pid": p.pid,
                    "name": p.name,
                    "alive": p.alive,
                    "cash": p.cash,
                    "net_worth": self.net_worth(p) if p.alive else 0,
                    "properties": sorted(p.props),
                    "houses": sum(self.houses[i] for i in p.props),
                    "bankrupt_round": p.bankrupt_turn,
                    **self.stats[p.pid],
                }
                for p in self.players
            ],
        }
        return self.result
