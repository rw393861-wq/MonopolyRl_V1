# Monopoly self-play report

Run directory: `logs/train-20261012-221932`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10043 | 16.7% |
| AI_2 | 16010 | 26.7% |
| AI_3 | 17414 | 29.0% |

## End condition

- last_standing: 59819 (99.7%)
- round_limit: 181 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 28% | 27% | 59 |
| 2 | 6000 | 17% | 26% | 29% | 59 |
| 3 | 6000 | 16% | 22% | 27% | 60 |
| 4 | 6000 | 16% | 23% | 34% | 59 |
| 5 | 6000 | 17% | 30% | 29% | 61 |
| 6 | 6000 | 18% | 28% | 31% | 61 |
| 7 | 6000 | 18% | 23% | 34% | 60 |
| 8 | 6000 | 17% | 29% | 32% | 61 |
| 9 | 6000 | 16% | 28% | 27% | 61 |
| 10 | 6000 | 16% | 29% | 21% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1340 | 0.90 |
| AI_2 | 7.3 | 13.8 | 2264 | 1.49 |
| AI_3 | 7.9 | 14.8 | 2385 | 1.49 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.4%  ############################
- Tennessee Avenue          98.4%  ############################
- B&O Railroad              98.3%  ############################
- St. James Place           98.2%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
- Water Works               97.8%  ############################
- Vermont Avenue            97.8%  ############################

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
