# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260925-191441`
Games logged: 300
Average rounds per game: 99.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 13 | 4.3% |
| heuristic_1 | 142 | 47.3% |
| heuristic_2 | 145 | 48.3% |

## End condition

- round_limit: 50 (16.7%)
- last_standing: 250 (83.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 0% | 50% | 50% | 113 |
| 2 | 30 | 10% | 30% | 60% | 94 |
| 3 | 30 | 3% | 57% | 40% | 94 |
| 4 | 30 | 7% | 43% | 50% | 102 |
| 5 | 30 | 7% | 57% | 37% | 92 |
| 6 | 30 | 10% | 57% | 33% | 101 |
| 7 | 30 | 3% | 40% | 57% | 106 |
| 8 | 30 | 0% | 43% | 57% | 91 |
| 9 | 30 | 0% | 57% | 43% | 103 |
| 10 | 30 | 3% | 40% | 57% | 96 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.0 | 1.2 | 832 | 0.08 |
| heuristic_1 | 12.6 | 18.2 | 4527 | 1.19 |
| heuristic_2 | 13.1 | 19.4 | 4832 | 1.18 |

## Properties most often held by the winner

- Baltic Avenue             93.0%  ############################
- Water Works               91.3%  ###########################-
- B&O Railroad              91.0%  ###########################-
- Mediterranean Avenue      91.0%  ###########################-
- Vermont Avenue            90.7%  ###########################-
- Pennsylvania Railroad     90.7%  ###########################-
- Pacific Avenue            90.7%  ###########################-
- North Carolina Avenue     90.7%  ###########################-
- States Avenue             90.0%  ###########################-
- Tennessee Avenue          89.7%  ###########################-
- Reading Railroad          89.7%  ###########################-
- St. James Place           89.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.90 per space
- lightblue  0.89 per space
- pink       0.89 per space
- util       0.89 per space
- orange     0.89 per space
- red        0.88 per space
- yellow     0.88 per space
- green      0.90 per space
- darkblue   0.89 per space
