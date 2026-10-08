# Monopoly self-play report

Run directory: `logs/eval-arena-20261008-203522`
Games logged: 300
Average rounds per game: 64.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 73 | 24.3% |
| random_1 | 106 | 35.3% |
| heuristic_1 | 121 | 40.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 37% | 37% | 57 |
| 2 | 30 | 23% | 33% | 43% | 66 |
| 3 | 30 | 20% | 37% | 43% | 64 |
| 4 | 30 | 27% | 37% | 37% | 65 |
| 5 | 30 | 37% | 33% | 30% | 71 |
| 6 | 30 | 23% | 37% | 40% | 61 |
| 7 | 30 | 23% | 47% | 30% | 63 |
| 8 | 30 | 30% | 33% | 37% | 66 |
| 9 | 30 | 20% | 30% | 50% | 58 |
| 10 | 30 | 13% | 30% | 57% | 74 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.6 | 9.7 | 2066 | 0.81 |
| random_1 | 9.8 | 19.1 | 3263 | 1.48 |
| heuristic_1 | 11.1 | 25.6 | 3677 | 2.55 |

## Properties most often held by the winner

- Reading Railroad          99.7%  ############################
- Vermont Avenue            99.7%  ############################
- Pennsylvania Railroad     99.3%  ############################
- St. James Place           99.3%  ############################
- Tennessee Avenue          99.3%  ############################
- Kentucky Avenue           99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Electric Company          99.0%  ############################
- North Carolina Avenue     99.0%  ############################
- Oriental Avenue           98.7%  ############################
- St. Charles Place         98.7%  ############################
- B&O Railroad              98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.99 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.97 per space
- green      0.98 per space
- darkblue   0.98 per space
