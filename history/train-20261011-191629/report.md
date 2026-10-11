# Monopoly self-play report

Run directory: `logs/train-20261011-191629`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10073 | 16.8% |
| AI_2 | 17838 | 29.7% |
| AI_3 | 16573 | 27.6% |

## End condition

- last_standing: 59833 (99.7%)
- round_limit: 167 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 29% | 27% | 59 |
| 2 | 6000 | 17% | 28% | 30% | 60 |
| 3 | 6000 | 16% | 27% | 27% | 60 |
| 4 | 6000 | 17% | 25% | 28% | 60 |
| 5 | 6000 | 17% | 25% | 36% | 61 |
| 6 | 6000 | 17% | 28% | 33% | 60 |
| 7 | 6000 | 17% | 32% | 23% | 60 |
| 8 | 6000 | 17% | 38% | 21% | 61 |
| 9 | 6000 | 17% | 35% | 25% | 60 |
| 10 | 6000 | 17% | 30% | 26% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.3 | 1343 | 0.91 |
| AI_2 | 8.1 | 14.6 | 2414 | 1.46 |
| AI_3 | 7.5 | 14.0 | 2283 | 1.46 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Electric Company          98.0%  ############################
- Indiana Avenue            97.8%  ############################
- Water Works               97.7%  ############################

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
