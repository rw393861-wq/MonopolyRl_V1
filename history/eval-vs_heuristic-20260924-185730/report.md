# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260924-185730`
Games logged: 300
Average rounds per game: 106.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 21 | 7.0% |
| heuristic_1 | 129 | 43.0% |
| heuristic_2 | 150 | 50.0% |

## End condition

- last_standing: 229 (76.3%)
- round_limit: 71 (23.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 40% | 57% | 93 |
| 2 | 30 | 10% | 47% | 43% | 112 |
| 3 | 30 | 3% | 53% | 43% | 94 |
| 4 | 30 | 10% | 33% | 57% | 86 |
| 5 | 30 | 10% | 30% | 60% | 106 |
| 6 | 30 | 7% | 47% | 47% | 117 |
| 7 | 30 | 3% | 50% | 47% | 107 |
| 8 | 30 | 7% | 50% | 43% | 113 |
| 9 | 30 | 10% | 30% | 60% | 110 |
| 10 | 30 | 7% | 50% | 43% | 123 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.8 | 1.4 | 1332 | 0.10 |
| heuristic_1 | 11.8 | 16.6 | 4260 | 0.85 |
| heuristic_2 | 13.2 | 18.0 | 4687 | 0.83 |

## Properties most often held by the winner

- Mediterranean Avenue      90.0%  ############################
- Baltic Avenue             88.7%  ############################
- Tennessee Avenue          88.3%  ###########################-
- Reading Railroad          86.7%  ###########################-
- Electric Company          86.7%  ###########################-
- Indiana Avenue            86.7%  ###########################-
- B&O Railroad              86.7%  ###########################-
- New York Avenue           86.3%  ###########################-
- Virginia Avenue           86.0%  ###########################-
- Short Line                86.0%  ###########################-
- Water Works               85.7%  ###########################-
- Kentucky Avenue           85.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.86 per space
- lightblue  0.84 per space
- pink       0.85 per space
- util       0.86 per space
- orange     0.86 per space
- red        0.85 per space
- yellow     0.84 per space
- green      0.84 per space
- darkblue   0.83 per space
