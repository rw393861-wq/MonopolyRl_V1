# Monopoly self-play report

Run directory: `logs/eval-arena-20261009-200526`
Games logged: 300
Average rounds per game: 61.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 79 | 26.3% |
| random_1 | 86 | 28.7% |
| heuristic_1 | 135 | 45.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 30% | 53% | 64 |
| 2 | 30 | 40% | 17% | 43% | 65 |
| 3 | 30 | 17% | 43% | 40% | 62 |
| 4 | 30 | 30% | 17% | 53% | 61 |
| 5 | 30 | 13% | 33% | 53% | 58 |
| 6 | 30 | 33% | 23% | 43% | 57 |
| 7 | 30 | 27% | 30% | 43% | 67 |
| 8 | 30 | 50% | 23% | 27% | 58 |
| 9 | 30 | 20% | 33% | 47% | 64 |
| 10 | 30 | 17% | 37% | 47% | 63 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 7.2 | 9.1 | 1989 | 0.80 |
| random_1 | 7.9 | 15.5 | 2731 | 1.51 |
| heuristic_1 | 12.4 | 25.1 | 3669 | 2.58 |

## Properties most often held by the winner

- Illinois Avenue           99.7%  ############################
- St. Charles Place         99.3%  ############################
- New York Avenue           99.3%  ############################
- Tennessee Avenue          99.0%  ############################
- B&O Railroad              99.0%  ############################
- Ventnor Avenue            99.0%  ############################
- Reading Railroad          98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Water Works               98.7%  ############################
- Pennsylvania Avenue       98.7%  ############################
- Oriental Avenue           98.3%  ############################
- States Avenue             98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
