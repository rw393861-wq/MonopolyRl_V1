# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261021-191456`
Games logged: 300
Average rounds per game: 118.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 28 | 9.3% |
| heuristic_1 | 138 | 46.0% |
| heuristic_2 | 134 | 44.7% |

## End condition

- last_standing: 202 (67.3%)
- round_limit: 98 (32.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 43% | 50% | 108 |
| 2 | 30 | 3% | 47% | 50% | 111 |
| 3 | 30 | 10% | 40% | 50% | 119 |
| 4 | 30 | 10% | 57% | 33% | 117 |
| 5 | 30 | 7% | 27% | 67% | 95 |
| 6 | 30 | 17% | 47% | 37% | 132 |
| 7 | 30 | 13% | 57% | 30% | 137 |
| 8 | 30 | 10% | 47% | 43% | 124 |
| 9 | 30 | 7% | 57% | 37% | 117 |
| 10 | 30 | 10% | 40% | 50% | 124 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.7 | 1.7 | 1451 | 0.02 |
| heuristic_1 | 12.2 | 15.1 | 4443 | 0.57 |
| heuristic_2 | 11.8 | 13.9 | 4333 | 0.54 |

## Properties most often held by the winner

- Ventnor Avenue            82.7%  ############################
- Mediterranean Avenue      82.3%  ############################
- St. Charles Place         82.3%  ############################
- States Avenue             82.3%  ############################
- Electric Company          81.7%  ############################
- Water Works               81.7%  ############################
- Reading Railroad          81.0%  ###########################-
- Short Line                81.0%  ###########################-
- Virginia Avenue           80.7%  ###########################-
- Tennessee Avenue          80.3%  ###########################-
- Indiana Avenue            80.3%  ###########################-
- Illinois Avenue           80.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.81 per space
- rail       0.81 per space
- lightblue  0.77 per space
- pink       0.82 per space
- util       0.82 per space
- orange     0.78 per space
- red        0.79 per space
- yellow     0.80 per space
- green      0.78 per space
- darkblue   0.80 per space
