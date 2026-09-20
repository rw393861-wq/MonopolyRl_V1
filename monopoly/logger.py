import csv
import json
import os
import time


class RunLogger:
    def __init__(self, root="logs", tag="run", meta=None):
        stamp = time.strftime("%Y%m%d-%H%M%S")
        self.dir = os.path.join(root, f"{tag}-{stamp}")
        os.makedirs(self.dir, exist_ok=True)
        self.games_path = os.path.join(self.dir, "games.jsonl")
        self.events_path = os.path.join(self.dir, "events.jsonl")
        self.csv_path = os.path.join(self.dir, "games.csv")
        self.metrics_path = os.path.join(self.dir, "training.csv")
        self.games_fh = open(self.games_path, "w", encoding="utf-8")
        self.events_fh = open(self.events_path, "w", encoding="utf-8")
        self.csv_fh = open(self.csv_path, "w", newline="", encoding="utf-8")
        self.metrics_fh = open(self.metrics_path, "w", newline="", encoding="utf-8")
        self.csv_writer = None
        self.metrics_writer = None
        self.n_games = 0
        with open(os.path.join(self.dir, "meta.json"), "w", encoding="utf-8") as fh:
            json.dump(meta or {}, fh, indent=2)

    def log_game(self, game_id, game, result, epsilon=None):
        self.n_games += 1
        record = {
            "game_id": game_id,
            "seed": game.seed,
            "winner": result["winner"],
            "winner_name": game.players[result["winner"]].name,
            "reason": result["reason"],
            "rounds": result["rounds"],
            "ranking": result["ranking"],
            "epsilon": epsilon,
            "players": result["players"],
        }
        self.games_fh.write(json.dumps(record) + "\n")
        if game.events:
            self.events_fh.write(json.dumps(
                {"game_id": game_id, "events": game.events}) + "\n")
        flat = {
            "game_id": game_id,
            "winner": record["winner_name"],
            "reason": record["reason"],
            "rounds": record["rounds"],
            "epsilon": round(epsilon, 4) if epsilon is not None else "",
        }
        for seat, p in enumerate(result["players"]):
            flat[f"p{seat}_name"] = p["name"]
            flat[f"p{seat}_net_worth"] = p["net_worth"]
            flat[f"p{seat}_props"] = len(p["properties"])
            flat[f"p{seat}_bought"] = p["bought"]
            flat[f"p{seat}_houses"] = p["houses_built"]
            flat[f"p{seat}_rent_recv"] = p["rent_received"]
            flat[f"p{seat}_bankrupt_round"] = p["bankrupt_round"] or ""
        if self.csv_writer is None:
            self.csv_writer = csv.DictWriter(self.csv_fh, fieldnames=list(flat))
            self.csv_writer.writeheader()
        self.csv_writer.writerow(flat)

    def log_metrics(self, row):
        if self.metrics_writer is None:
            self.metrics_writer = csv.DictWriter(self.metrics_fh, fieldnames=list(row))
            self.metrics_writer.writeheader()
        self.metrics_writer.writerow(row)
        self.metrics_fh.flush()

    def flush(self):
        self.games_fh.flush()
        self.events_fh.flush()
        self.csv_fh.flush()

    def close(self):
        for fh in (self.games_fh, self.events_fh, self.csv_fh, self.metrics_fh):
            fh.close()
