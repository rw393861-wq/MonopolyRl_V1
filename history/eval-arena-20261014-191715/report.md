# Monopoly self-play report

Run directory: `logs/eval-arena-20261014-191715`
Games logged: 300
Average rounds per game: 68.9

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 48 | 16.0% |
| random_1 | 109 | 36.3% |
| heuristic_1 | 143 | 47.7% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 23% | 57% | 72 |
| 2 | 30 | 20% | 40% | 40% | 67 |
| 3 | 30 | 7% | 43% | 50% | 71 |
| 4 | 30 | 10% | 37% | 53% | 63 |
| 5 | 30 | 17% | 33% | 50% | 73 |
| 6 | 30 | 17% | 30% | 53% | 69 |
| 7 | 30 | 23% | 37% | 40% | 68 |
| 8 | 30 | 20% | 50% | 30% | 69 |
| 9 | 30 | 17% | 37% | 47% | 57 |
| 10 | 30 | 10% | 33% | 57% | 82 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.5 | 6.6 | 1689 | 0.89 |
| random_1 | 10.1 | 18.2 | 3524 | 1.56 |
| heuristic_1 | 13.0 | 27.6 | 4188 | 2.46 |

## Properties most often held by the winner

- Reading Railroad          99.7%  ############################
- St. Charles Place         99.7%  ############################
- B&O Railroad              99.7%  ############################
- St. James Place           99.0%  ############################
- Illinois Avenue           99.0%  ############################
- Boardwalk                 99.0%  ############################
- Baltic Avenue             98.7%  ############################
- Vermont Avenue            98.7%  ############################
- Electric Company          98.7%  ############################
- New York Avenue           98.7%  ############################
- Indiana Avenue            98.7%  ############################
- Ventnor Avenue            98.7%  ############################

## Colour group pull rate (winner)

- brown      0.98 per space
- rail       0.99 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.99 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
