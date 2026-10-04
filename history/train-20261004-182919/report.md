# Monopoly self-play report

Run directory: `logs/train-20261004-182919`
Games logged: 60000
Average rounds per game: 59.7

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10050 | 16.8% |
| AI_2 | 15856 | 26.4% |
| AI_3 | 15925 | 26.5% |

## End condition

- last_standing: 59854 (99.8%)
- round_limit: 146 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 26% | 28% | 58 |
| 2 | 6000 | 17% | 26% | 25% | 59 |
| 3 | 6000 | 16% | 25% | 32% | 60 |
| 4 | 6000 | 16% | 21% | 25% | 60 |
| 5 | 6000 | 16% | 23% | 21% | 60 |
| 6 | 6000 | 16% | 24% | 22% | 60 |
| 7 | 6000 | 16% | 31% | 28% | 60 |
| 8 | 6000 | 18% | 30% | 24% | 60 |
| 9 | 6000 | 18% | 30% | 30% | 61 |
| 10 | 6000 | 17% | 27% | 31% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1327 | 0.89 |
| AI_2 | 7.2 | 13.3 | 2218 | 1.42 |
| AI_3 | 7.2 | 13.5 | 2227 | 1.41 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.8%  ############################
- Water Works               97.8%  ############################
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
