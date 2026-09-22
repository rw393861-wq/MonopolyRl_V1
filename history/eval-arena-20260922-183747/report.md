# Monopoly self-play report

Run directory: `logs/eval-arena-20260922-183747`
Games logged: 300
Average rounds per game: 61.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 32 | 10.7% |
| random_1 | 90 | 30.0% |
| heuristic_1 | 178 | 59.3% |

## End condition

- last_standing: 298 (99.3%)
- round_limit: 2 (0.7%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 27% | 60% | 64 |
| 2 | 30 | 3% | 27% | 70% | 59 |
| 3 | 30 | 13% | 37% | 50% | 64 |
| 4 | 30 | 10% | 33% | 57% | 65 |
| 5 | 30 | 10% | 27% | 63% | 57 |
| 6 | 30 | 7% | 40% | 53% | 58 |
| 7 | 30 | 13% | 40% | 47% | 62 |
| 8 | 30 | 17% | 30% | 53% | 60 |
| 9 | 30 | 7% | 20% | 73% | 62 |
| 10 | 30 | 13% | 20% | 67% | 65 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.9 | 4.2 | 1046 | 0.56 |
| random_1 | 8.3 | 17.3 | 2850 | 1.52 |
| heuristic_1 | 16.3 | 32.5 | 4483 | 2.71 |

## Properties most often held by the winner

- Oriental Avenue           99.7%  ############################
- Electric Company          99.7%  ############################
- Boardwalk                 99.7%  ############################
- Reading Railroad          99.3%  ############################
- St. Charles Place         99.3%  ############################
- Illinois Avenue           99.3%  ############################
- Connecticut Avenue        99.0%  ############################
- New York Avenue           99.0%  ############################
- Kentucky Avenue           99.0%  ############################
- Marvin Gardens            99.0%  ############################
- Pennsylvania Railroad     98.7%  ############################
- Water Works               98.7%  ############################

## Colour group pull rate (winner)

- brown      0.97 per space
- rail       0.98 per space
- lightblue  0.99 per space
- pink       0.98 per space
- util       0.99 per space
- orange     0.98 per space
- red        0.99 per space
- yellow     0.99 per space
- green      0.97 per space
- darkblue   0.99 per space
