# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20260923-185111`
Games logged: 300
Average rounds per game: 111.0

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 34 | 11.3% |
| heuristic_1 | 145 | 48.3% |
| heuristic_2 | 121 | 40.3% |

## End condition

- last_standing: 226 (75.3%)
- round_limit: 74 (24.7%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 10% | 37% | 53% | 111 |
| 2 | 30 | 13% | 50% | 37% | 127 |
| 3 | 30 | 13% | 50% | 37% | 114 |
| 4 | 30 | 10% | 53% | 37% | 100 |
| 5 | 30 | 7% | 57% | 37% | 121 |
| 6 | 30 | 13% | 50% | 37% | 106 |
| 7 | 30 | 7% | 50% | 43% | 109 |
| 8 | 30 | 20% | 53% | 27% | 123 |
| 9 | 30 | 10% | 43% | 47% | 95 |
| 10 | 30 | 10% | 40% | 50% | 105 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 2.6 | 3.0 | 1712 | 0.26 |
| heuristic_1 | 13.9 | 18.0 | 4872 | 0.60 |
| heuristic_2 | 11.3 | 14.1 | 4255 | 0.41 |

## Properties most often held by the winner

- Mediterranean Avenue      92.3%  ############################
- Baltic Avenue             92.3%  ############################
- Boardwalk                 86.3%  ##########################--
- Pennsylvania Railroad     86.0%  ##########################--
- Pacific Avenue            86.0%  ##########################--
- Reading Railroad          85.7%  ##########################--
- B&O Railroad              85.3%  ##########################--
- Pennsylvania Avenue       85.3%  ##########################--
- Vermont Avenue            84.7%  ##########################--
- Connecticut Avenue        84.7%  ##########################--
- St. James Place           84.7%  ##########################--
- Marvin Gardens            84.7%  ##########################--

## Colour group pull rate (winner)

- brown      0.92 per space
- rail       0.85 per space
- lightblue  0.84 per space
- pink       0.84 per space
- util       0.83 per space
- orange     0.83 per space
- red        0.84 per space
- yellow     0.84 per space
- green      0.85 per space
- darkblue   0.85 per space
