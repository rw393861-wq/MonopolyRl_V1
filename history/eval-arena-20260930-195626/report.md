# Monopoly self-play report

Run directory: `logs/eval-arena-20260930-195626`
Games logged: 300
Average rounds per game: 63.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 99 | 33.0% |
| random_1 | 70 | 23.3% |
| heuristic_1 | 131 | 43.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 33% | 10% | 57% | 56 |
| 2 | 30 | 27% | 23% | 50% | 69 |
| 3 | 30 | 37% | 17% | 47% | 56 |
| 4 | 30 | 30% | 20% | 50% | 60 |
| 5 | 30 | 33% | 17% | 50% | 72 |
| 6 | 30 | 27% | 23% | 50% | 62 |
| 7 | 30 | 37% | 23% | 40% | 63 |
| 8 | 30 | 40% | 27% | 33% | 67 |
| 9 | 30 | 23% | 57% | 20% | 68 |
| 10 | 30 | 43% | 17% | 40% | 65 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 9.0 | 11.7 | 2494 | 0.86 |
| random_1 | 6.4 | 13.8 | 2443 | 1.42 |
| heuristic_1 | 12.0 | 24.5 | 3657 | 2.48 |

## Properties most often held by the winner

- Illinois Avenue           99.7%  ############################
- North Carolina Avenue     99.7%  ############################
- Tennessee Avenue          99.3%  ############################
- New York Avenue           99.3%  ############################
- Pennsylvania Railroad     99.0%  ############################
- St. James Place           99.0%  ############################
- B&O Railroad              99.0%  ############################
- Reading Railroad          98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Indiana Avenue            98.7%  ############################
- St. Charles Place         98.3%  ############################
- Virginia Avenue           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.99 per space
- darkblue   0.96 per space
