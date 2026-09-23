# Monopoly self-play report

Run directory: `logs/train-20260923-184439`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10134 | 16.9% |
| AI_2 | 17459 | 29.1% |
| AI_3 | 16998 | 28.3% |

## End condition

- last_standing: 59848 (99.7%)
- round_limit: 152 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 23% | 35% | 59 |
| 2 | 6000 | 17% | 29% | 30% | 59 |
| 3 | 6000 | 17% | 29% | 27% | 60 |
| 4 | 6000 | 16% | 26% | 26% | 60 |
| 5 | 6000 | 18% | 24% | 32% | 61 |
| 6 | 6000 | 17% | 33% | 27% | 60 |
| 7 | 6000 | 17% | 31% | 25% | 60 |
| 8 | 6000 | 17% | 27% | 26% | 60 |
| 9 | 6000 | 16% | 36% | 26% | 60 |
| 10 | 6000 | 17% | 33% | 30% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1347 | 0.90 |
| AI_2 | 7.9 | 14.8 | 2390 | 1.51 |
| AI_3 | 7.7 | 14.3 | 2351 | 1.45 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- New York Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            97.8%  ############################
- Water Works               97.8%  ############################

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
