# Monopoly self-play report

Run directory: `logs/eval-arena-20260924-185727`
Games logged: 300
Average rounds per game: 59.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 46 | 15.3% |
| random_1 | 83 | 27.7% |
| heuristic_1 | 171 | 57.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 37% | 50% | 60 |
| 2 | 30 | 13% | 20% | 67% | 65 |
| 3 | 30 | 17% | 17% | 67% | 62 |
| 4 | 30 | 10% | 30% | 60% | 63 |
| 5 | 30 | 20% | 17% | 63% | 60 |
| 6 | 30 | 13% | 37% | 50% | 54 |
| 7 | 30 | 17% | 33% | 50% | 56 |
| 8 | 30 | 23% | 30% | 47% | 56 |
| 9 | 30 | 17% | 20% | 63% | 70 |
| 10 | 30 | 10% | 37% | 53% | 50 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.2 | 4.8 | 1396 | 0.60 |
| random_1 | 7.7 | 17.1 | 2634 | 1.56 |
| heuristic_1 | 15.6 | 29.7 | 4075 | 2.73 |

## Properties most often held by the winner

- St. Charles Place         99.7%  ############################
- Oriental Avenue           99.3%  ############################
- Connecticut Avenue        99.3%  ############################
- States Avenue             99.0%  ############################
- Virginia Avenue           99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- Reading Railroad          98.7%  ############################
- Vermont Avenue            98.7%  ############################
- Kentucky Avenue           98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- Electric Company          98.3%  ############################
- St. James Place           98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.97 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
