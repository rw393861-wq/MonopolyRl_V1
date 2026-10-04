# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261004-184103`
Games logged: 300
Average rounds per game: 108.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 45 | 15.0% |
| heuristic_1 | 136 | 45.3% |
| heuristic_2 | 119 | 39.7% |

## End condition

- last_standing: 221 (73.7%)
- round_limit: 79 (26.3%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 13% | 50% | 37% | 110 |
| 2 | 30 | 20% | 43% | 37% | 113 |
| 3 | 30 | 13% | 40% | 47% | 100 |
| 4 | 30 | 13% | 53% | 33% | 133 |
| 5 | 30 | 17% | 30% | 53% | 104 |
| 6 | 30 | 3% | 63% | 33% | 100 |
| 7 | 30 | 13% | 47% | 40% | 105 |
| 8 | 30 | 27% | 37% | 37% | 102 |
| 9 | 30 | 13% | 40% | 47% | 111 |
| 10 | 30 | 17% | 50% | 33% | 109 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 5.1 | 3.2 | 1731 | 0.03 |
| heuristic_1 | 11.7 | 15.2 | 4210 | 0.66 |
| heuristic_2 | 11.1 | 15.9 | 4299 | 0.66 |

## Properties most often held by the winner

- Baltic Avenue             90.7%  ############################
- Mediterranean Avenue      87.3%  ###########################-
- States Avenue             87.3%  ###########################-
- Reading Railroad          86.3%  ###########################-
- Virginia Avenue           86.3%  ###########################-
- Oriental Avenue           85.7%  ##########################--
- St. Charles Place         85.3%  ##########################--
- Vermont Avenue            85.0%  ##########################--
- Ventnor Avenue            85.0%  ##########################--
- North Carolina Avenue     85.0%  ##########################--
- Connecticut Avenue        84.7%  ##########################--
- Tennessee Avenue          84.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.89 per space
- rail       0.84 per space
- lightblue  0.85 per space
- pink       0.86 per space
- util       0.84 per space
- orange     0.84 per space
- red        0.84 per space
- yellow     0.84 per space
- green      0.81 per space
- darkblue   0.83 per space
