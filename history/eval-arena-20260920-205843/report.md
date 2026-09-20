# Monopoly self-play report

Run directory: `logs/eval-arena-20260920-205843`
Games logged: 300
Average rounds per game: 62.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 73 | 24.3% |
| random_1 | 89 | 29.7% |
| heuristic_1 | 138 | 46.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 23% | 53% | 59 |
| 2 | 30 | 27% | 33% | 40% | 64 |
| 3 | 30 | 30% | 43% | 27% | 60 |
| 4 | 30 | 30% | 17% | 53% | 61 |
| 5 | 30 | 13% | 40% | 47% | 63 |
| 6 | 30 | 23% | 37% | 40% | 66 |
| 7 | 30 | 43% | 23% | 33% | 61 |
| 8 | 30 | 20% | 17% | 63% | 62 |
| 9 | 30 | 23% | 23% | 53% | 62 |
| 10 | 30 | 10% | 40% | 50% | 68 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.7 | 10.5 | 2044 | 0.98 |
| random_1 | 8.2 | 14.8 | 2530 | 1.36 |
| heuristic_1 | 12.5 | 22.9 | 3580 | 2.22 |

## Properties most often held by the winner

- Illinois Avenue           99.3%  ############################
- St. Charles Place         98.7%  ############################
- Electric Company          98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################
- St. James Place           98.7%  ############################
- Boardwalk                 98.7%  ############################
- Reading Railroad          98.3%  ############################
- Virginia Avenue           98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Atlantic Avenue           98.3%  ############################
- Water Works               98.3%  ############################
- Vermont Avenue            98.0%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.96 per space
- darkblue   0.97 per space
