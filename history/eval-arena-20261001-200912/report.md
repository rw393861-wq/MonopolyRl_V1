# Monopoly self-play report

Run directory: `logs/eval-arena-20261001-200912`
Games logged: 300
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| AI_1 | 52 | 17.3% |
| random_1 | 79 | 26.3% |
| heuristic_1 | 169 | 56.3% |

## End condition

- last_standing: 299 (99.7%)
- round_limit: 1 (0.3%)

## Win rate over training windows

| window | games | AI_1 | random_1 | heuristic_1 | avg rounds |
|---|---|---|---|---|---|
| 1 | 30 | 23% | 40% | 37% | 64 |
| 2 | 30 | 17% | 17% | 67% | 57 |
| 3 | 30 | 20% | 37% | 43% | 56 |
| 4 | 30 | 20% | 10% | 70% | 62 |
| 5 | 30 | 10% | 23% | 67% | 64 |
| 6 | 30 | 20% | 30% | 50% | 62 |
| 7 | 30 | 13% | 37% | 50% | 55 |
| 8 | 30 | 17% | 27% | 57% | 69 |
| 9 | 30 | 23% | 13% | 63% | 54 |
| 10 | 30 | 10% | 30% | 60% | 62 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| AI_1 | 4.6 | 6.9 | 1455 | 0.68 |
| random_1 | 7.1 | 15.8 | 2686 | 1.44 |
| heuristic_1 | 15.5 | 30.2 | 4400 | 2.62 |

## Properties most often held by the winner

- Pennsylvania Railroad     99.0%  ############################
- Electric Company          98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- Illinois Avenue           98.3%  ############################
- Marvin Gardens            98.3%  ############################
- Vermont Avenue            98.0%  ############################
- St. Charles Place         98.0%  ############################
- New York Avenue           98.0%  ############################
- Indiana Avenue            98.0%  ############################
- Ventnor Avenue            98.0%  ############################
- Oriental Avenue           97.7%  ############################
- St. James Place           97.7%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.97 per space
- lightblue  0.97 per space
- pink       0.97 per space
- util       0.97 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.96 per space
