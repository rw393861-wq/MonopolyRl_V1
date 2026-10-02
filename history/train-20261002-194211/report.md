# Monopoly self-play report

Run directory: `logs/train-20261002-194211`
Games logged: 60000
Average rounds per game: 59.7

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10016 | 16.7% |
| AI_2 | 16800 | 28.0% |
| AI_3 | 17843 | 29.7% |

## End condition

- last_standing: 59854 (99.8%)
- round_limit: 146 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 24% | 31% | 59 |
| 2 | 6000 | 17% | 27% | 24% | 59 |
| 3 | 6000 | 16% | 30% | 29% | 60 |
| 4 | 6000 | 17% | 34% | 23% | 59 |
| 5 | 6000 | 16% | 44% | 20% | 59 |
| 6 | 6000 | 17% | 31% | 26% | 60 |
| 7 | 6000 | 18% | 25% | 26% | 61 |
| 8 | 6000 | 17% | 22% | 37% | 61 |
| 9 | 6000 | 16% | 23% | 39% | 61 |
| 10 | 6000 | 16% | 20% | 43% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1326 | 0.89 |
| AI_2 | 7.7 | 14.1 | 2297 | 1.45 |
| AI_3 | 8.1 | 15.1 | 2450 | 1.47 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               98.0%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
