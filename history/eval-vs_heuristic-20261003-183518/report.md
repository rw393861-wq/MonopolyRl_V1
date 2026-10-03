# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261003-183518`
Games logged: 300
Average rounds per game: 104.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 38 | 12.7% |
| heuristic_1 | 127 | 42.3% |
| heuristic_2 | 135 | 45.0% |

## End condition

- last_standing: 232 (77.3%)
- round_limit: 68 (22.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 30% | 63% | 110 |
| 2 | 30 | 23% | 23% | 53% | 115 |
| 3 | 30 | 7% | 60% | 33% | 114 |
| 4 | 30 | 7% | 50% | 43% | 107 |
| 5 | 30 | 7% | 30% | 63% | 97 |
| 6 | 30 | 20% | 23% | 57% | 128 |
| 7 | 30 | 10% | 60% | 30% | 90 |
| 8 | 30 | 20% | 47% | 33% | 92 |
| 9 | 30 | 10% | 60% | 30% | 105 |
| 10 | 30 | 17% | 40% | 43% | 87 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.0 | 4.6 | 1804 | 0.20 |
| heuristic_1 | 12.1 | 18.2 | 4557 | 0.90 |
| heuristic_2 | 11.6 | 16.7 | 4316 | 0.93 |

## Properties most often held by the winner

- Baltic Avenue             89.7%  ############################
- Vermont Avenue            89.0%  ############################
- Water Works               89.0%  ############################
- Reading Railroad          88.7%  ############################
- Electric Company          88.7%  ############################
- Mediterranean Avenue      88.3%  ############################
- Tennessee Avenue          87.7%  ###########################-
- Pacific Avenue            87.7%  ###########################-
- Oriental Avenue           87.3%  ###########################-
- Indiana Avenue            87.0%  ###########################-
- Marvin Gardens            86.7%  ###########################-
- St. James Place           86.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.86 per space
- lightblue  0.87 per space
- pink       0.85 per space
- util       0.89 per space
- orange     0.87 per space
- red        0.85 per space
- yellow     0.85 per space
- green      0.85 per space
- darkblue   0.85 per space
