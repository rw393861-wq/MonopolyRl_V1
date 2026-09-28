# Monopoly self-play report

Run directory: `logs/eval-arena-20260928-210433`
Games logged: 300
Average rounds per game: 59.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 61 | 20.3% |
| random_1 | 87 | 29.0% |
| heuristic_1 | 152 | 50.7% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 27% | 53% | 59 |
| 2 | 30 | 23% | 37% | 40% | 60 |
| 3 | 30 | 20% | 30% | 50% | 58 |
| 4 | 30 | 27% | 20% | 53% | 57 |
| 5 | 30 | 17% | 30% | 53% | 62 |
| 6 | 30 | 10% | 40% | 50% | 56 |
| 7 | 30 | 10% | 37% | 53% | 65 |
| 8 | 30 | 10% | 33% | 57% | 61 |
| 9 | 30 | 20% | 20% | 60% | 60 |
| 10 | 30 | 47% | 17% | 37% | 56 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.5 | 7.1 | 1679 | 0.64 |
| random_1 | 8.0 | 15.1 | 2615 | 1.47 |
| heuristic_1 | 13.9 | 26.6 | 3873 | 2.35 |

## Properties most often held by the winner

- Tennessee Avenue          99.7%  ############################
- Reading Railroad          99.3%  ############################
- Oriental Avenue           99.3%  ############################
- Virginia Avenue           99.3%  ############################
- New York Avenue           99.3%  ############################
- Connecticut Avenue        99.0%  ############################
- Pennsylvania Railroad     99.0%  ############################
- Illinois Avenue           99.0%  ############################
- Indiana Avenue            98.7%  ############################
- Water Works               98.7%  ############################
- Boardwalk                 98.7%  ############################
- Vermont Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.99 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
