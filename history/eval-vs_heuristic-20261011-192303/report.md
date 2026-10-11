# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261011-192303`
Games logged: 300
Average rounds per game: 110.6

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 18 | 6.0% |
| heuristic_1 | 146 | 48.7% |
| heuristic_2 | 136 | 45.3% |

## End condition

- last_standing: 220 (73.3%)
- round_limit: 80 (26.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 0% | 53% | 47% | 100 |
| 2 | 30 | 7% | 57% | 37% | 108 |
| 3 | 30 | 3% | 47% | 50% | 131 |
| 4 | 30 | 0% | 50% | 50% | 100 |
| 5 | 30 | 7% | 47% | 47% | 105 |
| 6 | 30 | 7% | 53% | 40% | 107 |
| 7 | 30 | 7% | 53% | 40% | 118 |
| 8 | 30 | 10% | 37% | 53% | 107 |
| 9 | 30 | 7% | 57% | 37% | 113 |
| 10 | 30 | 13% | 33% | 53% | 116 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.5 | 1.4 | 1150 | 0.00 |
| heuristic_1 | 12.9 | 17.1 | 4712 | 0.82 |
| heuristic_2 | 12.4 | 17.4 | 4352 | 0.88 |

## Properties most often held by the winner

- Water Works               86.7%  ############################
- Electric Company          86.3%  ############################
- Kentucky Avenue           86.3%  ############################
- B&O Railroad              86.3%  ############################
- Baltic Avenue             86.0%  ############################
- North Carolina Avenue     86.0%  ############################
- Ventnor Avenue            85.7%  ############################
- Short Line                85.7%  ############################
- Mediterranean Avenue      85.3%  ############################
- Tennessee Avenue          85.3%  ############################
- Reading Railroad          85.0%  ###########################-
- Pennsylvania Railroad     85.0%  ###########################-

## Colour group pull rate (winner)

- brown      0.86 per space
- rail       0.85 per space
- lightblue  0.84 per space
- pink       0.83 per space
- util       0.86 per space
- orange     0.83 per space
- red        0.83 per space
- yellow     0.82 per space
- green      0.83 per space
- darkblue   0.83 per space
