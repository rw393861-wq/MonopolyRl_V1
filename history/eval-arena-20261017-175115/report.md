# Monopoly self-play report

Run directory: `logs/eval-arena-20261017-175115`
Games logged: 300
Average rounds per game: 58.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 106 | 35.3% |
| random_1 | 71 | 23.7% |
| heuristic_1 | 123 | 41.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 43% | 23% | 33% | 60 |
| 2 | 30 | 47% | 17% | 37% | 62 |
| 3 | 30 | 33% | 23% | 43% | 55 |
| 4 | 30 | 33% | 3% | 63% | 61 |
| 5 | 30 | 37% | 23% | 40% | 58 |
| 6 | 30 | 33% | 40% | 27% | 58 |
| 7 | 30 | 30% | 27% | 43% | 56 |
| 8 | 30 | 23% | 30% | 47% | 64 |
| 9 | 30 | 37% | 23% | 40% | 59 |
| 10 | 30 | 37% | 27% | 37% | 55 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 9.5 | 14.2 | 2595 | 0.96 |
| random_1 | 6.5 | 13.1 | 2277 | 1.35 |
| heuristic_1 | 11.2 | 22.7 | 3312 | 2.35 |

## Properties most often held by the winner

- Tennessee Avenue          98.7%  ############################
- Illinois Avenue           98.7%  ############################
- B&O Railroad              98.7%  ############################
- Reading Railroad          98.3%  ############################
- St. James Place           98.3%  ############################
- Indiana Avenue            98.3%  ############################
- Atlantic Avenue           98.3%  ############################
- Boardwalk                 98.3%  ############################
- Connecticut Avenue        97.7%  ############################
- Pennsylvania Railroad     97.7%  ############################
- New York Avenue           97.7%  ############################
- Oriental Avenue           97.3%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.96 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
