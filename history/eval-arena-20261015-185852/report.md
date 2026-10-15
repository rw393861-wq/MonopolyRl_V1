# Monopoly self-play report

Run directory: `logs/eval-arena-20261015-185852`
Games logged: 300
Average rounds per game: 61.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 56 | 18.7% |
| random_1 | 89 | 29.7% |
| heuristic_1 | 155 | 51.7% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 30% | 47% | 62 |
| 2 | 30 | 30% | 13% | 57% | 58 |
| 3 | 30 | 20% | 23% | 57% | 61 |
| 4 | 30 | 13% | 33% | 53% | 67 |
| 5 | 30 | 7% | 40% | 53% | 64 |
| 6 | 30 | 17% | 33% | 50% | 58 |
| 7 | 30 | 17% | 37% | 47% | 61 |
| 8 | 30 | 17% | 43% | 40% | 63 |
| 9 | 30 | 23% | 20% | 57% | 60 |
| 10 | 30 | 20% | 23% | 57% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 6.3 | 1606 | 0.53 |
| random_1 | 8.2 | 15.7 | 2737 | 1.43 |
| heuristic_1 | 14.1 | 28.5 | 4057 | 2.47 |

## Properties most often held by the winner

- Illinois Avenue           99.0%  ############################
- Virginia Avenue           98.7%  ############################
- Marvin Gardens            98.7%  ############################
- Connecticut Avenue        98.3%  ############################
- Electric Company          98.3%  ############################
- New York Avenue           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pacific Avenue            98.3%  ############################
- St. James Place           98.0%  ############################
- Tennessee Avenue          98.0%  ############################
- Atlantic Avenue           98.0%  ############################
- Short Line                98.0%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.98 per space
- darkblue   0.96 per space
