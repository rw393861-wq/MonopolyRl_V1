# Monopoly self-play report

Run directory: `logs/train-20261023-184827`
Games logged: 60000
Average rounds per game: 59.7

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9948 | 16.6% |
| AI_2 | 15879 | 26.5% |
| AI_3 | 17215 | 28.7% |

## End condition

- last_standing: 59875 (99.8%)
- round_limit: 125 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 24% | 25% | 59 |
| 2 | 6000 | 16% | 36% | 24% | 59 |
| 3 | 6000 | 16% | 29% | 26% | 59 |
| 4 | 6000 | 16% | 25% | 24% | 61 |
| 5 | 6000 | 18% | 21% | 29% | 61 |
| 6 | 6000 | 18% | 24% | 34% | 60 |
| 7 | 6000 | 17% | 32% | 32% | 60 |
| 8 | 6000 | 16% | 32% | 31% | 60 |
| 9 | 6000 | 16% | 21% | 33% | 60 |
| 10 | 6000 | 16% | 22% | 29% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1314 | 0.89 |
| AI_2 | 7.2 | 13.6 | 2209 | 1.45 |
| AI_3 | 7.8 | 14.7 | 2361 | 1.49 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- New York Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.2%  ############################
- Electric Company          98.1%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.9%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
