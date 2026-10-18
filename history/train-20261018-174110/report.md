# Monopoly self-play report

Run directory: `logs/train-20261018-174110`
Games logged: 60000
Average rounds per game: 60.5

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10154 | 16.9% |
| AI_2 | 17421 | 29.0% |
| AI_3 | 17371 | 29.0% |

## End condition

- last_standing: 59831 (99.7%)
- round_limit: 169 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 28% | 25% | 59 |
| 2 | 6000 | 16% | 26% | 28% | 60 |
| 3 | 6000 | 17% | 33% | 27% | 60 |
| 4 | 6000 | 16% | 36% | 26% | 61 |
| 5 | 6000 | 17% | 30% | 29% | 61 |
| 6 | 6000 | 17% | 30% | 30% | 61 |
| 7 | 6000 | 18% | 26% | 27% | 62 |
| 8 | 6000 | 17% | 24% | 35% | 61 |
| 9 | 6000 | 16% | 23% | 34% | 61 |
| 10 | 6000 | 17% | 33% | 29% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.4 | 1350 | 0.91 |
| AI_2 | 7.9 | 15.2 | 2403 | 1.55 |
| AI_3 | 7.9 | 14.4 | 2388 | 1.45 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.9%  ############################
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
