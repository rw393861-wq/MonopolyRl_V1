# Monopoly self-play report

Run directory: `logs/train-20261006-195502`
Games logged: 60000
Average rounds per game: 60.2

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10382 | 17.3% |
| AI_2 | 16702 | 27.8% |
| AI_3 | 15655 | 26.1% |

## End condition

- last_standing: 59824 (99.7%)
- round_limit: 176 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 30% | 28% | 59 |
| 2 | 6000 | 17% | 27% | 32% | 59 |
| 3 | 6000 | 16% | 26% | 33% | 59 |
| 4 | 6000 | 18% | 29% | 24% | 61 |
| 5 | 6000 | 17% | 37% | 22% | 60 |
| 6 | 6000 | 18% | 27% | 26% | 60 |
| 7 | 6000 | 18% | 26% | 28% | 61 |
| 8 | 6000 | 18% | 25% | 23% | 61 |
| 9 | 6000 | 17% | 22% | 25% | 61 |
| 10 | 6000 | 17% | 30% | 21% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.8 | 9.4 | 1364 | 0.91 |
| AI_2 | 7.6 | 14.4 | 2333 | 1.50 |
| AI_3 | 7.1 | 13.8 | 2227 | 1.46 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- New York Avenue           98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.5%  ############################
- Reading Railroad          98.5%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.8%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.99 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
