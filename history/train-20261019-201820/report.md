# Monopoly self-play report

Run directory: `logs/train-20261019-201820`
Games logged: 60000
Average rounds per game: 59.8

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9951 | 16.6% |
| AI_2 | 15168 | 25.3% |
| AI_3 | 16088 | 26.8% |

## End condition

- last_standing: 59829 (99.7%)
- round_limit: 171 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 28% | 26% | 59 |
| 2 | 6000 | 16% | 27% | 26% | 60 |
| 3 | 6000 | 16% | 20% | 32% | 59 |
| 4 | 6000 | 17% | 31% | 30% | 60 |
| 5 | 6000 | 17% | 31% | 24% | 60 |
| 6 | 6000 | 18% | 31% | 27% | 61 |
| 7 | 6000 | 17% | 24% | 34% | 60 |
| 8 | 6000 | 17% | 22% | 24% | 60 |
| 9 | 6000 | 16% | 19% | 20% | 59 |
| 10 | 6000 | 15% | 20% | 24% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1327 | 0.89 |
| AI_2 | 6.9 | 13.2 | 2171 | 1.43 |
| AI_3 | 7.3 | 13.3 | 2238 | 1.40 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.3%  ############################
- St. James Place           98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.8%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.96 per space
