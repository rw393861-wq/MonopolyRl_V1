# Monopoly self-play report

Run directory: `logs/eval-arena-20260929-195449`
Games logged: 300
Average rounds per game: 63.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 88 | 29.3% |
| random_1 | 72 | 24.0% |
| heuristic_1 | 140 | 46.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 33% | 23% | 43% | 57 |
| 2 | 30 | 37% | 27% | 37% | 64 |
| 3 | 30 | 33% | 17% | 50% | 69 |
| 4 | 30 | 30% | 13% | 57% | 65 |
| 5 | 30 | 17% | 30% | 53% | 63 |
| 6 | 30 | 47% | 17% | 37% | 58 |
| 7 | 30 | 23% | 30% | 47% | 62 |
| 8 | 30 | 20% | 37% | 43% | 63 |
| 9 | 30 | 27% | 17% | 57% | 66 |
| 10 | 30 | 27% | 30% | 43% | 70 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 7.9 | 10.2 | 2297 | 0.64 |
| random_1 | 6.6 | 14.0 | 2590 | 1.32 |
| heuristic_1 | 12.8 | 26.3 | 3873 | 2.58 |

## Properties most often held by the winner

- Reading Railroad          99.0%  ############################
- Electric Company          98.7%  ############################
- St. James Place           98.7%  ############################
- Tennessee Avenue          98.3%  ############################
- New York Avenue           98.3%  ############################
- Illinois Avenue           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pacific Avenue            98.3%  ############################
- Virginia Avenue           98.0%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Oriental Avenue           97.7%  ############################
- St. Charles Place         97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
