# Monopoly self-play report

Run directory: `logs/eval-arena-20261020-185802`
Games logged: 300
Average rounds per game: 60.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 60 | 20.0% |
| random_1 | 75 | 25.0% |
| heuristic_1 | 165 | 55.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 23% | 63% | 59 |
| 2 | 30 | 20% | 23% | 57% | 56 |
| 3 | 30 | 23% | 20% | 57% | 64 |
| 4 | 30 | 33% | 30% | 37% | 64 |
| 5 | 30 | 20% | 17% | 63% | 62 |
| 6 | 30 | 17% | 30% | 53% | 59 |
| 7 | 30 | 13% | 33% | 53% | 57 |
| 8 | 30 | 10% | 30% | 60% | 64 |
| 9 | 30 | 20% | 13% | 67% | 61 |
| 10 | 30 | 30% | 30% | 40% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.5 | 7.9 | 1700 | 0.83 |
| random_1 | 7.0 | 14.0 | 2318 | 1.40 |
| heuristic_1 | 15.1 | 29.7 | 4231 | 2.75 |

## Properties most often held by the winner

- Virginia Avenue           99.7%  ############################
- Illinois Avenue           99.3%  ############################
- Marvin Gardens            99.3%  ############################
- St. Charles Place         99.0%  ############################
- States Avenue             99.0%  ############################
- Tennessee Avenue          99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Water Works               99.0%  ############################
- Oriental Avenue           98.7%  ############################
- Vermont Avenue            98.7%  ############################
- Connecticut Avenue        98.7%  ############################
- New York Avenue           98.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.97 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.99 per space
- yellow     0.99 per space
- green      0.98 per space
- darkblue   0.97 per space
