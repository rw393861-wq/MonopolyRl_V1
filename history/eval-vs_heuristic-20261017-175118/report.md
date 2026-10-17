# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261017-175118`
Games logged: 300
Average rounds per game: 99.1

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 48 | 16.0% |
| heuristic_1 | 110 | 36.7% |
| heuristic_2 | 142 | 47.3% |

## End condition

- round_limit: 59 (19.7%)
- last_standing: 241 (80.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 27% | 57% | 83 |
| 2 | 30 | 17% | 27% | 57% | 116 |
| 3 | 30 | 10% | 40% | 50% | 94 |
| 4 | 30 | 17% | 33% | 50% | 93 |
| 5 | 30 | 23% | 27% | 50% | 90 |
| 6 | 30 | 10% | 53% | 37% | 112 |
| 7 | 30 | 20% | 43% | 37% | 104 |
| 8 | 30 | 20% | 27% | 53% | 110 |
| 9 | 30 | 10% | 53% | 37% | 102 |
| 10 | 30 | 17% | 37% | 47% | 88 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.4 | 8.4 | 2128 | 0.64 |
| heuristic_1 | 10.4 | 15.3 | 3762 | 0.97 |
| heuristic_2 | 11.8 | 16.8 | 4156 | 1.04 |

## Properties most often held by the winner

- B&O Railroad              92.7%  ############################
- Reading Railroad          91.0%  ###########################-
- Pennsylvania Railroad     91.0%  ###########################-
- Mediterranean Avenue      90.3%  ###########################-
- Electric Company          89.0%  ###########################-
- Water Works               88.7%  ###########################-
- Illinois Avenue           88.0%  ###########################-
- Kentucky Avenue           87.7%  ##########################--
- Baltic Avenue             87.0%  ##########################--
- States Avenue             86.7%  ##########################--
- North Carolina Avenue     86.7%  ##########################--
- Park Place                86.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.90 per space
- lightblue  0.86 per space
- pink       0.86 per space
- util       0.89 per space
- orange     0.86 per space
- red        0.87 per space
- yellow     0.85 per space
- green      0.86 per space
- darkblue   0.86 per space
