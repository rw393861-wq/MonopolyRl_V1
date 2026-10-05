# Monopoly self-play report

Run directory: `logs/train-20261005-214408`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10203 | 17.0% |
| AI_2 | 16870 | 28.1% |
| AI_3 | 16502 | 27.5% |

## End condition

- last_standing: 59856 (99.8%)
- round_limit: 144 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 29% | 29% | 58 |
| 2 | 6000 | 17% | 28% | 32% | 60 |
| 3 | 6000 | 16% | 32% | 30% | 60 |
| 4 | 6000 | 16% | 30% | 22% | 59 |
| 5 | 6000 | 18% | 28% | 23% | 60 |
| 6 | 6000 | 17% | 24% | 28% | 62 |
| 7 | 6000 | 17% | 27% | 30% | 61 |
| 8 | 6000 | 17% | 20% | 31% | 60 |
| 9 | 6000 | 17% | 28% | 28% | 60 |
| 10 | 6000 | 18% | 34% | 23% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1349 | 0.90 |
| AI_2 | 7.7 | 14.3 | 2313 | 1.48 |
| AI_3 | 7.5 | 14.1 | 2310 | 1.44 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.5%  ############################
- B&O Railroad              98.3%  ############################
- Electric Company          98.1%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Water Works               98.0%  ############################
- Kentucky Avenue           98.0%  ############################
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
