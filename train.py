import os
import random
import time

from agents.baselines import HeuristicAgent
from agents.qlearning import QAgent
from monopoly.game import Game
from monopoly.logger import RunLogger

DEFAULT_NAMES = ("AI_1", "AI_2", "AI_3")


def make_agents(names=DEFAULT_NAMES, alpha=0.5, gamma=0.99, shaping=0.15, seed=0):
    return [QAgent(n, alpha=alpha, gamma=gamma, shaping=shaping, seed=seed + i)
            for i, n in enumerate(names)]


def rank_rewards(ranking, n):
    rewards = {}
    for place, pid in enumerate(ranking):
        rewards[pid] = 1.0 - 2.0 * place / max(1, n - 1)
    return rewards


def epsilon_at(game_idx, games, eps_start, eps_min, decay_frac):
    span = max(1, int(games * decay_frac))
    if game_idx >= span:
        return eps_min
    return eps_start + (eps_min - eps_start) * (game_idx / span)


def train(games=20000, max_rounds=200, seed=1, event_every=250, report_every=500,
          alpha=0.5, gamma=0.99, shaping=0.15, eps_start=1.0, eps_min=0.05,
          decay_frac=0.7, model_dir="models", log_root="logs", resume=False,
          baseline_rate=0.0, quiet=False):
    rng = random.Random(seed)
    agents = make_agents(alpha=alpha, gamma=gamma, shaping=shaping, seed=seed)
    if resume:
        for a in agents:
            path = os.path.join(model_dir, a.name + ".json")
            if os.path.exists(path):
                a.load(path)
    meta = {"games": games, "max_rounds": max_rounds, "seed": seed, "alpha": alpha,
            "gamma": gamma, "shaping": shaping, "eps_start": eps_start,
            "eps_min": eps_min, "decay_frac": decay_frac,
            "agents": [a.name for a in agents], "baseline_rate": baseline_rate,
            "mode": "train"}
    logger = RunLogger(log_root, "train", meta)
    wins = {a.name: 0 for a in agents}
    window = {a.name: 0 for a in agents}
    window_rounds = 0
    window_limit = 0
    t0 = time.time()

    for g in range(games):
        eps = epsilon_at(g, games, eps_start, eps_min, decay_frac)
        order = agents[g % len(agents):] + agents[:g % len(agents)]
        if baseline_rate and rng.random() < baseline_rate:
            seat = rng.randrange(len(order))
            order = list(order)
            order[seat] = HeuristicAgent("rulebot")
        for pid, a in enumerate(order):
            a.epsilon = eps
            a.training = True
            a.begin_game(pid)
        game = Game(order, seed=rng.randrange(1 << 30), max_rounds=max_rounds,
                    record_events=(event_every > 0 and g % event_every == 0))
        result = game.play(max_rounds=max_rounds)
        rewards = rank_rewards(result["ranking"], len(order))
        for pid, a in enumerate(order):
            a.end_game(rewards[pid])
        name = game.players[result["winner"]].name
        wins[name] = wins.get(name, 0) + 1
        window[name] = window.get(name, 0) + 1
        window_rounds += result["rounds"]
        window_limit += 1 if result["reason"] == "round_limit" else 0
        logger.log_game(g, game, result, eps)

        if report_every and (g + 1) % report_every == 0:
            row = {"game": g + 1, "epsilon": round(eps, 4),
                   "avg_rounds": round(window_rounds / report_every, 2),
                   "round_limit_pct": round(100 * window_limit / report_every, 1),
                   "elapsed_s": round(time.time() - t0, 1)}
            for a in agents:
                row[a.name + "_winrate"] = round(window.get(a.name, 0) / report_every, 3)
                row[a.name + "_states"] = a.states_seen()
            logger.log_metrics(row)
            if not quiet:
                rates = " ".join(f"{a.name}:{window.get(a.name, 0) / report_every:.2f}"
                                 for a in agents)
                print(f"game {g + 1}/{games} eps={eps:.3f} {rates} "
                      f"avg_rounds={row['avg_rounds']} "
                      f"states={sum(a.states_seen() for a in agents)}")
            window = {a.name: 0 for a in agents}
            window_rounds = 0
            window_limit = 0
        logger.flush() if (g + 1) % 2000 == 0 else None

    for a in agents:
        a.save(os.path.join(model_dir, a.name + ".json"))
    logger.close()
    if not quiet:
        print("total wins:", wins)
        print("models saved to", os.path.abspath(model_dir))
        print("logs written to", os.path.abspath(logger.dir))
    return agents, logger.dir, wins
