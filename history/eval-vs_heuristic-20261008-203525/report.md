# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261008-203525`
Games logged: 300
Average rounds per game: 99.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 36 | 12.0% |
| heuristic_1 | 125 | 41.7% |
| heuristic_2 | 139 | 46.3% |

## End condition

- last_standing: 238 (79.3%)
- round_limit: 62 (20.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 33% | 60% | 92 |
| 2 | 30 | 20% | 30% | 50% | 108 |
| 3 | 30 | 10% | 43% | 47% | 111 |
| 4 | 30 | 7% | 50% | 43% | 96 |
| 5 | 30 | 17% | 33% | 50% | 103 |
| 6 | 30 | 13% | 43% | 43% | 108 |
| 7 | 30 | 10% | 63% | 27% | 97 |
| 8 | 30 | 3% | 47% | 50% | 94 |
| 9 | 30 | 20% | 30% | 50% | 84 |
| 10 | 30 | 13% | 43% | 43% | 99 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.5 | 4.0 | 1613 | 0.27 |
| heuristic_1 | 11.2 | 16.3 | 4222 | 1.01 |
| heuristic_2 | 12.9 | 18.5 | 4431 | 1.01 |

## Properties most often held by the winner

- Vermont Avenue            89.7%  ############################
- Pennsylvania Railroad     89.0%  ############################
- Mediterranean Avenue      88.7%  ############################
- Baltic Avenue             88.3%  ############################
- Connecticut Avenue        88.3%  ############################
- Atlantic Avenue           88.0%  ###########################-
- Indiana Avenue            87.7%  ###########################-
- B&O Railroad              87.3%  ###########################-
- St. James Place           86.7%  ###########################-
- Reading Railroad          86.3%  ###########################-
- St. Charles Place         86.3%  ###########################-
- Short Line                86.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.87 per space
- lightblue  0.88 per space
- pink       0.84 per space
- util       0.85 per space
- orange     0.85 per space
- red        0.86 per space
- yellow     0.86 per space
- green      0.85 per space
- darkblue   0.83 per space
