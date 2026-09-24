# Monopoly self-play report

Run directory: `logs/train-20260924-184536`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10100 | 16.8% |
| AI_2 | 16404 | 27.3% |
| AI_3 | 16784 | 28.0% |

## End condition

- last_standing: 59845 (99.7%)
- round_limit: 155 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 24% | 33% | 59 |
| 2 | 6000 | 17% | 27% | 26% | 59 |
| 3 | 6000 | 17% | 27% | 29% | 60 |
| 4 | 6000 | 17% | 29% | 30% | 61 |
| 5 | 6000 | 17% | 30% | 25% | 60 |
| 6 | 6000 | 17% | 35% | 23% | 61 |
| 7 | 6000 | 18% | 29% | 23% | 60 |
| 8 | 6000 | 16% | 26% | 34% | 61 |
| 9 | 6000 | 17% | 27% | 25% | 60 |
| 10 | 6000 | 17% | 20% | 31% | 58 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.3 | 1341 | 0.90 |
| AI_2 | 7.5 | 14.2 | 2303 | 1.47 |
| AI_3 | 7.6 | 14.1 | 2320 | 1.45 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.4%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Electric Company          98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Kentucky Avenue           97.9%  ############################
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
