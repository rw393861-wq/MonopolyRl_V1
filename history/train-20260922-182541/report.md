# Monopoly self-play report

Run directory: `logs/train-20260922-182541`
Games logged: 60000
Average rounds per game: 59.6

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9885 | 16.5% |
| AI_2 | 16767 | 27.9% |
| AI_3 | 15250 | 25.4% |

## End condition

- last_standing: 59852 (99.8%)
- round_limit: 148 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 34% | 23% | 59 |
| 2 | 6000 | 17% | 26% | 24% | 59 |
| 3 | 6000 | 16% | 26% | 25% | 59 |
| 4 | 6000 | 16% | 27% | 22% | 60 |
| 5 | 6000 | 16% | 20% | 29% | 59 |
| 6 | 6000 | 17% | 25% | 23% | 60 |
| 7 | 6000 | 17% | 31% | 27% | 60 |
| 8 | 6000 | 17% | 34% | 27% | 60 |
| 9 | 6000 | 16% | 29% | 26% | 60 |
| 10 | 6000 | 17% | 28% | 29% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.5 | 9.1 | 1316 | 0.89 |
| AI_2 | 7.6 | 14.2 | 2317 | 1.47 |
| AI_3 | 6.9 | 12.7 | 2135 | 1.37 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.6%  ############################
- New York Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Water Works               97.8%  ############################

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
