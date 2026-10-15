# Monopoly self-play report

Run directory: `logs/train-20261015-184709`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9995 | 16.7% |
| AI_2 | 18167 | 30.3% |
| AI_3 | 15793 | 26.3% |

## End condition

- last_standing: 59830 (99.7%)
- round_limit: 170 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 33% | 26% | 59 |
| 2 | 6000 | 16% | 30% | 26% | 59 |
| 3 | 6000 | 16% | 29% | 24% | 60 |
| 4 | 6000 | 16% | 33% | 29% | 61 |
| 5 | 6000 | 17% | 36% | 20% | 60 |
| 6 | 6000 | 16% | 39% | 22% | 60 |
| 7 | 6000 | 17% | 25% | 30% | 60 |
| 8 | 6000 | 17% | 25% | 26% | 60 |
| 9 | 6000 | 17% | 31% | 27% | 60 |
| 10 | 6000 | 17% | 23% | 34% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1326 | 0.89 |
| AI_2 | 8.3 | 15.5 | 2464 | 1.49 |
| AI_3 | 7.2 | 13.1 | 2209 | 1.42 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.4%  ############################
- Tennessee Avenue          98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Electric Company          98.0%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.9%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
