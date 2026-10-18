# Monopoly self-play report

Run directory: `logs/eval-arena-20261018-174736`
Games logged: 300
Average rounds per game: 64.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 90 | 30.0% |
| random_1 | 73 | 24.3% |
| heuristic_1 | 137 | 45.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 33% | 40% | 60 |
| 2 | 30 | 30% | 17% | 53% | 66 |
| 3 | 30 | 47% | 23% | 30% | 61 |
| 4 | 30 | 27% | 27% | 47% | 68 |
| 5 | 30 | 27% | 17% | 57% | 70 |
| 6 | 30 | 27% | 27% | 47% | 64 |
| 7 | 30 | 27% | 20% | 53% | 64 |
| 8 | 30 | 30% | 33% | 37% | 59 |
| 9 | 30 | 23% | 13% | 63% | 63 |
| 10 | 30 | 37% | 33% | 30% | 69 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 8.1 | 11.7 | 2298 | 0.77 |
| random_1 | 6.8 | 15.0 | 2569 | 1.42 |
| heuristic_1 | 12.6 | 24.8 | 3845 | 2.26 |

## Properties most often held by the winner

- Ventnor Avenue            99.7%  ############################
- Pennsylvania Railroad     99.3%  ############################
- Kentucky Avenue           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Reading Railroad          98.7%  ############################
- Electric Company          98.7%  ############################
- St. James Place           98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- St. Charles Place         98.3%  ############################
- New York Avenue           98.3%  ############################
- Indiana Avenue            98.3%  ############################
- Illinois Avenue           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.99 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.99 per space
- green      0.98 per space
- darkblue   0.97 per space
