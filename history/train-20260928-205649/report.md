# Monopoly self-play report

Run directory: `logs/train-20260928-205649`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10126 | 16.9% |
| AI_2 | 16480 | 27.5% |
| AI_3 | 16185 | 27.0% |

## End condition

- last_standing: 59852 (99.8%)
- round_limit: 148 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 23% | 27% | 59 |
| 2 | 6000 | 17% | 28% | 26% | 60 |
| 3 | 6000 | 17% | 31% | 31% | 60 |
| 4 | 6000 | 16% | 33% | 19% | 61 |
| 5 | 6000 | 17% | 31% | 18% | 60 |
| 6 | 6000 | 17% | 22% | 25% | 61 |
| 7 | 6000 | 17% | 22% | 32% | 60 |
| 8 | 6000 | 17% | 28% | 35% | 61 |
| 9 | 6000 | 16% | 26% | 32% | 60 |
| 10 | 6000 | 16% | 30% | 24% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.1 | 1338 | 0.88 |
| AI_2 | 7.5 | 14.2 | 2298 | 1.42 |
| AI_3 | 7.4 | 13.9 | 2274 | 1.49 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.4%  ############################
- Tennessee Avenue          98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.9%  ############################
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
