import json
import os
import random

from agents.base import Agent
from monopoly.actions import ACTION_SPACES

NEG = -1e9


class QAgent(Agent):
    def __init__(self, name, alpha=0.5, gamma=0.99, epsilon=1.0,
                 epsilon_min=0.05, shaping=0.15, alpha_min=0.02,
                 alpha_decay=0.6, seed=None):
        super().__init__(name)
        self.alpha = alpha
        self.alpha_min = alpha_min
        self.alpha_decay = alpha_decay
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.shaping = shaping
        self.rng = random.Random(seed)
        self.q = {}
        self.n = {}
        self.training = True
        self.games_trained = 0
        self.updates = 0
        self.pid = None
        self.prev = None
        self.prev_phi = None
        self.pending = 0.0

    # ---------- table ----------

    def key(self, dtype, state):
        return dtype + "|" + "|".join(str(x) for x in state)

    def row(self, dtype, state):
        k = self.key(dtype, state)
        r = self.q.get(k)
        if r is None:
            r = [0.0] * ACTION_SPACES[dtype]
            self.q[k] = r
            self.n[k] = [0] * ACTION_SPACES[dtype]
        return r

    def step_size(self, k, a):
        counts = self.n.setdefault(k, [0] * len(self.q[k]))
        counts[a] += 1
        return max(self.alpha_min, self.alpha / (counts[a] ** self.alpha_decay))

    def best_value(self, dtype, state, legal):
        r = self.row(dtype, state)
        vals = [r[i] for i, ok in enumerate(legal) if ok]
        return max(vals) if vals else 0.0

    # ---------- episode ----------

    def begin_game(self, pid):
        self.pid = pid
        self.prev = None
        self.prev_phi = None
        self.pending = 0.0

    def act(self, decision):
        legal = decision.legal
        if self.training and self.prev is not None:
            reward = self.shaping * decision.potential
            target = reward + self.gamma * self.best_value(
                decision.dtype, decision.state, legal)
            self.update(self.prev, target)
        choices = [i for i, ok in enumerate(legal) if ok]
        if not choices:
            return 0
        if self.training and self.rng.random() < self.epsilon:
            a = self.rng.choice(choices)
        else:
            r = self.row(decision.dtype, decision.state)
            best = max(choices, key=lambda i: (r[i], self.rng.random()))
            a = best
        self.prev = (decision.dtype, decision.state, a)
        self.prev_phi = decision.potential
        self.pending = 0.0
        return a

    def end_game(self, terminal_reward):
        if self.training and self.prev is not None:
            self.update(self.prev, terminal_reward)
        self.games_trained += 1
        self.prev = None

    def update(self, prev, target):
        dtype, state, a = prev
        r = self.row(dtype, state)
        lr = self.step_size(self.key(dtype, state), a)
        r[a] += lr * (target - r[a])
        self.updates += 1

    # ---------- persistence ----------

    def save(self, path):
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        data = {
            "name": self.name,
            "alpha": self.alpha,
            "gamma": self.gamma,
            "epsilon": self.epsilon,
            "games_trained": self.games_trained,
            "updates": self.updates,
            "q": {k: [round(v, 5) for v in row] for k, row in self.q.items()},
            "n": self.n,
        }
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh)

    def load(self, path):
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        self.q = {k: list(v) for k, v in data["q"].items()}
        self.n = {k: list(v) for k, v in data.get("n", {}).items()}
        self.games_trained = data.get("games_trained", 0)
        self.updates = data.get("updates", 0)
        self.epsilon = data.get("epsilon", self.epsilon)
        return self

    def states_seen(self):
        return len(self.q)
