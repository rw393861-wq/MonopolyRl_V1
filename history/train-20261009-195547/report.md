# Monopoly self-play report

Run directory: `logs/train-20261009-195547`
Games logged: 60000
Average rounds per game: 59.8

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10015 | 16.7% |
| AI_2 | 15371 | 25.6% |
| AI_3 | 16907 | 28.2% |

## End condition

- last_standing: 59866 (99.8%)
- round_limit: 134 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 27% | 27% | 59 |
| 2 | 6000 | 17% | 24% | 30% | 59 |
| 3 | 6000 | 17% | 26% | 28% | 60 |
| 4 | 6000 | 17% | 28% | 28% | 61 |
| 5 | 6000 | 17% | 23% | 30% | 61 |
| 6 | 6000 | 17% | 25% | 23% | 60 |
| 7 | 6000 | 17% | 26% | 27% | 60 |
| 8 | 6000 | 16% | 26% | 37% | 60 |
| 9 | 6000 | 17% | 23% | 29% | 59 |
| 10 | 6000 | 17% | 27% | 24% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1324 | 0.90 |
| AI_2 | 7.0 | 13.2 | 2182 | 1.43 |
| AI_3 | 7.7 | 14.5 | 2333 | 1.42 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.4%  ############################
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
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
