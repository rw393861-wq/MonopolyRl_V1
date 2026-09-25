# Monopoly self-play report

Run directory: `logs/eval-arena-20260925-191438`
Games logged: 300
Average rounds per game: 61.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 37 | 12.3% |
| random_1 | 98 | 32.7% |
| heuristic_1 | 165 | 55.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 33% | 57% | 54 |
| 2 | 30 | 13% | 37% | 50% | 63 |
| 3 | 30 | 7% | 30% | 63% | 60 |
| 4 | 30 | 13% | 37% | 50% | 63 |
| 5 | 30 | 13% | 13% | 73% | 68 |
| 6 | 30 | 13% | 30% | 57% | 59 |
| 7 | 30 | 13% | 37% | 50% | 62 |
| 8 | 30 | 10% | 47% | 43% | 61 |
| 9 | 30 | 17% | 37% | 47% | 68 |
| 10 | 30 | 13% | 27% | 60% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.4 | 4.9 | 1178 | 0.63 |
| random_1 | 8.9 | 18.0 | 2971 | 1.73 |
| heuristic_1 | 15.2 | 29.3 | 4216 | 2.85 |

## Properties most often held by the winner

- St. Charles Place         99.7%  ############################
- St. James Place           99.7%  ############################
- Reading Railroad          99.3%  ############################
- Electric Company          99.3%  ############################
- Virginia Avenue           99.3%  ############################
- Boardwalk                 99.3%  ############################
- Tennessee Avenue          99.0%  ############################
- New York Avenue           99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Water Works               99.0%  ############################
- Illinois Avenue           98.7%  ############################
- Atlantic Avenue           98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.99 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
