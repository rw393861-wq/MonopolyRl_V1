# Monopoly self-play report

Run directory: `logs/eval-arena-20261012-223135`
Games logged: 300
Average rounds per game: 60.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 64 | 21.3% |
| random_1 | 86 | 28.7% |
| heuristic_1 | 150 | 50.0% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 27% | 60% | 60 |
| 2 | 30 | 13% | 13% | 73% | 61 |
| 3 | 30 | 13% | 27% | 60% | 60 |
| 4 | 30 | 10% | 37% | 53% | 61 |
| 5 | 30 | 17% | 47% | 37% | 60 |
| 6 | 30 | 37% | 23% | 40% | 56 |
| 7 | 30 | 30% | 37% | 33% | 70 |
| 8 | 30 | 20% | 27% | 53% | 59 |
| 9 | 30 | 33% | 20% | 47% | 58 |
| 10 | 30 | 27% | 30% | 43% | 64 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.8 | 8.9 | 1877 | 0.92 |
| random_1 | 7.8 | 14.6 | 2446 | 1.37 |
| heuristic_1 | 13.8 | 26.4 | 3764 | 2.70 |

## Properties most often held by the winner

- Reading Railroad          99.0%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Vermont Avenue            98.3%  ############################
- St. James Place           98.3%  ############################
- Oriental Avenue           98.0%  ############################
- Connecticut Avenue        98.0%  ############################
- St. Charles Place         98.0%  ############################
- Electric Company          98.0%  ############################
- Tennessee Avenue          98.0%  ############################
- Atlantic Avenue           98.0%  ############################
- Virginia Avenue           97.7%  ############################
- New York Avenue           97.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.97 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.97 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.96 per space
