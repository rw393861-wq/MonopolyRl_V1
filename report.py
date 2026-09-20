import json
import os

from monopoly.board import GROUPS, space

BARS = " .:-=+*#%@"


def latest_run(log_root="logs", prefix=""):
    if not os.path.isdir(log_root):
        return None
    runs = [d for d in os.listdir(log_root)
            if d.startswith(prefix) and os.path.isdir(os.path.join(log_root, d))]
    if not runs:
        return None
    return os.path.join(log_root, sorted(runs)[-1])


def load_games(run_dir):
    path = os.path.join(run_dir, "games.jsonl")
    with open(path, encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def bar(value, lo, hi, width=28):
    if hi <= lo:
        return ""
    frac = max(0.0, min(1.0, (value - lo) / (hi - lo)))
    filled = int(round(frac * width))
    return "#" * filled + "-" * (width - filled)


def windows(games, n=10):
    size = max(1, len(games) // n)
    return [games[i:i + size] for i in range(0, len(games), size)][:n]


def build_report(run_dir, out_name="report.md"):
    games = load_games(run_dir)
    if not games:
        return None
    names = [p["name"] for p in games[0]["players"]]
    total = len(games)
    wins = {n: 0 for n in names}
    props = {n: 0 for n in names}
    houses = {n: 0 for n in names}
    rent = {n: 0 for n in names}
    trades = {n: 0 for n in names}
    reasons = {}
    rounds = 0
    ownership = {}

    for g in games:
        wins[g["winner_name"]] = wins.get(g["winner_name"], 0) + 1
        reasons[g["reason"]] = reasons.get(g["reason"], 0) + 1
        rounds += g["rounds"]
        for p in g["players"]:
            n = p["name"]
            props[n] = props.get(n, 0) + len(p["properties"])
            houses[n] = houses.get(n, 0) + p["houses_built"]
            rent[n] = rent.get(n, 0) + p["rent_received"]
            trades[n] = trades.get(n, 0) + p["trades_done"]
            if n == g["winner_name"]:
                for i in p["properties"]:
                    ownership[i] = ownership.get(i, 0) + 1

    lines = []
    lines.append("# Monopoly self-play report")
    lines.append("")
    lines.append(f"Run directory: `{run_dir}`")
    lines.append(f"Games logged: {total}")
    lines.append(f"Average rounds per game: {rounds / total:.1f}")
    lines.append("")
    lines.append("## Overall win share")
    lines.append("")
    lines.append("| agent | wins | share |")
    lines.append("|---|---|---|")
    for n in names:
        lines.append(f"| {n} | {wins.get(n, 0)} | {100 * wins.get(n, 0) / total:.1f}% |")
    lines.append("")
    lines.append("## End condition")
    lines.append("")
    for k, v in reasons.items():
        lines.append(f"- {k}: {v} ({100 * v / total:.1f}%)")
    lines.append("")
    lines.append("## Win rate over training windows")
    lines.append("")
    ws = windows(games, 10)
    header = "| window | games | " + " | ".join(names) + " | avg rounds |"
    lines.append(header)
    lines.append("|" + "---|" * (len(names) + 3))
    for i, w in enumerate(ws):
        row = [f"| {i + 1} | {len(w)} "]
        for n in names:
            c = sum(1 for g in w if g["winner_name"] == n)
            row.append(f"| {100 * c / len(w):.0f}% ")
        row.append(f"| {sum(g['rounds'] for g in w) / len(w):.0f} |")
        lines.append("".join(row))
    lines.append("")
    lines.append("## Per-agent averages")
    lines.append("")
    lines.append("| agent | props held | houses built | rent received | trades |")
    lines.append("|---|---|---|---|---|")
    for n in names:
        lines.append(f"| {n} | {props[n] / total:.1f} | {houses[n] / total:.1f} "
                     f"| {rent[n] / total:.0f} | {trades[n] / total:.2f} |")
    lines.append("")
    lines.append("## Properties most often held by the winner")
    lines.append("")
    top = sorted(ownership.items(), key=lambda kv: -kv[1])[:12]
    hi = top[0][1] if top else 1
    for idx, count in top:
        sp = space(idx)
        lines.append(f"- {sp.name:<24} {100 * count / total:5.1f}%  "
                     f"{bar(count, 0, hi)}")
    lines.append("")
    lines.append("## Colour group pull rate (winner)")
    lines.append("")
    for g, idxs in GROUPS.items():
        c = sum(ownership.get(i, 0) for i in idxs)
        lines.append(f"- {g:<10} {c / (total * len(idxs)):.2f} per space")
    text = "\n".join(lines) + "\n"
    out = os.path.join(run_dir, out_name)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(text)
    return out
