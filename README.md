# Monopoly RL

Full Monopoly rules engine plus three reinforcement learning agents that learn the
game from zero by playing each other. Every game is logged. Pure Python 3.9+,
standard library only, no installs.

## Quick start (PowerShell)

```powershell
cd monopoly_rl
python tests.py 200
python run.py train --games 20000
python run.py eval --games 500 --mode selfplay
python run.py eval --games 500 --mode vs_heuristic
python run.py demo --seed 7
```

Training writes `models\AI_1.json`, `models\AI_2.json`, `models\AI_3.json` and a
timestamped folder under `logs\`.

## Putting it on GitHub

The repo is push ready. From the project folder:

```powershell
git init
git add .
git commit -m "monopoly rl"
gh repo create monopoly-rl --public --source . --push
```

Without the `gh` CLI, create the empty repo on github.com first, then:

```powershell
git remote add origin https://github.com/<your-user>/monopoly-rl.git
git branch -M main
git push -u origin main
```

Make it public. Standard GitHub hosted runners are free without a practical minute
limit on public repositories; private repositories draw on a 2,000 minute monthly
allowance instead.

`.github\workflows\train.yml` then trains in the cloud for free. It runs the
invariant tests, trains with `--resume` so every run continues the committed tables,
benchmarks against the baselines, uploads the full logs as a run artifact, and commits
the updated tables plus each run's `report.md` and `training.csv` into `history\`.
Trigger it by hand from the Actions tab, or leave the daily cron to accumulate games
while you do nothing. One setting needs your attention once: Settings, Actions,
General, Workflow permissions, set to read and write, or the commit step is rejected.

Jobs are capped at six hours, which is the reason for the chunked resumable design.
A run of 60,000 games finishes well inside that.

## Commands

| command | purpose |
|---|---|
| `python run.py train` | self-play training for the three agents |
| `python run.py eval` | fixed games with exploration and learning off |
| `python run.py report` | rebuild `report.md` for a run folder |
| `python run.py demo` | play one game and print every event |
| `python tests.py 300` | rules invariant checks over 300 random games |

Useful train flags: `--games`, `--max-rounds`, `--alpha`, `--gamma`, `--shaping`,
`--eps-start`, `--eps-min`, `--decay-frac`, `--baseline-rate`, `--event-every`,
`--resume`, `--seed`.

Eval modes: `selfplay`, `vs_random`, `vs_heuristic`, `arena`, `baselines`.
`arena` is the fair one: one trained agent, one random, one rule based, in the same
game, seats rotated.

## What the agents start with

Nothing. Q-tables are empty, all values zero, and the first thousand games are
near-random. No property rankings, no opening book, no hand-written strategy. The
only inputs are the legal action list, the abstracted state, and the reward.

## Rewards

Two parts.

Terminal reward by finishing place: `+1` for first, `0` for second, `-1` for third.

Dense reward at every decision: `shaping * advantage`, where advantage is the
player's share of the net worth still on the board minus an even share. Leading pays
a little every step, trailing costs a little every step. Net worth counts cash,
unmortgaged property at face price, mortgaged property at mortgage value and
buildings at build cost, so buying, building and mortgaging are all value neutral at
the instant they happen and only their consequences move the reward.

An earlier version used potential based shaping, `gamma * phi(next) - phi(now)`.
That is the textbook choice and it is policy invariant, but that is exactly the
problem here: the shaping sum telescopes, so it contributes nothing that separates
one action from another, and all the discrimination has to come from a terminal
reward discounted across roughly a hundred decisions. Measured Q values for buy
versus pass came out equal to three decimal places after thousands of visits each.
The advantage reward does not telescope, and the same tables then separate cleanly.

Set `--shaping 0` for the win or lose signal alone. It trains, and it is much worse.

## Results, and what went wrong on the way

The shipped tables come from 18,000 games with `--baseline-rate 0.34`. In the arena
the best agent wins about 28 percent of games against a random and a rule based
opponent, where an even split is 33 percent. The rule based opponent wins about 46
percent. So the agents learn real play from nothing, comfortably beat random in
self-play terms, and still lose to twenty lines of hand written rules.

Three failures were worth more than the final number.

Pure self-play collapsed into collusion. With three learners and nobody else, the
agents stopped building. Once nobody builds, monopolies are harmless, so they also
started selling each other set completing properties. Against any opponent who does
build, that policy scored 2 percent. The `--baseline-rate` flag mixes a rule based
opponent into a fraction of training games and breaks the equilibrium: same settings,
23 percent instead of 2. Set it to 0 for pure three way self-play and watch it happen.

The value function could not see its own investments. The reward tracks net worth but
the state only encoded cash, so converting cash into houses looked like moving to a
poorer state and the agents learned never to build. An ablation, replacing one
decision head at a time with the rule based version, isolated it:

| head replaced by rules | arena win rate |
|---|---|
| none, pure tables | 0.20 |
| buy | 0.175 |
| auction | 0.30 |
| build | 0.40 |
| jail | 0.215 |
| trade offer | 0.19 |
| trade reply | 0.19 |

Every head except build was fine or better than the rules. `wealth_b` in
`features.py` is the fix, a three bucket view of net worth position.

Learning rate and exploration floors were too low. A constant step size averages only
the last few samples, which cannot resolve action gaps of 0.01 against dice noise, so
the step size now decays with visit count. Floors that decay too far freeze a bad
early policy in place before the rest of the agent is good enough to reveal it was
bad. `--eps-min 0.12` and `alpha_min 0.02` were worth roughly 8 points.

Obvious next steps: a larger league of frozen past selves, linear function
approximation instead of a table, and letting the agents learn how to raise cash
rather than scripting it.

## Learning method

Tabular Q-learning, one table per agent, epsilon greedy with a linear decay, updated
at every decision point rather than every dice roll. The update target for a decision
is the reward collected since that decision plus the discounted best value of the next
decision the agent faces, so the engine is treated as a semi Markov process and the
dice rolls in between are absorbed into the reward.

The agents share no tables. They learn separately from a common stream of games, so
each one develops its own valuations and they act as each other's curriculum.

## Decisions the agents control

- buy a property at list price or send it to auction
- bid in an auction: no bid, or a maximum of 0.5x, 0.9x or 1.3x list price
- develop a chosen colour group, which builds as many houses as cash allows
- jail: roll for doubles, pay the fine, use a card
- offer to buy a property that completes a set, at 1x, 1.5x or 2.5x list price
- accept or reject such an offer

Raising cash when short is scripted, not learned: mortgage the cheapest free property
first, then sell buildings from the most developed cheap group. This keeps the action
space small enough for tabular learning.

## State abstraction

Raw Monopoly states are far too many to tabulate, so each decision gets a small
bucketed view: colour group, cash band, how many of that group each side holds,
whether the property completes or blocks a set, current bid as a fraction of list
price, and an early or late game flag. Around 3,000 distinct states appear in total,
which is the reason the agents converge in tens of thousands of games instead of
millions. `agents\features.py` holds all of it.

## Logging

Each run creates `logs\<tag>-<timestamp>\` containing:

- `games.jsonl` — one line per game: seed, winner, reason, rounds, ranking, epsilon,
  and per player final cash, net worth, properties, houses built, rent paid and
  received, trades, bankruptcy round
- `games.csv` — same games flattened for a spreadsheet
- `events.jsonl` — full move by move log for sampled games, controlled by
  `--event-every`
- `training.csv` — win rate, average game length, table size per window
- `report.md` — written at the end of the run
- `meta.json` — the settings the run used

## Rules covered

Standard 40 space US board, full Chance and Community Chest decks, rent tables,
colour group double rent, railroads and utilities, even building, the 32 house and
12 hotel supply limits, mortgages with 10 percent interest to lift, jail with fine,
doubles and cards, three doubles to jail, auctions for any declined or repossessed
property, bankruptcy to a player or to the bank, and a round limit that awards the
game on net worth.

Auctions run as sealed maximum bids: every player names the most they will pay, the
highest bidder wins and pays one increment above the second highest. For players with
fixed valuations that lands on the same outcome as calling out rising bids, and it
turns a long chain of decisions into a single one, which matters a lot for learning.

Deliberately left out: free parking jackpots and other house rules, multi property
trades, and bidding above cash on hand.

## Layout

```
monopoly_rl\
  run.py            command line entry point
  train.py          self-play loop and epsilon schedule
  evaluate.py       fixed matches, loads saved tables
  report.py         turns a log folder into report.md
  tests.py          rules invariant checks
  monopoly\
    board.py        40 spaces, groups, rents, prices
    cards.py        Chance and Community Chest
    player.py       player state
    actions.py      decision types and action spaces
    game.py         the rules engine
    logger.py       run logging
  agents\
    base.py         agent interface
    qlearning.py    the learning agent
    baselines.py    random and fixed rule opponents
    features.py     state abstraction
  models\           saved Q-tables
  logs\             one folder per run
```
