# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260927-185355`
Games logged: 300
Average rounds per game: 102.3

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 124 | 41.3% |
| heuristic_2 | 136 | 45.3% |

## End condition

- round_limit: 59 (19.7%)
- last_standing: 241 (80.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 43% | 40% | 108 |
| 2 | 30 | 13% | 50% | 37% | 125 |
| 3 | 30 | 7% | 60% | 33% | 97 |
| 4 | 30 | 13% | 37% | 50% | 105 |
| 5 | 30 | 13% | 30% | 57% | 97 |
| 6 | 30 | 20% | 40% | 40% | 101 |
| 7 | 30 | 13% | 33% | 53% | 95 |
| 8 | 30 | 17% | 43% | 40% | 87 |
| 9 | 30 | 7% | 37% | 57% | 114 |
| 10 | 30 | 13% | 40% | 47% | 95 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.3 | 4.5 | 1911 | 0.18 |
| heuristic_1 | 11.5 | 16.8 | 4257 | 1.01 |
| heuristic_2 | 12.0 | 18.5 | 4470 | 1.07 |

## Properties most often held by the winner

- Baltic Avenue             90.7%  ############################
- Pennsylvania Railroad     90.0%  ############################
- Mediterranean Avenue      90.0%  ############################
- Short Line                89.3%  ############################
- St. James Place           89.0%  ###########################-
- Reading Railroad          89.0%  ###########################-
- Illinois Avenue           89.0%  ###########################-
- B&O Railroad              89.0%  ###########################-
- Boardwalk                 89.0%  ###########################-
- New York Avenue           88.7%  ###########################-
- Ventnor Avenue            88.7%  ###########################-
- Water Works               88.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.88 per space
- pink       0.87 per space
- util       0.88 per space
- orange     0.89 per space
- red        0.88 per space
- yellow     0.86 per space
- green      0.87 per space
- darkblue   0.88 per space
