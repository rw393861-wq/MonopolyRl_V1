# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261007-202736`
Games logged: 300
Average rounds per game: 99.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 31 | 10.3% |
| heuristic_1 | 124 | 41.3% |
| heuristic_2 | 145 | 48.3% |

## End condition

- last_standing: 239 (79.7%)
- round_limit: 61 (20.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 53% | 40% | 81 |
| 2 | 30 | 3% | 43% | 53% | 114 |
| 3 | 30 | 10% | 33% | 57% | 108 |
| 4 | 30 | 7% | 33% | 60% | 122 |
| 5 | 30 | 7% | 43% | 50% | 99 |
| 6 | 30 | 17% | 50% | 33% | 102 |
| 7 | 30 | 7% | 40% | 53% | 91 |
| 8 | 30 | 20% | 33% | 47% | 92 |
| 9 | 30 | 20% | 43% | 37% | 98 |
| 10 | 30 | 7% | 40% | 53% | 87 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.5 | 3.1 | 1444 | 0.13 |
| heuristic_1 | 11.6 | 15.8 | 4248 | 1.00 |
| heuristic_2 | 12.6 | 18.5 | 4587 | 1.14 |

## Properties most often held by the winner

- Mediterranean Avenue      91.3%  ############################
- Baltic Avenue             90.7%  ############################
- Short Line                90.3%  ############################
- Water Works               89.7%  ###########################-
- Tennessee Avenue          88.7%  ###########################-
- St. James Place           88.3%  ###########################-
- Reading Railroad          88.0%  ###########################-
- Pacific Avenue            88.0%  ###########################-
- Park Place                87.7%  ###########################-
- B&O Railroad              87.3%  ###########################-
- Boardwalk                 87.3%  ###########################-
- Connecticut Avenue        87.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.88 per space
- lightblue  0.87 per space
- pink       0.86 per space
- util       0.88 per space
- orange     0.88 per space
- red        0.86 per space
- yellow     0.85 per space
- green      0.87 per space
- darkblue   0.88 per space
