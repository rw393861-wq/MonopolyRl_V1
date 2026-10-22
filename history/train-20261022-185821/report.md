# Monopoly self-play report

Run directory: `logs/train-20261022-185821`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10082 | 16.8% |
| AI_2 | 17124 | 28.5% |
| AI_3 | 16413 | 27.4% |

## End condition

- last_standing: 59859 (99.8%)
- round_limit: 141 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 31% | 27% | 58 |
| 2 | 6000 | 16% | 29% | 27% | 59 |
| 3 | 6000 | 17% | 31% | 24% | 60 |
| 4 | 6000 | 17% | 31% | 25% | 60 |
| 5 | 6000 | 18% | 30% | 26% | 62 |
| 6 | 6000 | 18% | 31% | 27% | 61 |
| 7 | 6000 | 17% | 22% | 35% | 61 |
| 8 | 6000 | 17% | 24% | 35% | 61 |
| 9 | 6000 | 16% | 31% | 26% | 61 |
| 10 | 6000 | 16% | 25% | 22% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.4 | 1337 | 0.90 |
| AI_2 | 7.8 | 14.1 | 2362 | 1.41 |
| AI_3 | 7.5 | 13.9 | 2282 | 1.45 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.5%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.4%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

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
