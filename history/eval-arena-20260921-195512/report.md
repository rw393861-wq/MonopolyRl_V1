# Monopoly self-play report

Run directory: `logs/eval-arena-20260921-195512`
Games logged: 300
Average rounds per game: 61.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 69 | 23.0% |
| random_1 | 80 | 26.7% |
| heuristic_1 | 151 | 50.3% |

## End condition

- last_standing: 300 (100.0%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 20% | 60% | 61 |
| 2 | 30 | 30% | 37% | 33% | 55 |
| 3 | 30 | 23% | 37% | 40% | 67 |
| 4 | 30 | 23% | 20% | 57% | 61 |
| 5 | 30 | 37% | 17% | 47% | 63 |
| 6 | 30 | 23% | 30% | 47% | 63 |
| 7 | 30 | 13% | 17% | 70% | 64 |
| 8 | 30 | 20% | 33% | 47% | 62 |
| 9 | 30 | 20% | 30% | 50% | 61 |
| 10 | 30 | 20% | 27% | 53% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.3 | 9.6 | 1977 | 0.83 |
| random_1 | 7.3 | 14.8 | 2594 | 1.37 |
| heuristic_1 | 13.8 | 26.8 | 3977 | 2.60 |

## Properties most often held by the winner

- Boardwalk                 99.7%  ############################
- Reading Railroad          99.0%  ############################
- Water Works               99.0%  ############################
- St. Charles Place         98.7%  ############################
- New York Avenue           98.7%  ############################
- B&O Railroad              98.7%  ############################
- Atlantic Avenue           98.7%  ############################
- Pacific Avenue            98.7%  ############################
- Vermont Avenue            98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Illinois Avenue           98.3%  ############################
- Oriental Avenue           98.0%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.97 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
