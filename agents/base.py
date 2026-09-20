class Agent:
    def __init__(self, name):
        self.name = name

    def begin_game(self, pid):
        pass

    def act(self, decision):
        raise NotImplementedError

    def end_game(self, terminal_reward):
        pass

    def save(self, path):
        pass

    def load(self, path):
        pass


def first_legal(decision):
    for i, ok in enumerate(decision.legal):
        if ok:
            return i
    return 0
