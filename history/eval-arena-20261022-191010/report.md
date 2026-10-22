# Monopoly self-play report

Run directory: `logs/eval-arena-20261022-191010`
Games logged: 300
Average rounds per game: 64.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 95 | 31.7% |
| random_1 | 69 | 23.0% |
| heuristic_1 | 136 | 45.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 40% | 27% | 33% | 58 |
| 2 | 30 | 30% | 30% | 40% | 71 |
| 3 | 30 | 33% | 23% | 43% | 63 |
| 4 | 30 | 27% | 27% | 47% | 69 |
| 5 | 30 | 30% | 27% | 43% | 61 |
| 6 | 30 | 40% | 13% | 47% | 68 |
| 7 | 30 | 27% | 30% | 43% | 62 |
| 8 | 30 | 30% | 10% | 60% | 61 |
| 9 | 30 | 40% | 13% | 47% | 64 |
| 10 | 30 | 20% | 30% | 50% | 66 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 8.6 | 12.0 | 2470 | 1.00 |
| random_1 | 6.3 | 13.2 | 2312 | 1.38 |
| heuristic_1 | 12.6 | 25.4 | 3875 | 2.57 |

## Properties most often held by the winner

- St. Charles Place         99.3%  ############################
- States Avenue             99.3%  ############################
- Kentucky Avenue           99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Boardwalk                 99.3%  ############################
- Oriental Avenue           99.0%  ############################
- Vermont Avenue            99.0%  ############################
- Electric Company          99.0%  ############################
- New York Avenue           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Pacific Avenue            99.0%  ############################
- Pennsylvania Avenue       99.0%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.99 per space
- orange     0.98 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.97 per space
