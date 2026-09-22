# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260922-183750`
Games logged: 300
Average rounds per game: 112.2

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 19 | 6.3% |
| heuristic_1 | 159 | 53.0% |
| heuristic_2 | 122 | 40.7% |

## End condition

- last_standing: 220 (73.3%)
- round_limit: 80 (26.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 7% | 50% | 43% | 91 |
| 2 | 30 | 0% | 67% | 33% | 114 |
| 3 | 30 | 3% | 63% | 33% | 136 |
| 4 | 30 | 17% | 43% | 40% | 109 |
| 5 | 30 | 0% | 50% | 50% | 106 |
| 6 | 30 | 7% | 47% | 47% | 133 |
| 7 | 30 | 3% | 67% | 30% | 109 |
| 8 | 30 | 3% | 47% | 50% | 114 |
| 9 | 30 | 10% | 47% | 43% | 99 |
| 10 | 30 | 13% | 50% | 37% | 111 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.6 | 1.1 | 1180 | 0.00 |
| heuristic_1 | 13.4 | 17.6 | 5001 | 0.71 |
| heuristic_2 | 11.6 | 14.6 | 4404 | 0.55 |

## Properties most often held by the winner

- Baltic Avenue             90.3%  ############################
- Mediterranean Avenue      86.3%  ###########################-
- Oriental Avenue           86.3%  ###########################-
- Vermont Avenue            85.7%  ###########################-
- Connecticut Avenue        85.7%  ###########################-
- B&O Railroad              85.7%  ###########################-
- Kentucky Avenue           85.3%  ##########################--
- Indiana Avenue            85.3%  ##########################--
- Reading Railroad          85.0%  ##########################--
- St. James Place           84.0%  ##########################--
- Illinois Avenue           84.0%  ##########################--
- Short Line                84.0%  ##########################--

## Colour group pull rate (winner)

- brown      0.88 per space
- rail       0.84 per space
- lightblue  0.86 per space
- pink       0.81 per space
- util       0.83 per space
- orange     0.83 per space
- red        0.85 per space
- yellow     0.82 per space
- green      0.82 per space
- darkblue   0.81 per space
