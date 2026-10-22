# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261022-191013`
Games logged: 300
Average rounds per game: 104.7

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 35 | 11.7% |
| heuristic_1 | 137 | 45.7% |
| heuristic_2 | 128 | 42.7% |

## End condition

- last_standing: 229 (76.3%)
- round_limit: 71 (23.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 17% | 43% | 40% | 89 |
| 2 | 30 | 10% | 60% | 30% | 106 |
| 3 | 30 | 10% | 57% | 33% | 108 |
| 4 | 30 | 10% | 40% | 50% | 99 |
| 5 | 30 | 13% | 37% | 50% | 89 |
| 6 | 30 | 17% | 27% | 57% | 108 |
| 7 | 30 | 13% | 43% | 43% | 110 |
| 8 | 30 | 3% | 60% | 37% | 120 |
| 9 | 30 | 17% | 37% | 47% | 106 |
| 10 | 30 | 7% | 53% | 40% | 111 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.6 | 4.2 | 1747 | 0.27 |
| heuristic_1 | 11.5 | 15.9 | 4440 | 1.04 |
| heuristic_2 | 11.8 | 15.9 | 4212 | 0.97 |

## Properties most often held by the winner

- Baltic Avenue             91.0%  ############################
- Mediterranean Avenue      90.7%  ############################
- Short Line                88.0%  ###########################-
- North Carolina Avenue     87.3%  ###########################-
- Pennsylvania Railroad     87.0%  ###########################-
- Illinois Avenue           87.0%  ###########################-
- Water Works               86.7%  ###########################-
- Atlantic Avenue           86.3%  ###########################-
- Reading Railroad          86.0%  ##########################--
- St. Charles Place         86.0%  ##########################--
- B&O Railroad              86.0%  ##########################--
- Marvin Gardens            85.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.91 per space
- rail       0.87 per space
- lightblue  0.85 per space
- pink       0.85 per space
- util       0.85 per space
- orange     0.84 per space
- red        0.85 per space
- yellow     0.86 per space
- green      0.84 per space
- darkblue   0.85 per space
