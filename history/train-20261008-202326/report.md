# Monopoly self-play report

Run directory: `logs/train-20261008-202326`
Games logged: 60000
Average rounds per game: 60.2

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10156 | 16.9% |
| AI_2 | 16266 | 27.1% |
| AI_3 | 16930 | 28.2% |

## End condition

- last_standing: 59841 (99.7%)
- round_limit: 159 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 29% | 28% | 60 |
| 2 | 6000 | 17% | 29% | 25% | 60 |
| 3 | 6000 | 16% | 23% | 27% | 60 |
| 4 | 6000 | 17% | 22% | 28% | 59 |
| 5 | 6000 | 18% | 30% | 25% | 61 |
| 6 | 6000 | 17% | 29% | 27% | 60 |
| 7 | 6000 | 17% | 25% | 32% | 60 |
| 8 | 6000 | 16% | 25% | 37% | 60 |
| 9 | 6000 | 16% | 31% | 30% | 60 |
| 10 | 6000 | 16% | 27% | 25% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1334 | 0.89 |
| AI_2 | 7.4 | 14.0 | 2276 | 1.48 |
| AI_3 | 7.7 | 14.1 | 2321 | 1.44 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           97.9%  ############################
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
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
