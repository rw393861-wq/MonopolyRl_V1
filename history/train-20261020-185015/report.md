# Monopoly self-play report

Run directory: `logs/train-20261020-185015`
Games logged: 60000
Average rounds per game: 59.8

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9943 | 16.6% |
| AI_2 | 17325 | 28.9% |
| AI_3 | 17619 | 29.4% |

## End condition

- last_standing: 59865 (99.8%)
- round_limit: 135 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 30% | 26% | 58 |
| 2 | 6000 | 17% | 33% | 26% | 59 |
| 3 | 6000 | 16% | 31% | 24% | 59 |
| 4 | 6000 | 17% | 28% | 30% | 60 |
| 5 | 6000 | 16% | 22% | 42% | 60 |
| 6 | 6000 | 16% | 24% | 39% | 60 |
| 7 | 6000 | 16% | 27% | 38% | 59 |
| 8 | 6000 | 16% | 33% | 27% | 60 |
| 9 | 6000 | 17% | 30% | 21% | 61 |
| 10 | 6000 | 18% | 31% | 20% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1325 | 0.90 |
| AI_2 | 7.9 | 14.8 | 2392 | 1.47 |
| AI_3 | 8.0 | 14.7 | 2395 | 1.48 |

## Properties most often held by the winner

- Reading Railroad          98.5%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Illinois Avenue           98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Water Works               97.9%  ############################
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
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
