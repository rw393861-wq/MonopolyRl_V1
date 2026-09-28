# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260928-210435`
Games logged: 300
Average rounds per game: 101.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 33 | 11.0% |
| heuristic_1 | 126 | 42.0% |
| heuristic_2 | 141 | 47.0% |

## End condition

- round_limit: 61 (20.3%)
- last_standing: 239 (79.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 47% | 43% | 99 |
| 2 | 30 | 7% | 43% | 50% | 105 |
| 3 | 30 | 13% | 50% | 37% | 96 |
| 4 | 30 | 10% | 33% | 57% | 107 |
| 5 | 30 | 7% | 47% | 47% | 113 |
| 6 | 30 | 10% | 43% | 47% | 92 |
| 7 | 30 | 30% | 23% | 47% | 91 |
| 8 | 30 | 10% | 43% | 47% | 99 |
| 9 | 30 | 7% | 43% | 50% | 110 |
| 10 | 30 | 7% | 47% | 47% | 102 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.0 | 3.1 | 1392 | 0.29 |
| heuristic_1 | 11.4 | 15.7 | 4224 | 0.67 |
| heuristic_2 | 12.4 | 16.3 | 4328 | 0.81 |

## Properties most often held by the winner

- Water Works               92.7%  ############################
- Mediterranean Avenue      90.7%  ###########################-
- St. James Place           90.3%  ###########################-
- B&O Railroad              90.0%  ###########################-
- Ventnor Avenue            89.7%  ###########################-
- Virginia Avenue           89.0%  ###########################-
- States Avenue             88.7%  ###########################-
- Reading Railroad          88.3%  ###########################-
- St. Charles Place         88.3%  ###########################-
- Electric Company          88.3%  ###########################-
- Illinois Avenue           88.0%  ###########################-
- Pennsylvania Avenue       88.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.88 per space
- lightblue  0.87 per space
- pink       0.89 per space
- util       0.91 per space
- orange     0.87 per space
- red        0.86 per space
- yellow     0.88 per space
- green      0.87 per space
- darkblue   0.84 per space
