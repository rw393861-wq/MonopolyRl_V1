import random
import sys

from agents.baselines import HeuristicAgent, RandomAgent
from monopoly import board as B
from monopoly.game import Game


def check_invariants(game):
    errs = []
    houses_in_play = 0
    hotels_in_play = 0
    for i in B.BUYABLE_IDX:
        lvl = game.houses[i]
        if lvl < 0 or lvl > 5:
            errs.append(f"bad level {lvl} at {i}")
        if lvl and B.space(i).kind != B.STREET:
            errs.append(f"houses on non-street {i}")
        if lvl == 5:
            hotels_in_play += 1
        else:
            houses_in_play += lvl
        if lvl and game.mortgaged[i]:
            errs.append(f"houses on mortgaged {i}")
    if houses_in_play + game.houses_left != B.MAX_HOUSES:
        errs.append(f"house supply {houses_in_play}+{game.houses_left}")
    if hotels_in_play + game.hotels_left != B.MAX_HOTELS:
        errs.append(f"hotel supply {hotels_in_play}+{game.hotels_left}")
    for g in B.STREET_GROUPS:
        lv = [game.houses[i] for i in B.GROUPS[g]]
        if max(lv) - min(lv) > 1:
            errs.append(f"uneven build in {g}: {lv}")
        if max(lv) > 0 and game.group_owner(g) is None:
            errs.append(f"houses without monopoly in {g}")
    for p in game.players:
        for i in p.props:
            if game.owner[i] != p.pid:
                errs.append(f"owner mismatch {i}")
        if p.alive and p.cash < 0:
            errs.append(f"negative cash {p.name} {p.cash}")
        if not p.alive and p.props:
            errs.append(f"dead player holds props {p.name}")
    for i in B.BUYABLE_IDX:
        o = game.owner[i]
        if o is not None and i not in game.players[o].props:
            errs.append(f"orphan property {i}")
    return errs


def run(n=200, seed=5, max_rounds=200):
    rng = random.Random(seed)
    fails = 0
    reasons = {}
    for k in range(n):
        agents = [RandomAgent("r1", seed=rng.randrange(1000)),
                  RandomAgent("r2", seed=rng.randrange(1000)),
                  HeuristicAgent("h1")]
        for pid, a in enumerate(agents):
            a.begin_game(pid)
        game = Game(agents, seed=rng.randrange(1 << 30), max_rounds=max_rounds)
        result = game.play(max_rounds=max_rounds)
        reasons[result["reason"]] = reasons.get(result["reason"], 0) + 1
        errs = check_invariants(game)
        if errs:
            fails += 1
            print(f"game {k} seed {game.seed}:")
            for e in errs[:6]:
                print("   ", e)
    print(f"checked {n} games, {fails} with violations, endings {reasons}")
    return fails


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 200
    sys.exit(1 if run(n) else 0)
