import os
import random

from agents.baselines import HeuristicAgent, RandomAgent
from agents.qlearning import QAgent
from monopoly.game import Game
from monopoly.logger import RunLogger
from train import DEFAULT_NAMES


def load_agents(model_dir="models", names=DEFAULT_NAMES):
    out = []
    for n in names:
        a = QAgent(n)
        path = os.path.join(model_dir, n + ".json")
        if os.path.exists(path):
            a.load(path)
        a.training = False
        a.epsilon = 0.0
        out.append(a)
    return out


def build_lineup(mode, model_dir):
    trained = load_agents(model_dir)
    if mode == "selfplay":
        return trained
    if mode == "vs_random":
        return [trained[0], RandomAgent("random_1", seed=7),
                RandomAgent("random_2", seed=8)]
    if mode == "vs_heuristic":
        return [trained[0], HeuristicAgent("heuristic_1"),
                HeuristicAgent("heuristic_2")]
    if mode == "arena":
        return [trained[0], RandomAgent("random_1", seed=7),
                HeuristicAgent("heuristic_1")]
    if mode == "baselines":
        return [RandomAgent("random_1", seed=7), RandomAgent("random_2", seed=8),
                HeuristicAgent("heuristic_1")]
    raise ValueError("unknown mode " + mode)


def evaluate(games=500, mode="selfplay", model_dir="models", max_rounds=200,
             seed=99, log_root="logs", event_every=50, quiet=False):
    rng = random.Random(seed)
    lineup = build_lineup(mode, model_dir)
    meta = {"mode": "evaluate:" + mode, "games": games, "seed": seed,
            "agents": [a.name for a in lineup]}
    logger = RunLogger(log_root, "eval-" + mode, meta)
    wins = {a.name: 0 for a in lineup}
    rounds_total = 0
    for g in range(games):
        order = lineup[g % len(lineup):] + lineup[:g % len(lineup)]
        for pid, a in enumerate(order):
            a.begin_game(pid)
        game = Game(order, seed=rng.randrange(1 << 30), max_rounds=max_rounds,
                    record_events=(event_every > 0 and g % event_every == 0))
        result = game.play(max_rounds=max_rounds)
        for a in order:
            a.end_game(0.0)
        wins[game.players[result["winner"]].name] += 1
        rounds_total += result["rounds"]
        logger.log_game(g, game, result, 0.0)
    logger.close()
    if not quiet:
        print(f"mode={mode} games={games} avg_rounds={rounds_total / games:.1f}")
        for k, v in sorted(wins.items(), key=lambda kv: -kv[1]):
            print(f"  {k:<14} wins {v:>5}  ({100 * v / games:.1f}%)")
        print("logs written to", os.path.abspath(logger.dir))
    return wins, logger.dir
