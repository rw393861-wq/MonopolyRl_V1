# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260926-182233`
Games logged: 300
Average rounds per game: 101.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 24 | 8.0% |
| heuristic_1 | 131 | 43.7% |
| heuristic_2 | 145 | 48.3% |

## End condition

- round_limit: 61 (20.3%)
- last_standing: 239 (79.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 53% | 37% | 88 |
| 2 | 30 | 3% | 40% | 57% | 94 |
| 3 | 30 | 7% | 60% | 33% | 99 |
| 4 | 30 | 3% | 37% | 60% | 115 |
| 5 | 30 | 7% | 23% | 70% | 105 |
| 6 | 30 | 3% | 47% | 50% | 91 |
| 7 | 30 | 13% | 47% | 40% | 121 |
| 8 | 30 | 10% | 57% | 33% | 93 |
| 9 | 30 | 10% | 43% | 47% | 109 |
| 10 | 30 | 13% | 30% | 57% | 99 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.7 | 1.9 | 1202 | 0.06 |
| heuristic_1 | 12.1 | 15.3 | 4242 | 0.59 |
| heuristic_2 | 12.9 | 17.3 | 4526 | 0.77 |

## Properties most often held by the winner

- Electric Company          90.7%  ############################
- Mediterranean Avenue      88.7%  ###########################-
- Baltic Avenue             88.3%  ###########################-
- Kentucky Avenue           88.3%  ###########################-
- Water Works               88.3%  ###########################-
- States Avenue             88.0%  ###########################-
- Reading Railroad          87.7%  ###########################-
- Tennessee Avenue          87.7%  ###########################-
- Vermont Avenue            87.7%  ###########################-
- Ventnor Avenue            87.7%  ###########################-
- St. James Place           87.3%  ###########################-
- Short Line                87.3%  ###########################-

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.87 per space
- lightblue  0.87 per space
- pink       0.86 per space
- util       0.90 per space
- orange     0.87 per space
- red        0.87 per space
- yellow     0.87 per space
- green      0.85 per space
- darkblue   0.86 per space
