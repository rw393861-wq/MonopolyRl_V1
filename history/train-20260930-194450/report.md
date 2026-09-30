# Monopoly self-play report

Run directory: `logs/train-20260930-194450`
Games logged: 60000
Average rounds per game: 60.2

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10090 | 16.8% |
| AI_2 | 17407 | 29.0% |
| AI_3 | 16016 | 26.7% |

## End condition

- last_standing: 59836 (99.7%)
- round_limit: 164 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 27% | 27% | 59 |
| 2 | 6000 | 16% | 31% | 32% | 60 |
| 3 | 6000 | 17% | 29% | 32% | 59 |
| 4 | 6000 | 16% | 26% | 27% | 60 |
| 5 | 6000 | 17% | 30% | 22% | 60 |
| 6 | 6000 | 17% | 34% | 24% | 60 |
| 7 | 6000 | 17% | 40% | 22% | 60 |
| 8 | 6000 | 18% | 29% | 28% | 61 |
| 9 | 6000 | 17% | 25% | 27% | 61 |
| 10 | 6000 | 17% | 20% | 26% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1337 | 0.90 |
| AI_2 | 7.9 | 14.5 | 2387 | 1.45 |
| AI_3 | 7.3 | 13.8 | 2266 | 1.46 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           97.9%  ############################
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
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
