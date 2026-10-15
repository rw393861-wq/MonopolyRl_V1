# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261015-185855`
Games logged: 300
Average rounds per game: 101.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 51 | 17.0% |
| heuristic_1 | 118 | 39.3% |
| heuristic_2 | 131 | 43.7% |

## End condition

- round_limit: 62 (20.7%)
- last_standing: 238 (79.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 43% | 47% | 94 |
| 2 | 30 | 17% | 33% | 50% | 87 |
| 3 | 30 | 17% | 53% | 30% | 107 |
| 4 | 30 | 23% | 27% | 50% | 113 |
| 5 | 30 | 17% | 53% | 30% | 97 |
| 6 | 30 | 23% | 40% | 37% | 102 |
| 7 | 30 | 13% | 40% | 47% | 112 |
| 8 | 30 | 7% | 43% | 50% | 107 |
| 9 | 30 | 13% | 37% | 50% | 100 |
| 10 | 30 | 30% | 23% | 47% | 99 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.8 | 3.7 | 1877 | 0.06 |
| heuristic_1 | 10.8 | 15.7 | 3995 | 0.75 |
| heuristic_2 | 12.1 | 16.3 | 4114 | 0.82 |

## Properties most often held by the winner

- Pennsylvania Railroad     89.7%  ############################
- B&O Railroad              89.3%  ############################
- Reading Railroad          89.0%  ############################
- Marvin Gardens            88.7%  ############################
- Baltic Avenue             88.7%  ############################
- St. Charles Place         88.3%  ############################
- Short Line                87.7%  ###########################-
- Vermont Avenue            87.7%  ###########################-
- Boardwalk                 87.3%  ###########################-
- Ventnor Avenue            87.0%  ###########################-
- North Carolina Avenue     86.7%  ###########################-
- Water Works               86.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.89 per space
- lightblue  0.87 per space
- pink       0.86 per space
- util       0.86 per space
- orange     0.86 per space
- red        0.86 per space
- yellow     0.87 per space
- green      0.85 per space
- darkblue   0.86 per space
