# Monopoly self-play report

Run directory: `logs/eval-arena-20261011-192301`
Games logged: 300
Average rounds per game: 64.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 42 | 14.0% |
| random_1 | 104 | 34.7% |
| heuristic_1 | 154 | 51.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 47% | 47% | 66 |
| 2 | 30 | 7% | 37% | 57% | 57 |
| 3 | 30 | 20% | 37% | 43% | 67 |
| 4 | 30 | 10% | 30% | 60% | 65 |
| 5 | 30 | 27% | 30% | 43% | 65 |
| 6 | 30 | 7% | 30% | 63% | 66 |
| 7 | 30 | 13% | 37% | 50% | 74 |
| 8 | 30 | 10% | 33% | 57% | 66 |
| 9 | 30 | 20% | 33% | 47% | 58 |
| 10 | 30 | 20% | 33% | 47% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.8 | 5.0 | 1343 | 0.48 |
| random_1 | 9.5 | 18.7 | 3273 | 1.64 |
| heuristic_1 | 14.2 | 28.0 | 4180 | 2.61 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- Electric Company          99.0%  ############################
- Short Line                99.0%  ############################
- Boardwalk                 99.0%  ############################
- Vermont Avenue            98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- New York Avenue           98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Atlantic Avenue           98.7%  ############################
- Pennsylvania Avenue       98.7%  ############################
- St. Charles Place         98.3%  ############################
- Pennsylvania Railroad     98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.97 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
