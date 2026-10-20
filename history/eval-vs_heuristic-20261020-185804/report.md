# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261020-185804`
Games logged: 300
Average rounds per game: 105.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 26 | 8.7% |
| heuristic_1 | 146 | 48.7% |
| heuristic_2 | 128 | 42.7% |

## End condition

- last_standing: 232 (77.3%)
- round_limit: 68 (22.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 0% | 67% | 33% | 102 |
| 2 | 30 | 13% | 43% | 43% | 108 |
| 3 | 30 | 10% | 33% | 57% | 97 |
| 4 | 30 | 13% | 40% | 47% | 120 |
| 5 | 30 | 3% | 43% | 53% | 98 |
| 6 | 30 | 10% | 50% | 40% | 118 |
| 7 | 30 | 7% | 60% | 33% | 108 |
| 8 | 30 | 10% | 47% | 43% | 92 |
| 9 | 30 | 7% | 57% | 37% | 111 |
| 10 | 30 | 13% | 47% | 40% | 105 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.2 | 2.3 | 1463 | 0.24 |
| heuristic_1 | 13.0 | 19.1 | 4758 | 0.91 |
| heuristic_2 | 11.6 | 15.7 | 4281 | 0.88 |

## Properties most often held by the winner

- Baltic Avenue             91.0%  ############################
- Electric Company          89.3%  ###########################-
- Reading Railroad          89.0%  ###########################-
- Mediterranean Avenue      88.0%  ###########################-
- B&O Railroad              88.0%  ###########################-
- Pacific Avenue            87.7%  ###########################-
- Short Line                87.7%  ###########################-
- Oriental Avenue           87.0%  ###########################-
- Pennsylvania Railroad     87.0%  ###########################-
- Water Works               87.0%  ###########################-
- Vermont Avenue            86.3%  ###########################-
- Connecticut Avenue        86.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.88 per space
- lightblue  0.87 per space
- pink       0.84 per space
- util       0.88 per space
- orange     0.85 per space
- red        0.85 per space
- yellow     0.84 per space
- green      0.85 per space
- darkblue   0.84 per space
