# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261009-200529`
Games logged: 300
Average rounds per game: 110.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 37 | 12.3% |
| heuristic_1 | 123 | 41.0% |
| heuristic_2 | 140 | 46.7% |

## End condition

- last_standing: 217 (72.3%)
- round_limit: 83 (27.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 43% | 43% | 91 |
| 2 | 30 | 10% | 30% | 60% | 100 |
| 3 | 30 | 7% | 53% | 40% | 123 |
| 4 | 30 | 17% | 33% | 50% | 121 |
| 5 | 30 | 17% | 37% | 47% | 102 |
| 6 | 30 | 20% | 33% | 47% | 126 |
| 7 | 30 | 10% | 47% | 43% | 108 |
| 8 | 30 | 3% | 43% | 53% | 94 |
| 9 | 30 | 13% | 40% | 47% | 117 |
| 10 | 30 | 13% | 50% | 37% | 119 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.1 | 3.4 | 1619 | 0.28 |
| heuristic_1 | 11.4 | 15.3 | 4167 | 0.83 |
| heuristic_2 | 12.2 | 16.8 | 4417 | 0.90 |

## Properties most often held by the winner

- Reading Railroad          88.7%  ############################
- Water Works               86.3%  ###########################-
- Illinois Avenue           86.0%  ###########################-
- Pennsylvania Railroad     85.7%  ###########################-
- B&O Railroad              85.0%  ###########################-
- New York Avenue           84.7%  ###########################-
- Baltic Avenue             84.3%  ###########################-
- Connecticut Avenue        84.3%  ###########################-
- North Carolina Avenue     84.0%  ###########################-
- Park Place                84.0%  ###########################-
- Electric Company          83.7%  ##########################--
- Mediterranean Avenue      82.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.83 per space
- rail       0.85 per space
- lightblue  0.82 per space
- pink       0.82 per space
- util       0.85 per space
- orange     0.83 per space
- red        0.83 per space
- yellow     0.80 per space
- green      0.81 per space
- darkblue   0.82 per space
