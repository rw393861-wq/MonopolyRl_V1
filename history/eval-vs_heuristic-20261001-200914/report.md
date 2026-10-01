# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261001-200914`
Games logged: 300
Average rounds per game: 106.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 32 | 10.7% |
| heuristic_1 | 130 | 43.3% |
| heuristic_2 | 138 | 46.0% |

## End condition

- round_limit: 77 (25.7%)
- last_standing: 223 (74.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 33% | 57% | 101 |
| 2 | 30 | 10% | 37% | 53% | 106 |
| 3 | 30 | 7% | 37% | 57% | 114 |
| 4 | 30 | 17% | 50% | 33% | 96 |
| 5 | 30 | 10% | 43% | 47% | 97 |
| 6 | 30 | 3% | 50% | 47% | 115 |
| 7 | 30 | 7% | 57% | 37% | 100 |
| 8 | 30 | 20% | 47% | 33% | 110 |
| 9 | 30 | 10% | 37% | 53% | 113 |
| 10 | 30 | 13% | 43% | 43% | 112 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 3.7 | 2.9 | 1270 | 0.07 |
| heuristic_1 | 11.7 | 16.2 | 4742 | 0.74 |
| heuristic_2 | 12.3 | 14.9 | 4653 | 0.73 |

## Properties most often held by the winner

- Baltic Avenue             92.0%  ############################
- B&O Railroad              90.3%  ###########################-
- Mediterranean Avenue      90.0%  ###########################-
- North Carolina Avenue     89.7%  ###########################-
- Short Line                87.0%  ##########################--
- Oriental Avenue           87.0%  ##########################--
- Pennsylvania Railroad     86.3%  ##########################--
- Reading Railroad          86.0%  ##########################--
- Tennessee Avenue          85.7%  ##########################--
- Connecticut Avenue        85.3%  ##########################--
- St. James Place           85.3%  ##########################--
- New York Avenue           85.3%  ##########################--

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.87 per space
- lightblue  0.85 per space
- pink       0.84 per space
- util       0.83 per space
- orange     0.85 per space
- red        0.83 per space
- yellow     0.82 per space
- green      0.85 per space
- darkblue   0.81 per space
