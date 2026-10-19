# Monopoly self-play report

Run directory: `logs/eval-arena-20261019-202602`
Games logged: 300
Average rounds per game: 61.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 89 | 29.7% |
| random_1 | 77 | 25.7% |
| heuristic_1 | 134 | 44.7% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 33% | 17% | 50% | 59 |
| 2 | 30 | 30% | 30% | 40% | 63 |
| 3 | 30 | 17% | 40% | 43% | 58 |
| 4 | 30 | 33% | 30% | 37% | 57 |
| 5 | 30 | 27% | 20% | 53% | 59 |
| 6 | 30 | 27% | 20% | 53% | 64 |
| 7 | 30 | 40% | 17% | 43% | 62 |
| 8 | 30 | 33% | 30% | 37% | 68 |
| 9 | 30 | 23% | 30% | 47% | 65 |
| 10 | 30 | 33% | 23% | 43% | 57 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 8.1 | 13.2 | 2500 | 1.02 |
| random_1 | 7.1 | 13.9 | 2374 | 1.34 |
| heuristic_1 | 12.2 | 23.9 | 3644 | 2.58 |

## Properties most often held by the winner

- St. James Place          100.0%  ############################
- St. Charles Place         99.3%  ############################
- Illinois Avenue           99.0%  ############################
- Virginia Avenue           98.7%  ############################
- B&O Railroad              98.7%  ############################
- Oriental Avenue           98.3%  ############################
- Connecticut Avenue        98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Ventnor Avenue            98.3%  ############################
- Reading Railroad          98.0%  ###########################-
- States Avenue             98.0%  ###########################-
- Indiana Avenue            98.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
