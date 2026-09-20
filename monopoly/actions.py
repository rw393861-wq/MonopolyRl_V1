BUY = "buy"
AUCTION = "auction"
BUILD = "build"
JAIL = "jail"
TRADE_OFFER = "trade_offer"
TRADE_REPLY = "trade_reply"

ACTION_SPACES = {
    BUY: 2,
    AUCTION: 4,
    BUILD: 2,
    JAIL: 3,
    TRADE_OFFER: 4,
    TRADE_REPLY: 2,
}

ACTION_NAMES = {
    BUY: ("pass", "buy"),
    AUCTION: ("no_bid", "max_half", "max_list", "max_over"),
    BUILD: ("skip", "build"),
    JAIL: ("roll", "pay_fine", "use_card"),
    TRADE_OFFER: ("no_offer", "offer_1x", "offer_1_5x", "offer_2_5x"),
    TRADE_REPLY: ("reject", "accept"),
}

TRADE_MULTIPLIERS = (0.0, 1.0, 1.5, 2.5)
AUCTION_LEVELS = (0.0, 0.5, 0.9, 1.3)


class Decision:
    __slots__ = ("dtype", "state", "legal", "meta", "potential")

    def __init__(self, dtype, state, legal, potential, meta=None):
        self.dtype = dtype
        self.state = state
        self.legal = legal
        self.potential = potential
        self.meta = meta or {}

    @property
    def n_actions(self):
        return ACTION_SPACES[self.dtype]
