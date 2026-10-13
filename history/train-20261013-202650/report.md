# Monopoly self-play report

Run directory: `logs/train-20261013-202650`
Games logged: 60000
Average rounds per game: 60.4

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10153 | 16.9% |
| AI_2 | 16757 | 27.9% |
| AI_3 | 15839 | 26.4% |

## End condition

- last_standing: 59830 (99.7%)
- round_limit: 170 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 27% | 24% | 58 |
| 2 | 6000 | 16% | 26% | 27% | 59 |
| 3 | 6000 | 16% | 24% | 27% | 59 |
| 4 | 6000 | 16% | 22% | 28% | 60 |
| 5 | 6000 | 17% | 31% | 28% | 62 |
| 6 | 6000 | 17% | 38% | 24% | 62 |
| 7 | 6000 | 18% | 30% | 24% | 61 |
| 8 | 6000 | 18% | 23% | 25% | 62 |
| 9 | 6000 | 17% | 31% | 25% | 61 |
| 10 | 6000 | 17% | 29% | 32% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1346 | 0.89 |
| AI_2 | 7.6 | 14.2 | 2349 | 1.46 |
| AI_3 | 7.2 | 13.7 | 2243 | 1.44 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Water Works               97.9%  ############################

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
