# Monopoly self-play report

Run directory: `logs/eval-arena-20260927-185354`
Games logged: 300
Average rounds per game: 61.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 70 | 23.3% |
| random_1 | 79 | 26.3% |
| heuristic_1 | 151 | 50.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 17% | 63% | 67 |
| 2 | 30 | 17% | 17% | 67% | 64 |
| 3 | 30 | 17% | 20% | 63% | 62 |
| 4 | 30 | 23% | 33% | 43% | 57 |
| 5 | 30 | 27% | 23% | 50% | 58 |
| 6 | 30 | 37% | 30% | 33% | 65 |
| 7 | 30 | 27% | 33% | 40% | 64 |
| 8 | 30 | 10% | 23% | 67% | 60 |
| 9 | 30 | 33% | 30% | 37% | 60 |
| 10 | 30 | 23% | 37% | 40% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.3 | 10.4 | 1999 | 0.91 |
| random_1 | 7.3 | 14.4 | 2463 | 1.36 |
| heuristic_1 | 13.9 | 26.3 | 3970 | 2.52 |

## Properties most often held by the winner

- Reading Railroad          99.3%  ############################
- Oriental Avenue           99.0%  ############################
- St. Charles Place         98.7%  ############################
- B&O Railroad              98.7%  ############################
- Ventnor Avenue            98.7%  ############################
- Pacific Avenue            98.7%  ############################
- New York Avenue           98.3%  ############################
- Illinois Avenue           98.3%  ############################
- Atlantic Avenue           98.3%  ############################
- Water Works               98.3%  ############################
- Boardwalk                 98.3%  ############################
- Virginia Avenue           98.0%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.97 per space
