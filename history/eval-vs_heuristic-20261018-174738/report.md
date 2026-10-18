# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261018-174738`
Games logged: 300
Average rounds per game: 100.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 44 | 14.7% |
| heuristic_1 | 120 | 40.0% |
| heuristic_2 | 136 | 45.3% |

## End condition

- round_limit: 58 (19.3%)
- last_standing: 242 (80.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 20% | 47% | 33% | 100 |
| 2 | 30 | 10% | 23% | 67% | 109 |
| 3 | 30 | 13% | 53% | 33% | 100 |
| 4 | 30 | 20% | 30% | 50% | 104 |
| 5 | 30 | 13% | 33% | 53% | 94 |
| 6 | 30 | 20% | 37% | 43% | 96 |
| 7 | 30 | 7% | 50% | 43% | 97 |
| 8 | 30 | 3% | 43% | 53% | 98 |
| 9 | 30 | 20% | 40% | 40% | 111 |
| 10 | 30 | 20% | 43% | 37% | 94 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.4 | 3.6 | 1647 | 0.16 |
| heuristic_1 | 11.6 | 15.5 | 4244 | 0.74 |
| heuristic_2 | 11.7 | 16.2 | 4276 | 0.74 |

## Properties most often held by the winner

- Pennsylvania Railroad     91.0%  ############################
- Vermont Avenue            90.3%  ############################
- Water Works               90.0%  ############################
- States Avenue             89.3%  ###########################-
- Oriental Avenue           89.0%  ###########################-
- New York Avenue           89.0%  ###########################-
- B&O Railroad              89.0%  ###########################-
- Pacific Avenue            89.0%  ###########################-
- Mediterranean Avenue      88.7%  ###########################-
- Tennessee Avenue          88.0%  ###########################-
- North Carolina Avenue     88.0%  ###########################-
- Ventnor Avenue            88.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.87 per space
- rail       0.89 per space
- lightblue  0.89 per space
- pink       0.87 per space
- util       0.89 per space
- orange     0.88 per space
- red        0.87 per space
- yellow     0.88 per space
- green      0.87 per space
- darkblue   0.87 per space
