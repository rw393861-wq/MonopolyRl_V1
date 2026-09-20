import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from evaluate import evaluate, load_agents
from monopoly.game import Game
from monopoly.logger import RunLogger
from report import build_report, latest_run
from train import train


def cmd_train(a):
    train(games=a.games, max_rounds=a.max_rounds, seed=a.seed,
          event_every=a.event_every, report_every=a.report_every,
          alpha=a.alpha, gamma=a.gamma, shaping=a.shaping,
          eps_start=a.eps_start, eps_min=a.eps_min, decay_frac=a.decay_frac,
          model_dir=a.model_dir, log_root=a.log_root, resume=a.resume,
          baseline_rate=a.baseline_rate)
    run = latest_run(a.log_root, "train")
    if run and a.report:
        print("report written to", build_report(run))


def cmd_eval(a):
    evaluate(games=a.games, mode=a.mode, model_dir=a.model_dir,
             max_rounds=a.max_rounds, seed=a.seed, log_root=a.log_root)
    run = latest_run(a.log_root, "eval")
    if run and a.report:
        print("report written to", build_report(run))


def cmd_report(a):
    run = a.run or latest_run(a.log_root, a.prefix)
    if not run:
        print("no run directory found")
        return
    print("report written to", build_report(run))


def cmd_demo(a):
    agents = load_agents(a.model_dir)
    for pid, ag in enumerate(agents):
        ag.begin_game(pid)
    logger = RunLogger(a.log_root, "demo", {"mode": "demo", "seed": a.seed})
    game = Game(agents, seed=a.seed, max_rounds=a.max_rounds, record_events=True)
    result = game.play(max_rounds=a.max_rounds)
    logger.log_game(0, game, result, 0.0)
    logger.close()
    for ev in game.events:
        who = game.players[ev["p"]].name if "p" in ev else ""
        detail = {k: v for k, v in ev.items() if k not in ("e", "t", "p")}
        print(f"r{ev['t']:>3} {who:<8} {ev['e']:<12} {detail}")
    print()
    print("winner:", game.players[result["winner"]].name, "-", result["reason"])
    for p in result["players"]:
        print(f"  {p['name']:<8} net={p['net_worth']:<6} props={len(p['properties'])} "
              f"houses={p['houses']} rent_recv={p['rent_received']}")
    print("log written to", os.path.abspath(logger.dir))


def main():
    ap = argparse.ArgumentParser(description="Monopoly reinforcement learning sandbox")
    sub = ap.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("train", help="self-play training for the three agents")
    t.add_argument("--games", type=int, default=20000)
    t.add_argument("--max-rounds", type=int, default=200)
    t.add_argument("--seed", type=int, default=1)
    t.add_argument("--alpha", type=float, default=0.5)
    t.add_argument("--gamma", type=float, default=0.99)
    t.add_argument("--shaping", type=float, default=0.15)
    t.add_argument("--eps-start", type=float, default=1.0)
    t.add_argument("--eps-min", type=float, default=0.05)
    t.add_argument("--decay-frac", type=float, default=0.7)
    t.add_argument("--event-every", type=int, default=250)
    t.add_argument("--report-every", type=int, default=500)
    t.add_argument("--model-dir", default="models")
    t.add_argument("--log-root", default="logs")
    t.add_argument("--resume", action="store_true")
    t.add_argument("--baseline-rate", type=float, default=0.0)
    t.add_argument("--no-report", dest="report", action="store_false")
    t.set_defaults(func=cmd_train, report=True)

    e = sub.add_parser("eval", help="play fixed games with learning switched off")
    e.add_argument("--games", type=int, default=500)
    e.add_argument("--mode", default="selfplay",
                   choices=["selfplay", "vs_random", "vs_heuristic", "arena",
                            "baselines"])
    e.add_argument("--max-rounds", type=int, default=200)
    e.add_argument("--seed", type=int, default=99)
    e.add_argument("--model-dir", default="models")
    e.add_argument("--log-root", default="logs")
    e.add_argument("--no-report", dest="report", action="store_false")
    e.set_defaults(func=cmd_eval, report=True)

    r = sub.add_parser("report", help="build report.md for a run directory")
    r.add_argument("--run", default=None)
    r.add_argument("--log-root", default="logs")
    r.add_argument("--prefix", default="")
    r.set_defaults(func=cmd_report)

    d = sub.add_parser("demo", help="play and print one narrated game")
    d.add_argument("--seed", type=int, default=7)
    d.add_argument("--max-rounds", type=int, default=200)
    d.add_argument("--model-dir", default="models")
    d.add_argument("--log-root", default="logs")
    d.set_defaults(func=cmd_demo)

    a = ap.parse_args()
    a.func(a)


if __name__ == "__main__":
    main()
