# Monopoly self-play report

Run directory: `logs/eval-arena-20261007-202734`
Games logged: 300
Average rounds per game: 66.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| random_1 | 116 | 38.7% |
| heuristic_1 | 144 | 48.0% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 50% | 40% | 69 |
| 2 | 30 | 10% | 43% | 47% | 67 |
| 3 | 30 | 17% | 47% | 37% | 64 |
| 4 | 30 | 17% | 37% | 47% | 61 |
| 5 | 30 | 10% | 40% | 50% | 67 |
| 6 | 30 | 10% | 23% | 67% | 63 |
| 7 | 30 | 10% | 50% | 40% | 79 |
| 8 | 30 | 7% | 40% | 53% | 70 |
| 9 | 30 | 17% | 27% | 57% | 63 |
| 10 | 30 | 27% | 30% | 43% | 63 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.6 | 5.7 | 1459 | 0.64 |
| random_1 | 10.6 | 19.2 | 3520 | 1.72 |
| heuristic_1 | 13.3 | 27.9 | 4148 | 2.77 |

## Properties most often held by the winner

- Pennsylvania Railroad     99.7%  ############################
- Reading Railroad          99.3%  ############################
- New York Avenue           99.3%  ############################
- Kentucky Avenue           99.3%  ############################
- Illinois Avenue           99.0%  ############################
- Boardwalk                 99.0%  ############################
- Vermont Avenue            98.7%  ############################
- Electric Company          98.7%  ############################
- Tennessee Avenue          98.7%  ############################
- B&O Railroad              98.7%  ############################
- Pennsylvania Avenue       98.7%  ############################
- St. Charles Place         98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
