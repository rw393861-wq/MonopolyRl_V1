# Monopoly self-play report

Run directory: `logs/train-20261007-202034`
Games logged: 60000
Average rounds per game: 60.2

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10316 | 17.2% |
| AI_2 | 17131 | 28.6% |
| AI_3 | 17279 | 28.8% |

## End condition

- last_standing: 59832 (99.7%)
- round_limit: 168 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 31% | 24% | 59 |
| 2 | 6000 | 17% | 26% | 31% | 59 |
| 3 | 6000 | 16% | 28% | 31% | 60 |
| 4 | 6000 | 17% | 31% | 29% | 60 |
| 5 | 6000 | 17% | 30% | 32% | 61 |
| 6 | 6000 | 17% | 25% | 35% | 60 |
| 7 | 6000 | 17% | 25% | 30% | 61 |
| 8 | 6000 | 18% | 31% | 23% | 61 |
| 9 | 6000 | 17% | 31% | 23% | 60 |
| 10 | 6000 | 18% | 28% | 30% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.4 | 1358 | 0.90 |
| AI_2 | 7.8 | 14.2 | 2345 | 1.47 |
| AI_3 | 7.9 | 14.8 | 2390 | 1.48 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Electric Company          98.0%  ############################
- Indiana Avenue            97.9%  ############################
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
