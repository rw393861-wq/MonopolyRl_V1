# Monopoly self-play report

Run directory: `logs/eval-arena-20261004-184101`
Games logged: 300
Average rounds per game: 58.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 54 | 18.0% |
| random_1 | 76 | 25.3% |
| heuristic_1 | 170 | 56.7% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 30% | 30% | 40% | 56 |
| 2 | 30 | 13% | 27% | 60% | 54 |
| 3 | 30 | 20% | 30% | 50% | 61 |
| 4 | 30 | 23% | 13% | 63% | 56 |
| 5 | 30 | 20% | 27% | 53% | 58 |
| 6 | 30 | 7% | 30% | 63% | 59 |
| 7 | 30 | 20% | 23% | 57% | 56 |
| 8 | 30 | 20% | 23% | 57% | 60 |
| 9 | 30 | 20% | 30% | 50% | 65 |
| 10 | 30 | 7% | 20% | 73% | 57 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.8 | 5.3 | 1478 | 0.50 |
| random_1 | 6.9 | 15.6 | 2482 | 1.42 |
| heuristic_1 | 15.4 | 30.6 | 4217 | 2.70 |

## Properties most often held by the winner

- St. Charles Place         99.0%  ############################
- New York Avenue           98.7%  ############################
- Illinois Avenue           98.7%  ############################
- Tennessee Avenue          98.3%  ############################
- Reading Railroad          98.0%  ############################
- Marvin Gardens            98.0%  ############################
- States Avenue             97.7%  ############################
- North Carolina Avenue     97.7%  ############################
- Pennsylvania Railroad     97.3%  ############################
- Electric Company          97.3%  ############################
- Boardwalk                 97.3%  ############################
- Oriental Avenue           97.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.94 per space
- rail       0.97 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.97 per space
- yellow     0.97 per space
- green      0.96 per space
- darkblue   0.96 per space
