# Monopoly self-play report

Run directory: `logs/eval-vs_heuristic-20261010-191555`
Games logged: 300
Average rounds per game: 99.8

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 40 | 13.3% |
| heuristic_1 | 118 | 39.3% |
| heuristic_2 | 142 | 47.3% |

## End condition

- round_limit: 57 (19.0%)
- last_standing: 243 (81.0%)

## Win rate over training windows

| window | games | AI_1 | heuristic_1 | heuristic_2 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 3% | 47% | 50% | 97 |
| 2 | 30 | 3% | 47% | 50% | 112 |
| 3 | 30 | 20% | 50% | 30% | 111 |
| 4 | 30 | 13% | 57% | 30% | 98 |
| 5 | 30 | 17% | 30% | 53% | 90 |
| 6 | 30 | 20% | 20% | 60% | 106 |
| 7 | 30 | 10% | 33% | 57% | 83 |
| 8 | 30 | 20% | 40% | 40% | 107 |
| 9 | 30 | 17% | 37% | 47% | 93 |
| 10 | 30 | 10% | 33% | 57% | 100 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.4 | 4.1 | 1816 | 0.19 |
| heuristic_1 | 10.6 | 16.5 | 4207 | 1.00 |
| heuristic_2 | 12.8 | 18.7 | 4591 | 1.14 |

## Properties most often held by the winner

- Baltic Avenue             90.3%  ############################
- Mediterranean Avenue      90.3%  ############################
- Pennsylvania Railroad     90.3%  ############################
- Water Works               89.7%  ############################
- Reading Railroad          89.3%  ############################
- Virginia Avenue           89.3%  ############################
- Electric Company          89.0%  ############################
- St. James Place           89.0%  ############################
- Marvin Gardens            89.0%  ############################
- Short Line                89.0%  ############################
- North Carolina Avenue     89.0%  ############################
- Illinois Avenue           88.7%  ###########################-

## Colour group pull rate (winner)

- brown      0.90 per space
- rail       0.89 per space
- lightblue  0.86 per space
- pink       0.87 per space
- util       0.89 per space
- orange     0.88 per space
- red        0.87 per space
- yellow     0.88 per space
- green      0.88 per space
- darkblue   0.87 per space
