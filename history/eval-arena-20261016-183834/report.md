# Monopoly self-play report

Run directory: `logs/eval-arena-20261016-183834`
Games logged: 300
Average rounds per game: 59.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 64 | 21.3% |
| random_1 | 75 | 25.0% |
| heuristic_1 | 161 | 53.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 30% | 53% | 60 |
| 2 | 30 | 17% | 20% | 63% | 55 |
| 3 | 30 | 13% | 27% | 60% | 62 |
| 4 | 30 | 30% | 20% | 50% | 57 |
| 5 | 30 | 33% | 23% | 43% | 64 |
| 6 | 30 | 20% | 27% | 53% | 62 |
| 7 | 30 | 27% | 23% | 50% | 56 |
| 8 | 30 | 23% | 23% | 53% | 60 |
| 9 | 30 | 20% | 33% | 47% | 63 |
| 10 | 30 | 13% | 23% | 63% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.8 | 8.4 | 1643 | 0.99 |
| random_1 | 6.9 | 14.7 | 2496 | 1.44 |
| heuristic_1 | 14.8 | 25.7 | 3917 | 2.42 |

## Properties most often held by the winner

- St. James Place          100.0%  ############################
- B&O Railroad             100.0%  ############################
- St. Charles Place         99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- New York Avenue           99.3%  ############################
- Oriental Avenue           99.0%  ############################
- Pennsylvania Railroad     99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Indiana Avenue            99.0%  ############################
- Illinois Avenue           99.0%  ############################
- Ventnor Avenue            99.0%  ############################
- Reading Railroad          98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     1.00 per space
- red        0.99 per space
- yellow     0.99 per space
- green      0.97 per space
- darkblue   0.98 per space
