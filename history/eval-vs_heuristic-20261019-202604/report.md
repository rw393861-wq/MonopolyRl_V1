# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261019-202604`
Games logged: 300
Average rounds per game: 102.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 65 | 21.7% |
| heuristic_1 | 107 | 35.7% |
| heuristic_2 | 128 | 42.7% |

## End condition

- round_limit: 59 (19.7%)
- last_standing: 241 (80.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 27% | 37% | 37% | 110 |
| 2 | 30 | 10% | 43% | 47% | 107 |
| 3 | 30 | 20% | 40% | 40% | 111 |
| 4 | 30 | 27% | 30% | 43% | 99 |
| 5 | 30 | 27% | 30% | 43% | 84 |
| 6 | 30 | 23% | 27% | 50% | 111 |
| 7 | 30 | 27% | 37% | 37% | 87 |
| 8 | 30 | 13% | 50% | 37% | 99 |
| 9 | 30 | 20% | 37% | 43% | 102 |
| 10 | 30 | 23% | 27% | 50% | 110 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 6.1 | 8.2 | 2531 | 0.49 |
| heuristic_1 | 10.3 | 15.4 | 3921 | 1.06 |
| heuristic_2 | 11.4 | 16.6 | 4328 | 1.11 |

## Properties most often held by the winner

- Atlantic Avenue           91.0%  ############################
- Reading Railroad          90.7%  ############################
- Connecticut Avenue        89.0%  ###########################-
- Boardwalk                 89.0%  ###########################-
- Mediterranean Avenue      88.7%  ###########################-
- Oriental Avenue           88.7%  ###########################-
- Short Line                88.3%  ###########################-
- Baltic Avenue             88.3%  ###########################-
- Pennsylvania Railroad     88.3%  ###########################-
- Tennessee Avenue          88.0%  ###########################-
- Marvin Gardens            88.0%  ###########################-
- Indiana Avenue            87.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.89 per space
- lightblue  0.88 per space
- pink       0.87 per space
- util       0.86 per space
- orange     0.87 per space
- red        0.87 per space
- yellow     0.89 per space
- green      0.86 per space
- darkblue   0.88 per space
