# Monopoly self-play report

Run directory: `logs/train-20261024-174344`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9832 | 16.4% |
| AI_2 | 17284 | 28.8% |
| AI_3 | 16656 | 27.8% |

## End condition

- last_standing: 59847 (99.7%)
- round_limit: 153 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 29% | 24% | 59 |
| 2 | 6000 | 17% | 27% | 27% | 59 |
| 3 | 6000 | 16% | 29% | 28% | 60 |
| 4 | 6000 | 16% | 34% | 27% | 60 |
| 5 | 6000 | 17% | 39% | 23% | 60 |
| 6 | 6000 | 16% | 37% | 22% | 61 |
| 7 | 6000 | 17% | 28% | 32% | 60 |
| 8 | 6000 | 16% | 22% | 32% | 60 |
| 9 | 6000 | 16% | 23% | 29% | 60 |
| 10 | 6000 | 17% | 20% | 33% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.5 | 9.1 | 1310 | 0.90 |
| AI_2 | 7.9 | 14.6 | 2375 | 1.47 |
| AI_3 | 7.6 | 14.0 | 2303 | 1.45 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.8%  ############################
- Kentucky Avenue           97.8%  ############################
- Vermont Avenue            97.7%  ############################

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
- darkblue   0.96 per space
