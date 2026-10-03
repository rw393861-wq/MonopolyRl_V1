# Monopoly self-play report

Run directory: `logs/eval-arena-20261003-183516`
Games logged: 300
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 58 | 19.3% |
| random_1 | 82 | 27.3% |
| heuristic_1 | 160 | 53.3% |

## End condition

- last_standing: 297 (99.0%)
- round_limit: 3 (1.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 20% | 60% | 63 |
| 2 | 30 | 23% | 10% | 67% | 61 |
| 3 | 30 | 27% | 20% | 53% | 68 |
| 4 | 30 | 13% | 30% | 57% | 61 |
| 5 | 30 | 33% | 30% | 37% | 57 |
| 6 | 30 | 27% | 50% | 23% | 54 |
| 7 | 30 | 7% | 30% | 63% | 63 |
| 8 | 30 | 10% | 40% | 50% | 59 |
| 9 | 30 | 17% | 33% | 50% | 55 |
| 10 | 30 | 17% | 10% | 73% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.2 | 9.2 | 1831 | 0.72 |
| random_1 | 7.6 | 14.8 | 2482 | 1.40 |
| heuristic_1 | 14.6 | 26.6 | 4079 | 2.43 |

## Properties most often held by the winner

- Boardwalk                 99.3%  ############################
- Tennessee Avenue          98.7%  ############################
- Marvin Gardens            98.7%  ############################
- Oriental Avenue           98.3%  ############################
- Vermont Avenue            98.3%  ############################
- St. Charles Place         98.3%  ############################
- New York Avenue           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Water Works               98.3%  ############################
- North Carolina Avenue     98.3%  ############################
- Short Line                98.3%  ############################
- Connecticut Avenue        98.0%  ############################

## Colour group pull rate (winner)

- brown      0.94 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
