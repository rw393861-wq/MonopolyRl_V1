class Player:
    def __init__(self, pid, name, cash):
        self.pid = pid
        self.name = name
        self.cash = cash
        self.position = 0
        self.in_jail = False
        self.jail_turns = 0
        self.jail_cards = 0
        self.alive = True
        self.bankrupt_turn = None
        self.props = set()

    def __repr__(self):
        return f"<{self.name} cash={self.cash} props={len(self.props)}>"
