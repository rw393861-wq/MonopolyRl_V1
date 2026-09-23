# Monopoly self-play report

Run directory: `logs/eval-arena-20260923-185110`
Games logged: 300
Average rounds per game: 62.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 24 | 8.0% |
| random_1 | 97 | 32.3% |
| heuristic_1 | 179 | 59.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 33% | 63% | 67 |
| 2 | 30 | 13% | 33% | 53% | 65 |
| 3 | 30 | 0% | 40% | 60% | 60 |
| 4 | 30 | 13% | 27% | 60% | 60 |
| 5 | 30 | 13% | 27% | 60% | 61 |
| 6 | 30 | 7% | 30% | 63% | 57 |
| 7 | 30 | 7% | 23% | 70% | 61 |
| 8 | 30 | 13% | 30% | 57% | 65 |
| 9 | 30 | 0% | 37% | 63% | 61 |
| 10 | 30 | 10% | 43% | 47% | 66 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.1 | 3.7 | 926 | 0.58 |
| random_1 | 8.9 | 18.7 | 3224 | 1.60 |
| heuristic_1 | 16.5 | 32.4 | 4751 | 2.60 |

## Properties most often held by the winner

- Pennsylvania Railroad     99.7%  ############################
- Reading Railroad          99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Vermont Avenue            99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- Indiana Avenue            99.0%  ############################
- Oriental Avenue           98.7%  ############################
- St. Charles Place         98.7%  ############################
- Electric Company          98.7%  ############################
- New York Avenue           98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- B&O Railroad              98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.97 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
