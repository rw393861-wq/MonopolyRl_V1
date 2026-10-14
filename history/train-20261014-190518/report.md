# Monopoly self-play report

Run directory: `logs/train-20261014-190518`
Games logged: 60000
Average rounds per game: 60.6

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10245 | 17.1% |
| AI_2 | 16564 | 27.6% |
| AI_3 | 16477 | 27.5% |

## End condition

- last_standing: 59851 (99.8%)
- round_limit: 149 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 25% | 32% | 59 |
| 2 | 6000 | 17% | 31% | 28% | 60 |
| 3 | 6000 | 16% | 32% | 28% | 60 |
| 4 | 6000 | 17% | 25% | 28% | 60 |
| 5 | 6000 | 18% | 22% | 27% | 62 |
| 6 | 6000 | 18% | 30% | 23% | 61 |
| 7 | 6000 | 18% | 31% | 25% | 61 |
| 8 | 6000 | 18% | 26% | 29% | 61 |
| 9 | 6000 | 17% | 28% | 26% | 60 |
| 10 | 6000 | 17% | 26% | 29% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1345 | 0.89 |
| AI_2 | 7.5 | 14.0 | 2302 | 1.45 |
| AI_3 | 7.5 | 14.3 | 2325 | 1.49 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.7%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- New York Avenue           98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
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
