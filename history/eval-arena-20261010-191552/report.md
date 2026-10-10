# Monopoly self-play report

Run directory: `logs/eval-arena-20261010-191552`
Games logged: 300
Average rounds per game: 63.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 98 | 32.7% |
| random_1 | 72 | 24.0% |
| heuristic_1 | 130 | 43.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 30% | 43% | 58 |
| 2 | 30 | 47% | 10% | 43% | 63 |
| 3 | 30 | 20% | 30% | 50% | 67 |
| 4 | 30 | 43% | 27% | 30% | 64 |
| 5 | 30 | 30% | 27% | 43% | 62 |
| 6 | 30 | 30% | 23% | 47% | 68 |
| 7 | 30 | 33% | 23% | 43% | 61 |
| 8 | 30 | 37% | 23% | 40% | 59 |
| 9 | 30 | 33% | 27% | 40% | 67 |
| 10 | 30 | 27% | 20% | 53% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 8.7 | 13.5 | 2530 | 0.90 |
| random_1 | 6.6 | 14.4 | 2496 | 1.42 |
| heuristic_1 | 12.0 | 24.0 | 3628 | 2.51 |

## Properties most often held by the winner

- Illinois Avenue           99.3%  ############################
- New York Avenue           99.0%  ############################
- Reading Railroad          98.7%  ############################
- St. Charles Place         98.7%  ############################
- Electric Company          98.7%  ############################
- States Avenue             98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- Oriental Avenue           98.3%  ############################
- St. James Place           98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Indiana Avenue            98.3%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
