# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260929-195452`
Games logged: 300
Average rounds per game: 106.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 34 | 11.3% |
| heuristic_1 | 133 | 44.3% |
| heuristic_2 | 133 | 44.3% |

## End condition

- last_standing: 234 (78.0%)
- round_limit: 66 (22.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 33% | 47% | 102 |
| 2 | 30 | 10% | 53% | 37% | 117 |
| 3 | 30 | 10% | 30% | 60% | 105 |
| 4 | 30 | 17% | 40% | 43% | 115 |
| 5 | 30 | 7% | 47% | 47% | 93 |
| 6 | 30 | 10% | 50% | 40% | 99 |
| 7 | 30 | 13% | 50% | 37% | 99 |
| 8 | 30 | 3% | 53% | 43% | 130 |
| 9 | 30 | 10% | 47% | 43% | 114 |
| 10 | 30 | 13% | 40% | 47% | 87 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.0 | 3.1 | 1562 | 0.05 |
| heuristic_1 | 11.6 | 17.2 | 4454 | 0.97 |
| heuristic_2 | 12.2 | 16.7 | 4378 | 0.96 |

## Properties most often held by the winner

- B&O Railroad              90.7%  ############################
- Mediterranean Avenue      90.3%  ############################
- Pennsylvania Railroad     88.7%  ###########################-
- Indiana Avenue            88.7%  ###########################-
- St. Charles Place         88.3%  ###########################-
- Oriental Avenue           88.0%  ###########################-
- Boardwalk                 88.0%  ###########################-
- Reading Railroad          87.3%  ###########################-
- Electric Company          87.3%  ###########################-
- Baltic Avenue             86.7%  ###########################-
- Tennessee Avenue          86.7%  ###########################-
- Illinois Avenue           86.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.88 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.87 per space
- orange     0.86 per space
- red        0.87 per space
- yellow     0.85 per space
- green      0.85 per space
- darkblue   0.87 per space
