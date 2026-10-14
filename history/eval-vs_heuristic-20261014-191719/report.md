# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261014-191719`
Games logged: 300
Average rounds per game: 104.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 30 | 10.0% |
| heuristic_1 | 134 | 44.7% |
| heuristic_2 | 136 | 45.3% |

## End condition

- last_standing: 226 (75.3%)
- round_limit: 74 (24.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 50% | 37% | 93 |
| 2 | 30 | 20% | 43% | 37% | 100 |
| 3 | 30 | 3% | 33% | 63% | 121 |
| 4 | 30 | 10% | 50% | 40% | 93 |
| 5 | 30 | 17% | 47% | 37% | 88 |
| 6 | 30 | 10% | 37% | 53% | 113 |
| 7 | 30 | 10% | 47% | 43% | 118 |
| 8 | 30 | 3% | 50% | 47% | 108 |
| 9 | 30 | 0% | 50% | 50% | 126 |
| 10 | 30 | 13% | 40% | 47% | 88 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.4 | 1.6 | 1344 | 0.09 |
| heuristic_1 | 11.7 | 15.0 | 4221 | 0.66 |
| heuristic_2 | 12.5 | 17.4 | 4083 | 0.82 |

## Properties most often held by the winner

- Oriental Avenue           86.7%  ############################
- Electric Company          85.7%  ############################
- Pennsylvania Railroad     85.7%  ############################
- B&O Railroad              85.3%  ############################
- Baltic Avenue             85.0%  ###########################-
- Water Works               85.0%  ###########################-
- Tennessee Avenue          84.7%  ###########################-
- Pacific Avenue            84.7%  ###########################-
- Short Line                84.7%  ###########################-
- Mediterranean Avenue      84.3%  ###########################-
- Virginia Avenue           84.3%  ###########################-
- Reading Railroad          84.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.85 per space
- rail       0.85 per space
- lightblue  0.84 per space
- pink       0.83 per space
- util       0.85 per space
- orange     0.84 per space
- red        0.83 per space
- yellow     0.83 per space
- green      0.83 per space
- darkblue   0.81 per space
