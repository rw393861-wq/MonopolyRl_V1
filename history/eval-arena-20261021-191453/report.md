# Monopoly self-play report

Run directory: `logs/eval-arena-20261021-191453`
Games logged: 300
Average rounds per game: 63.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 57 | 19.0% |
| random_1 | 91 | 30.3% |
| heuristic_1 | 152 | 50.7% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 17% | 57% | 54 |
| 2 | 30 | 30% | 23% | 47% | 64 |
| 3 | 30 | 10% | 43% | 47% | 71 |
| 4 | 30 | 10% | 40% | 50% | 66 |
| 5 | 30 | 20% | 20% | 60% | 63 |
| 6 | 30 | 23% | 37% | 40% | 61 |
| 7 | 30 | 30% | 23% | 47% | 67 |
| 8 | 30 | 10% | 40% | 50% | 58 |
| 9 | 30 | 10% | 33% | 57% | 71 |
| 10 | 30 | 20% | 27% | 53% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.3 | 6.8 | 1576 | 0.44 |
| random_1 | 8.2 | 17.3 | 3187 | 1.59 |
| heuristic_1 | 14.0 | 28.8 | 4102 | 2.44 |

## Properties most often held by the winner

- Reading Railroad          99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- St. Charles Place         98.7%  ############################
- Virginia Avenue           98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Short Line                98.7%  ############################
- Boardwalk                 98.7%  ############################
- St. James Place           98.3%  ############################
- New York Avenue           98.3%  ############################
- Illinois Avenue           98.3%  ############################
- Oriental Avenue           98.0%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.98 per space
