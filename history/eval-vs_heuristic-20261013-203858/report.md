# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261013-203858`
Games logged: 300
Average rounds per game: 102.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 26 | 8.7% |
| heuristic_1 | 124 | 41.3% |
| heuristic_2 | 150 | 50.0% |

## End condition

- round_limit: 61 (20.3%)
- last_standing: 239 (79.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 53% | 40% | 114 |
| 2 | 30 | 7% | 40% | 53% | 103 |
| 3 | 30 | 7% | 53% | 40% | 114 |
| 4 | 30 | 7% | 43% | 50% | 89 |
| 5 | 30 | 7% | 30% | 63% | 116 |
| 6 | 30 | 13% | 40% | 47% | 117 |
| 7 | 30 | 7% | 37% | 57% | 87 |
| 8 | 30 | 10% | 43% | 47% | 95 |
| 9 | 30 | 13% | 43% | 43% | 89 |
| 10 | 30 | 10% | 30% | 60% | 100 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.7 | 1.6 | 1271 | 0.00 |
| heuristic_1 | 10.9 | 16.2 | 4655 | 1.02 |
| heuristic_2 | 14.1 | 19.1 | 4943 | 1.22 |

## Properties most often held by the winner

- Mediterranean Avenue      91.3%  ############################
- Baltic Avenue             89.3%  ###########################-
- Short Line                89.3%  ###########################-
- Electric Company          88.7%  ###########################-
- Tennessee Avenue          88.7%  ###########################-
- Water Works               88.7%  ###########################-
- States Avenue             88.0%  ###########################-
- Oriental Avenue           88.0%  ###########################-
- Pacific Avenue            87.7%  ###########################-
- Reading Railroad          87.3%  ###########################-
- Kentucky Avenue           87.3%  ###########################-
- B&O Railroad              87.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.88 per space
- lightblue  0.87 per space
- pink       0.87 per space
- util       0.89 per space
- orange     0.86 per space
- red        0.86 per space
- yellow     0.86 per space
- green      0.87 per space
- darkblue   0.85 per space
