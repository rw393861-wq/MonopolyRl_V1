# Monopoly self-play report

Run directory: `logs/eval-arena-20261024-175536`
Games logged: 300
Average rounds per game: 63.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 61 | 20.3% |
| random_1 | 86 | 28.7% |
| heuristic_1 | 153 | 51.0% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 30% | 53% | 71 |
| 2 | 30 | 30% | 33% | 37% | 62 |
| 3 | 30 | 13% | 30% | 57% | 62 |
| 4 | 30 | 27% | 23% | 50% | 58 |
| 5 | 30 | 27% | 23% | 50% | 69 |
| 6 | 30 | 10% | 37% | 53% | 68 |
| 7 | 30 | 27% | 27% | 47% | 73 |
| 8 | 30 | 17% | 37% | 47% | 59 |
| 9 | 30 | 23% | 17% | 60% | 62 |
| 10 | 30 | 13% | 30% | 57% | 55 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.6 | 7.5 | 1774 | 0.68 |
| random_1 | 7.9 | 16.0 | 2965 | 1.54 |
| heuristic_1 | 14.1 | 29.1 | 4156 | 2.71 |

## Properties most often held by the winner

- Reading Railroad         100.0%  ############################
- Connecticut Avenue        99.7%  ############################
- Electric Company          99.7%  ############################
- Oriental Avenue           99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Water Works               99.3%  ############################
- St. Charles Place         99.0%  ############################
- States Avenue             99.0%  ############################
- St. James Place           99.0%  ############################
- New York Avenue           99.0%  ############################
- Vermont Avenue            98.7%  ############################
- Pennsylvania Railroad     98.7%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.99 per space
- lightblue  0.99 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.98 per space
