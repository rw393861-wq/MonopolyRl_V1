# Monopoly self-play report

Run directory: `logs/eval-arena-20261002-195352`
Games logged: 300
Average rounds per game: 61.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 62 | 20.7% |
| random_1 | 89 | 29.7% |
| heuristic_1 | 149 | 49.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 23% | 60% | 60 |
| 2 | 30 | 10% | 43% | 47% | 59 |
| 3 | 30 | 40% | 27% | 33% | 65 |
| 4 | 30 | 17% | 37% | 47% | 63 |
| 5 | 30 | 17% | 20% | 63% | 63 |
| 6 | 30 | 20% | 30% | 50% | 60 |
| 7 | 30 | 17% | 30% | 53% | 58 |
| 8 | 30 | 13% | 27% | 60% | 65 |
| 9 | 30 | 30% | 27% | 43% | 70 |
| 10 | 30 | 27% | 33% | 40% | 56 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.7 | 9.2 | 1819 | 0.75 |
| random_1 | 8.2 | 15.2 | 2754 | 1.48 |
| heuristic_1 | 13.6 | 25.7 | 3875 | 2.27 |

## Properties most often held by the winner

- Vermont Avenue            99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- B&O Railroad              99.0%  ############################
- St. Charles Place         98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Atlantic Avenue           98.7%  ############################
- Boardwalk                 98.7%  ############################
- Reading Railroad          98.3%  ############################
- Electric Company          98.3%  ############################
- Virginia Avenue           98.3%  ############################
- New York Avenue           98.3%  ############################
- Ventnor Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
