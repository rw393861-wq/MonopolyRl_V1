# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260930-195629`
Games logged: 300
Average rounds per game: 106.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 35 | 11.7% |
| heuristic_1 | 126 | 42.0% |
| heuristic_2 | 139 | 46.3% |

## End condition

- round_limit: 66 (22.0%)
- last_standing: 234 (78.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 37% | 47% | 114 |
| 2 | 30 | 3% | 53% | 43% | 108 |
| 3 | 30 | 7% | 53% | 40% | 100 |
| 4 | 30 | 17% | 57% | 27% | 99 |
| 5 | 30 | 13% | 33% | 53% | 108 |
| 6 | 30 | 7% | 43% | 50% | 107 |
| 7 | 30 | 23% | 17% | 60% | 108 |
| 8 | 30 | 13% | 50% | 37% | 102 |
| 9 | 30 | 10% | 40% | 50% | 123 |
| 10 | 30 | 7% | 37% | 57% | 94 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.9 | 2.5 | 1548 | 0.13 |
| heuristic_1 | 11.5 | 16.1 | 4256 | 0.90 |
| heuristic_2 | 12.5 | 16.6 | 4633 | 0.88 |

## Properties most often held by the winner

- Mediterranean Avenue      91.0%  ############################
- Baltic Avenue             90.7%  ############################
- Pennsylvania Avenue       89.0%  ###########################-
- Water Works               88.7%  ###########################-
- Short Line                88.7%  ###########################-
- St. Charles Place         88.7%  ###########################-
- Electric Company          88.3%  ###########################-
- Pennsylvania Railroad     88.0%  ###########################-
- Virginia Avenue           87.0%  ###########################-
- Illinois Avenue           87.0%  ###########################-
- Indiana Avenue            86.3%  ###########################-
- Vermont Avenue            86.0%  ##########################--

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.86 per space
- lightblue  0.85 per space
- pink       0.87 per space
- util       0.89 per space
- orange     0.84 per space
- red        0.86 per space
- yellow     0.84 per space
- green      0.86 per space
- darkblue   0.85 per space
