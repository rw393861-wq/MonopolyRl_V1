# Monopoly self-play report

Run directory: `logs/train-20261016-183221`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10141 | 16.9% |
| AI_2 | 18245 | 30.4% |
| AI_3 | 16038 | 26.7% |

## End condition

- last_standing: 59848 (99.7%)
- round_limit: 152 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 32% | 27% | 59 |
| 2 | 6000 | 17% | 33% | 25% | 60 |
| 3 | 6000 | 16% | 32% | 25% | 60 |
| 4 | 6000 | 17% | 37% | 22% | 60 |
| 5 | 6000 | 18% | 25% | 28% | 61 |
| 6 | 6000 | 17% | 26% | 29% | 60 |
| 7 | 6000 | 16% | 25% | 30% | 61 |
| 8 | 6000 | 17% | 27% | 31% | 61 |
| 9 | 6000 | 17% | 30% | 29% | 60 |
| 10 | 6000 | 17% | 38% | 23% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1348 | 0.91 |
| AI_2 | 8.3 | 15.5 | 2462 | 1.52 |
| AI_3 | 7.3 | 13.5 | 2251 | 1.44 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.6%  ############################
- Tennessee Avenue          98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.9%  ############################
- Indiana Avenue            97.9%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
