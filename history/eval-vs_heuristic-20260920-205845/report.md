# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260920-205845`
Games logged: 300
Average rounds per game: 95.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 64 | 21.3% |
| heuristic_1 | 110 | 36.7% |
| heuristic_2 | 126 | 42.0% |

## End condition

- round_limit: 49 (16.3%)
- last_standing: 251 (83.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 33% | 57% | 95 |
| 2 | 30 | 10% | 63% | 27% | 103 |
| 3 | 30 | 23% | 40% | 37% | 97 |
| 4 | 30 | 23% | 37% | 40% | 100 |
| 5 | 30 | 33% | 17% | 50% | 94 |
| 6 | 30 | 20% | 37% | 43% | 106 |
| 7 | 30 | 33% | 37% | 30% | 94 |
| 8 | 30 | 20% | 33% | 47% | 85 |
| 9 | 30 | 13% | 37% | 50% | 91 |
| 10 | 30 | 27% | 33% | 40% | 92 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.9 | 7.5 | 2469 | 0.59 |
| heuristic_1 | 10.1 | 13.2 | 3372 | 0.79 |
| heuristic_2 | 11.7 | 16.0 | 3826 | 0.89 |

## Properties most often held by the winner

- Water Works               90.3%  ############################
- Short Line                90.3%  ############################
- Electric Company          90.0%  ############################
- Marvin Gardens            89.7%  ############################
- Virginia Avenue           89.7%  ############################
- Boardwalk                 89.7%  ############################
- Reading Railroad          89.3%  ############################
- Indiana Avenue            89.3%  ############################
- B&O Railroad              89.3%  ############################
- Kentucky Avenue           89.3%  ############################
- New York Avenue           89.0%  ############################
- Pennsylvania Avenue       89.0%  ############################

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.89 per space
- lightblue  0.88 per space
- pink       0.88 per space
- util       0.90 per space
- orange     0.89 per space
- red        0.89 per space
- yellow     0.88 per space
- green      0.88 per space
- darkblue   0.89 per space
