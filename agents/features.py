from monopoly.board import GROUPS, STREET_GROUPS

CASH_BANDS = (50, 200, 600)
BID_BANDS = (0.5, 1.0, 1.5)
PRICE_BANDS = (1.25, 2.0)


def band(value, bands):
    i = 0
    for b in bands:
        if value >= b:
            i += 1
        else:
            break
    return i


def cash_b(cash):
    return band(cash, CASH_BANDS)


def wealth_b(game, p):
    return band(game.advantage(p), (-0.07, 0.07))


def phase(turn):
    return 0 if turn < 30 else 1


def cap(n, m=2):
    return n if n < m else m


def group_counts(game, group, pid):
    idxs = GROUPS[group]
    mine = 0
    others = {}
    for i in idxs:
        o = game.owner[i]
        if o == pid:
            mine += 1
        elif o is not None:
            others[o] = others.get(o, 0) + 1
    best_other = max(others.values()) if others else 0
    return mine, best_other, len(idxs)


def monopolies(game, pid):
    return sum(1 for g in STREET_GROUPS if game.group_owner(g) == pid)


def opp_monopolies(game, pid):
    return sum(1 for g in STREET_GROUPS if game.group_owner(g) not in (None, pid))


def buy_state(game, p, sp):
    mine, best_other, size = group_counts(game, sp.group, p.pid)
    return (
        sp.group,
        cash_b(p.cash),
        cap(mine),
        1 if mine + 1 == size else 0,
        1 if best_other + 1 == size else 0,
        wealth_b(game, p),
        phase(game.turn),
    )


def auction_state(game, p, sp):
    mine, best_other, size = group_counts(game, sp.group, p.pid)
    return (
        sp.group,
        cash_b(p.cash),
        cap(mine),
        1 if mine + 1 == size else 0,
        1 if best_other + 1 == size else 0,
        wealth_b(game, p),
    )


def build_state(game, p, group, level):
    return (group, level, cash_b(p.cash), wealth_b(game, p),
            cap(opp_monopolies(game, p.pid), 1))


def jail_state(game, p):
    return (
        p.jail_turns,
        cash_b(p.cash),
        1 if p.jail_cards else 0,
        wealth_b(game, p),
        cap(opp_monopolies(game, p.pid), 1),
        phase(game.turn),
    )


def trade_offer_state(game, p, sp, target_cash):
    return (sp.group, cash_b(p.cash), phase(game.turn))


def trade_reply_state(game, p, sp, price, buyer):
    mine, _, size = group_counts(game, sp.group, p.pid)
    return (
        sp.group,
        band(price / max(1, sp.price), PRICE_BANDS),
        cash_b(p.cash),
        cap(mine),
    )
