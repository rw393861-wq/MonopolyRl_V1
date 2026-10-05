# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261005-215325`
Games logged: 300
Average rounds per game: 105.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 15 | 5.0% |
| heuristic_1 | 139 | 46.3% |
| heuristic_2 | 146 | 48.7% |

## End condition

- last_standing: 234 (78.0%)
- round_limit: 66 (22.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 43% | 47% | 101 |
| 2 | 30 | 7% | 40% | 53% | 96 |
| 3 | 30 | 3% | 50% | 47% | 116 |
| 4 | 30 | 3% | 57% | 40% | 108 |
| 5 | 30 | 7% | 43% | 50% | 112 |
| 6 | 30 | 0% | 43% | 57% | 108 |
| 7 | 30 | 3% | 47% | 50% | 96 |
| 8 | 30 | 0% | 53% | 47% | 111 |
| 9 | 30 | 7% | 50% | 43% | 104 |
| 10 | 30 | 10% | 37% | 53% | 101 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.4 | 0.8 | 1248 | 0.20 |
| heuristic_1 | 12.1 | 18.9 | 4712 | 0.98 |
| heuristic_2 | 13.2 | 18.5 | 4716 | 0.98 |

## Properties most often held by the winner

- Baltic Avenue             92.0%  ############################
- Mediterranean Avenue      90.3%  ###########################-
- Atlantic Avenue           88.0%  ###########################-
- Illinois Avenue           87.7%  ###########################-
- Water Works               87.7%  ###########################-
- North Carolina Avenue     87.7%  ###########################-
- Pennsylvania Railroad     87.3%  ###########################-
- Kentucky Avenue           87.3%  ###########################-
- St. Charles Place         87.0%  ##########################--
- Pacific Avenue            87.0%  ##########################--
- Reading Railroad          86.7%  ##########################--
- Tennessee Avenue          86.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.86 per space
- lightblue  0.84 per space
- pink       0.86 per space
- util       0.87 per space
- orange     0.84 per space
- red        0.87 per space
- yellow     0.85 per space
- green      0.87 per space
- darkblue   0.84 per space
