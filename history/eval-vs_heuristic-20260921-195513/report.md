# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260921-195513`
Games logged: 300
Average rounds per game: 102.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 136 | 45.3% |
| heuristic_2 | 124 | 41.3% |

## End condition

- round_limit: 53 (17.7%)
- last_standing: 247 (82.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 57% | 30% | 87 |
| 2 | 30 | 30% | 40% | 30% | 89 |
| 3 | 30 | 3% | 53% | 43% | 118 |
| 4 | 30 | 20% | 50% | 30% | 118 |
| 5 | 30 | 17% | 27% | 57% | 98 |
| 6 | 30 | 13% | 37% | 50% | 102 |
| 7 | 30 | 3% | 47% | 50% | 111 |
| 8 | 30 | 7% | 53% | 40% | 109 |
| 9 | 30 | 7% | 47% | 47% | 93 |
| 10 | 30 | 20% | 43% | 37% | 101 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.3 | 5.5 | 2058 | 0.24 |
| heuristic_1 | 11.9 | 19.0 | 4904 | 1.14 |
| heuristic_2 | 11.6 | 18.1 | 4508 | 1.14 |

## Properties most often held by the winner

- Short Line                92.3%  ############################
- Baltic Avenue             91.7%  ############################
- Pennsylvania Railroad     91.3%  ############################
- Water Works               91.3%  ############################
- Mediterranean Avenue      91.0%  ############################
- Oriental Avenue           90.3%  ###########################-
- St. Charles Place         90.3%  ###########################-
- New York Avenue           90.3%  ###########################-
- St. James Place           90.0%  ###########################-
- B&O Railroad              90.0%  ###########################-
- Pacific Avenue            90.0%  ###########################-
- Electric Company          90.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.90 per space
- lightblue  0.89 per space
- pink       0.90 per space
- util       0.91 per space
- orange     0.90 per space
- red        0.88 per space
- yellow     0.89 per space
- green      0.89 per space
- darkblue   0.88 per space
