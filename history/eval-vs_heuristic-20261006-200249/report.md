# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261006-200249`
Games logged: 300
Average rounds per game: 97.5

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 117 | 39.0% |
| heuristic_2 | 143 | 47.7% |

## End condition

- last_standing: 251 (83.7%)
- round_limit: 49 (16.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 50% | 37% | 102 |
| 2 | 30 | 20% | 37% | 43% | 96 |
| 3 | 30 | 20% | 27% | 53% | 104 |
| 4 | 30 | 13% | 53% | 33% | 82 |
| 5 | 30 | 10% | 40% | 50% | 109 |
| 6 | 30 | 20% | 27% | 53% | 90 |
| 7 | 30 | 0% | 50% | 50% | 92 |
| 8 | 30 | 13% | 33% | 53% | 96 |
| 9 | 30 | 10% | 53% | 37% | 106 |
| 10 | 30 | 13% | 20% | 67% | 98 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.3 | 3.2 | 1455 | 0.05 |
| heuristic_1 | 10.3 | 16.0 | 4072 | 0.96 |
| heuristic_2 | 13.1 | 20.4 | 4722 | 1.16 |

## Properties most often held by the winner

- Baltic Avenue             95.3%  ############################
- Mediterranean Avenue      93.0%  ###########################-
- New York Avenue           91.7%  ###########################-
- B&O Railroad              91.7%  ###########################-
- Pennsylvania Railroad     90.7%  ###########################-
- St. James Place           90.0%  ##########################--
- Water Works               90.0%  ##########################--
- St. Charles Place         89.7%  ##########################--
- Electric Company          89.7%  ##########################--
- Illinois Avenue           89.7%  ##########################--
- Pennsylvania Avenue       89.7%  ##########################--
- Oriental Avenue           89.3%  ##########################--

## Colour group pull rate (winner)

- brown      0.94 per space
- rail       0.90 per space
- lightblue  0.89 per space
- pink       0.89 per space
- util       0.90 per space
- orange     0.90 per space
- red        0.89 per space
- yellow     0.88 per space
- green      0.88 per space
- darkblue   0.86 per space
