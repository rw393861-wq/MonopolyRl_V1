# Monopoly self-play report

Run directory: `logs/eval-arena-20261013-203855`
Games logged: 300
Average rounds per game: 63.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 58 | 19.3% |
| random_1 | 95 | 31.7% |
| heuristic_1 | 147 | 49.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 30% | 23% | 47% | 60 |
| 2 | 30 | 10% | 37% | 53% | 66 |
| 3 | 30 | 23% | 33% | 43% | 57 |
| 4 | 30 | 20% | 33% | 47% | 71 |
| 5 | 30 | 23% | 33% | 43% | 59 |
| 6 | 30 | 27% | 33% | 40% | 69 |
| 7 | 30 | 10% | 33% | 57% | 62 |
| 8 | 30 | 17% | 30% | 53% | 63 |
| 9 | 30 | 10% | 33% | 57% | 62 |
| 10 | 30 | 23% | 27% | 50% | 65 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.2 | 5.9 | 1668 | 0.55 |
| random_1 | 8.7 | 17.3 | 2952 | 1.63 |
| heuristic_1 | 13.6 | 27.4 | 3939 | 2.73 |

## Properties most often held by the winner

- Kentucky Avenue           99.3%  ############################
- Indiana Avenue            99.3%  ############################
- Vermont Avenue            99.0%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Reading Railroad          98.3%  ############################
- Illinois Avenue           98.3%  ############################
- St. Charles Place         98.3%  ############################
- Electric Company          98.0%  ############################
- B&O Railroad              98.0%  ############################
- Ventnor Avenue            98.0%  ############################
- Oriental Avenue           97.7%  ############################
- North Carolina Avenue     97.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.97 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
