import random

from agents.base import Agent
from monopoly.actions import AUCTION, BUILD, BUY, JAIL, TRADE_OFFER, TRADE_REPLY
from monopoly.board import space


class RandomAgent(Agent):
    def __init__(self, name="random", seed=None):
        super().__init__(name)
        self.rng = random.Random(seed)

    def act(self, decision):
        choices = [i for i, ok in enumerate(decision.legal) if ok]
        return self.rng.choice(choices) if choices else 0


class HeuristicAgent(Agent):
    def __init__(self, name="heuristic"):
        super().__init__(name)

    def act(self, decision):
        d, legal, meta = decision.dtype, decision.legal, decision.meta
        if d == BUY:
            return 1 if legal[1] else 0
        if d == AUCTION:
            return 2 if legal[2] else (1 if legal[1] else 0)
        if d == BUILD:
            return 1
        if d == JAIL:
            if meta.get("turn", 0) < 30 and legal[1]:
                return 1
            return 2 if legal[2] else 0
        if d == TRADE_OFFER:
            return 2 if legal[2] else (1 if legal[1] else 0)
        if d == TRADE_REPLY:
            return 1 if meta["price"] >= 2 * space(meta["prop"]).price else 0
        return 0
