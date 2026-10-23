# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261023-185503`
Games logged: 300
Average rounds per game: 99.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 32 | 10.7% |
| heuristic_1 | 134 | 44.7% |
| heuristic_2 | 134 | 44.7% |

## End condition

- round_limit: 59 (19.7%)
- last_standing: 241 (80.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 50% | 43% | 105 |
| 2 | 30 | 10% | 57% | 33% | 100 |
| 3 | 30 | 20% | 40% | 40% | 92 |
| 4 | 30 | 17% | 53% | 30% | 102 |
| 5 | 30 | 13% | 27% | 60% | 96 |
| 6 | 30 | 10% | 47% | 43% | 108 |
| 7 | 30 | 10% | 37% | 53% | 94 |
| 8 | 30 | 0% | 47% | 53% | 102 |
| 9 | 30 | 10% | 43% | 47% | 100 |
| 10 | 30 | 10% | 47% | 43% | 92 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.9 | 2.8 | 1387 | 0.38 |
| heuristic_1 | 11.9 | 17.9 | 4331 | 1.06 |
| heuristic_2 | 11.9 | 17.6 | 4275 | 1.09 |

## Properties most often held by the winner

- B&O Railroad              91.7%  ############################
- Mediterranean Avenue      91.7%  ############################
- Water Works               90.7%  ############################
- Ventnor Avenue            89.3%  ###########################-
- Short Line                89.3%  ###########################-
- Reading Railroad          89.0%  ###########################-
- Virginia Avenue           89.0%  ###########################-
- Baltic Avenue             88.7%  ###########################-
- Boardwalk                 88.7%  ###########################-
- New York Avenue           88.3%  ###########################-
- Illinois Avenue           88.3%  ###########################-
- Tennessee Avenue          87.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.88 per space
- orange     0.88 per space
- red        0.86 per space
- yellow     0.87 per space
- green      0.87 per space
- darkblue   0.86 per space
