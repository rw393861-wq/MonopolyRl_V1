# Monopoly self-play report

Run directory: `logs/eval-arena-20261023-185502`
Games logged: 300
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 70 | 23.3% |
| random_1 | 91 | 30.3% |
| heuristic_1 | 139 | 46.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 27% | 47% | 53 |
| 2 | 30 | 30% | 33% | 37% | 67 |
| 3 | 30 | 20% | 33% | 47% | 62 |
| 4 | 30 | 20% | 30% | 50% | 57 |
| 5 | 30 | 23% | 40% | 37% | 65 |
| 6 | 30 | 27% | 27% | 47% | 68 |
| 7 | 30 | 17% | 27% | 57% | 57 |
| 8 | 30 | 40% | 17% | 43% | 55 |
| 9 | 30 | 17% | 27% | 57% | 62 |
| 10 | 30 | 13% | 43% | 43% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.3 | 8.9 | 1869 | 1.04 |
| random_1 | 8.4 | 15.2 | 2706 | 1.34 |
| heuristic_1 | 12.8 | 25.0 | 3705 | 2.45 |

## Properties most often held by the winner

- New York Avenue           99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Reading Railroad          99.0%  ############################
- Vermont Avenue            99.0%  ############################
- Electric Company          99.0%  ############################
- Indiana Avenue            99.0%  ############################
- St. Charles Place         98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- Water Works               98.7%  ############################
- Connecticut Avenue        98.3%  ############################
- St. James Place           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
