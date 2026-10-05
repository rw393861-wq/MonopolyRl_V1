# Monopoly self-play report

Run directory: `logs/eval-arena-20261005-215323`
Games logged: 300
Average rounds per game: 64.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 54 | 18.0% |
| random_1 | 91 | 30.3% |
| heuristic_1 | 155 | 51.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 30% | 60% | 60 |
| 2 | 30 | 13% | 27% | 60% | 62 |
| 3 | 30 | 27% | 30% | 43% | 67 |
| 4 | 30 | 17% | 33% | 50% | 68 |
| 5 | 30 | 23% | 30% | 47% | 67 |
| 6 | 30 | 10% | 37% | 53% | 60 |
| 7 | 30 | 13% | 43% | 43% | 68 |
| 8 | 30 | 17% | 30% | 53% | 65 |
| 9 | 30 | 20% | 30% | 50% | 58 |
| 10 | 30 | 30% | 13% | 57% | 69 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.9 | 6.4 | 1621 | 0.58 |
| random_1 | 8.4 | 17.3 | 3010 | 1.60 |
| heuristic_1 | 14.2 | 29.2 | 4319 | 2.65 |

## Properties most often held by the winner

- Connecticut Avenue        99.3%  ############################
- Electric Company          99.3%  ############################
- Tennessee Avenue          99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Reading Railroad          98.7%  ############################
- Vermont Avenue            98.7%  ############################
- Virginia Avenue           98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- St. Charles Place         98.3%  ############################
- States Avenue             98.3%  ############################
- Pennsylvania Railroad     98.3%  ############################
- Indiana Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
