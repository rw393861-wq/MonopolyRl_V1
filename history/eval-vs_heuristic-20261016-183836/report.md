# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261016-183836`
Games logged: 300
Average rounds per game: 93.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 48 | 16.0% |
| heuristic_1 | 121 | 40.3% |
| heuristic_2 | 131 | 43.7% |

## End condition

- round_limit: 48 (16.0%)
- last_standing: 252 (84.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 30% | 37% | 33% | 102 |
| 2 | 30 | 7% | 30% | 63% | 97 |
| 3 | 30 | 17% | 50% | 33% | 90 |
| 4 | 30 | 7% | 57% | 37% | 98 |
| 5 | 30 | 7% | 43% | 50% | 89 |
| 6 | 30 | 13% | 40% | 47% | 101 |
| 7 | 30 | 20% | 33% | 47% | 97 |
| 8 | 30 | 20% | 20% | 60% | 80 |
| 9 | 30 | 17% | 43% | 40% | 98 |
| 10 | 30 | 23% | 50% | 27% | 83 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.2 | 4.9 | 1653 | 0.35 |
| heuristic_1 | 10.9 | 15.5 | 4172 | 1.05 |
| heuristic_2 | 11.5 | 17.3 | 4072 | 1.12 |

## Properties most often held by the winner

- Baltic Avenue             92.7%  ############################
- Pennsylvania Railroad     92.0%  ############################
- Water Works               91.3%  ############################
- Reading Railroad          91.0%  ###########################-
- States Avenue             90.3%  ###########################-
- B&O Railroad              90.3%  ###########################-
- Mediterranean Avenue      90.0%  ###########################-
- St. Charles Place         90.0%  ###########################-
- New York Avenue           90.0%  ###########################-
- North Carolina Avenue     90.0%  ###########################-
- Short Line                89.7%  ###########################-
- Marvin Gardens            89.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.91 per space
- lightblue  0.87 per space
- pink       0.90 per space
- util       0.90 per space
- orange     0.89 per space
- red        0.88 per space
- yellow     0.88 per space
- green      0.89 per space
- darkblue   0.88 per space
