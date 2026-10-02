# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261002-195355`
Games logged: 300
Average rounds per game: 101.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 135 | 45.0% |
| heuristic_2 | 125 | 41.7% |

## End condition

- last_standing: 239 (79.7%)
- round_limit: 61 (20.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 47% | 37% | 93 |
| 2 | 30 | 20% | 43% | 37% | 111 |
| 3 | 30 | 20% | 40% | 40% | 97 |
| 4 | 30 | 13% | 40% | 47% | 106 |
| 5 | 30 | 3% | 60% | 37% | 91 |
| 6 | 30 | 23% | 33% | 43% | 99 |
| 7 | 30 | 7% | 47% | 47% | 90 |
| 8 | 30 | 7% | 47% | 47% | 113 |
| 9 | 30 | 13% | 53% | 33% | 110 |
| 10 | 30 | 10% | 40% | 50% | 108 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.9 | 4.0 | 1612 | 0.18 |
| heuristic_1 | 12.5 | 17.1 | 4293 | 0.85 |
| heuristic_2 | 11.4 | 15.1 | 4009 | 0.86 |

## Properties most often held by the winner

- Pennsylvania Railroad     91.7%  ############################
- Reading Railroad          90.0%  ###########################-
- Mediterranean Avenue      89.0%  ###########################-
- Short Line                89.0%  ###########################-
- New York Avenue           88.7%  ###########################-
- B&O Railroad              88.7%  ###########################-
- North Carolina Avenue     88.3%  ###########################-
- Oriental Avenue           88.0%  ###########################-
- St. Charles Place         88.0%  ###########################-
- Water Works               88.0%  ###########################-
- Baltic Avenue             87.7%  ###########################-
- Pacific Avenue            87.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.90 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.87 per space
- orange     0.87 per space
- red        0.86 per space
- yellow     0.85 per space
- green      0.88 per space
- darkblue   0.86 per space
