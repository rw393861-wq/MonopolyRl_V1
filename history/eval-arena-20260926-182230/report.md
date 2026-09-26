# Monopoly self-play report

Run directory: `logs/eval-arena-20260926-182230`
Games logged: 300
Average rounds per game: 62.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 28 | 9.3% |
| random_1 | 116 | 38.7% |
| heuristic_1 | 156 | 52.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 30% | 67% | 62 |
| 2 | 30 | 10% | 40% | 50% | 57 |
| 3 | 30 | 7% | 43% | 50% | 62 |
| 4 | 30 | 7% | 37% | 57% | 61 |
| 5 | 30 | 0% | 47% | 53% | 72 |
| 6 | 30 | 13% | 43% | 43% | 58 |
| 7 | 30 | 20% | 33% | 47% | 65 |
| 8 | 30 | 3% | 37% | 60% | 58 |
| 9 | 30 | 10% | 33% | 57% | 64 |
| 10 | 30 | 20% | 43% | 37% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.4 | 4.5 | 1202 | 0.58 |
| random_1 | 10.7 | 18.8 | 3302 | 1.49 |
| heuristic_1 | 14.2 | 26.5 | 4074 | 2.20 |

## Properties most often held by the winner

- B&O Railroad              99.3%  ############################
- Vermont Avenue            99.0%  ############################
- St. James Place           99.0%  ############################
- New York Avenue           99.0%  ############################
- Illinois Avenue           99.0%  ############################
- Tennessee Avenue          98.7%  ############################
- St. Charles Place         98.0%  ############################
- States Avenue             98.0%  ############################
- Marvin Gardens            98.0%  ############################
- Short Line                98.0%  ############################
- Electric Company          97.7%  ############################
- Water Works               97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.97 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
