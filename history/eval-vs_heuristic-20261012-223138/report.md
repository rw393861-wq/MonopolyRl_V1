# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261012-223138`
Games logged: 300
Average rounds per game: 99.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 28 | 9.3% |
| heuristic_1 | 137 | 45.7% |
| heuristic_2 | 135 | 45.0% |

## End condition

- round_limit: 51 (17.0%)
- last_standing: 249 (83.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 50% | 40% | 89 |
| 2 | 30 | 3% | 43% | 53% | 102 |
| 3 | 30 | 30% | 47% | 23% | 110 |
| 4 | 30 | 13% | 43% | 43% | 105 |
| 5 | 30 | 13% | 27% | 60% | 92 |
| 6 | 30 | 0% | 37% | 63% | 104 |
| 7 | 30 | 0% | 57% | 43% | 103 |
| 8 | 30 | 7% | 53% | 40% | 98 |
| 9 | 30 | 7% | 57% | 37% | 97 |
| 10 | 30 | 10% | 43% | 47% | 92 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.9 | 2.5 | 1359 | 0.19 |
| heuristic_1 | 12.2 | 19.0 | 4403 | 1.01 |
| heuristic_2 | 12.5 | 17.8 | 4354 | 1.04 |

## Properties most often held by the winner

- Baltic Avenue             91.7%  ############################
- Vermont Avenue            91.0%  ############################
- B&O Railroad              90.7%  ############################
- Water Works               90.3%  ############################
- Illinois Avenue           90.0%  ###########################-
- Reading Railroad          89.7%  ###########################-
- St. James Place           89.7%  ###########################-
- Kentucky Avenue           89.7%  ###########################-
- Marvin Gardens            89.7%  ###########################-
- Pacific Avenue            89.3%  ###########################-
- New York Avenue           89.3%  ###########################-
- Virginia Avenue           89.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.88 per space
- pink       0.88 per space
- util       0.89 per space
- orange     0.89 per space
- red        0.89 per space
- yellow     0.88 per space
- green      0.87 per space
- darkblue   0.88 per space
