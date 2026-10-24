# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261024-175539`
Games logged: 300
Average rounds per game: 97.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 126 | 42.0% |
| heuristic_2 | 134 | 44.7% |

## End condition

- round_limit: 49 (16.3%)
- last_standing: 251 (83.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 50% | 33% | 95 |
| 2 | 30 | 20% | 40% | 40% | 115 |
| 3 | 30 | 17% | 33% | 50% | 90 |
| 4 | 30 | 20% | 40% | 40% | 100 |
| 5 | 30 | 17% | 37% | 47% | 98 |
| 6 | 30 | 7% | 57% | 37% | 98 |
| 7 | 30 | 13% | 33% | 53% | 102 |
| 8 | 30 | 7% | 50% | 43% | 99 |
| 9 | 30 | 3% | 40% | 57% | 89 |
| 10 | 30 | 13% | 40% | 47% | 84 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.9 | 2.6 | 1438 | 0.14 |
| heuristic_1 | 11.2 | 17.8 | 4649 | 1.03 |
| heuristic_2 | 12.7 | 18.0 | 4571 | 1.01 |

## Properties most often held by the winner

- Boardwalk                 92.3%  ############################
- Baltic Avenue             92.3%  ############################
- B&O Railroad              92.3%  ############################
- Mediterranean Avenue      92.0%  ############################
- Connecticut Avenue        91.7%  ############################
- Virginia Avenue           91.3%  ############################
- St. James Place           91.3%  ############################
- Pennsylvania Railroad     91.0%  ############################
- Indiana Avenue            91.0%  ############################
- Vermont Avenue            90.3%  ###########################-
- States Avenue             90.3%  ###########################-
- Ventnor Avenue            90.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.90 per space
- lightblue  0.90 per space
- pink       0.90 per space
- util       0.88 per space
- orange     0.89 per space
- red        0.90 per space
- yellow     0.89 per space
- green      0.89 per space
- darkblue   0.90 per space
