# Monopoly self-play report

Run directory: `logs/train-20261010-190401`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9941 | 16.6% |
| AI_2 | 18557 | 30.9% |
| AI_3 | 15668 | 26.1% |

## End condition

- last_standing: 59829 (99.7%)
- round_limit: 171 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 28% | 26% | 59 |
| 2 | 6000 | 16% | 29% | 25% | 59 |
| 3 | 6000 | 16% | 29% | 29% | 60 |
| 4 | 6000 | 16% | 38% | 25% | 60 |
| 5 | 6000 | 16% | 44% | 22% | 61 |
| 6 | 6000 | 17% | 31% | 24% | 60 |
| 7 | 6000 | 17% | 23% | 33% | 61 |
| 8 | 6000 | 17% | 31% | 29% | 60 |
| 9 | 6000 | 17% | 32% | 24% | 60 |
| 10 | 6000 | 17% | 23% | 25% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1316 | 0.88 |
| AI_2 | 8.4 | 15.5 | 2501 | 1.50 |
| AI_3 | 7.1 | 13.3 | 2207 | 1.43 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- New York Avenue           98.3%  ############################
- St. James Place           98.2%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Water Works               98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Indiana Avenue            97.8%  ############################

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
