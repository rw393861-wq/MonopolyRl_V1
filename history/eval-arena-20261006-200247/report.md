# Monopoly self-play report

Run directory: `logs/eval-arena-20261006-200247`
Games logged: 300
Average rounds per game: 61.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 73 | 24.3% |
| random_1 | 93 | 31.0% |
| heuristic_1 | 134 | 44.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 37% | 27% | 37% | 62 |
| 2 | 30 | 23% | 20% | 57% | 64 |
| 3 | 30 | 23% | 27% | 50% | 62 |
| 4 | 30 | 20% | 27% | 53% | 64 |
| 5 | 30 | 17% | 20% | 63% | 62 |
| 6 | 30 | 27% | 33% | 40% | 58 |
| 7 | 30 | 13% | 40% | 47% | 64 |
| 8 | 30 | 23% | 33% | 43% | 62 |
| 9 | 30 | 27% | 50% | 23% | 60 |
| 10 | 30 | 33% | 33% | 33% | 54 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.6 | 8.2 | 1919 | 0.61 |
| random_1 | 8.5 | 15.8 | 2780 | 1.51 |
| heuristic_1 | 12.3 | 26.2 | 3752 | 2.62 |

## Properties most often held by the winner

- St. Charles Place         99.3%  ############################
- Virginia Avenue           99.3%  ############################
- Illinois Avenue           99.3%  ############################
- States Avenue             99.0%  ############################
- New York Avenue           99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Pennsylvania Railroad     98.7%  ############################
- St. James Place           98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Water Works               98.7%  ############################
- Reading Railroad          98.3%  ############################
- Vermont Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
