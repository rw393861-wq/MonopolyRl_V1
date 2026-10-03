# Monopoly self-play report

Run directory: `logs/train-20261003-182727`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10350 | 17.2% |
| AI_2 | 18422 | 30.7% |
| AI_3 | 16387 | 27.3% |

## End condition

- last_standing: 59814 (99.7%)
- round_limit: 186 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 27% | 31% | 59 |
| 2 | 6000 | 16% | 32% | 24% | 59 |
| 3 | 6000 | 16% | 30% | 23% | 60 |
| 4 | 6000 | 17% | 29% | 29% | 60 |
| 5 | 6000 | 18% | 32% | 27% | 62 |
| 6 | 6000 | 16% | 40% | 20% | 61 |
| 7 | 6000 | 18% | 32% | 27% | 62 |
| 8 | 6000 | 19% | 31% | 27% | 61 |
| 9 | 6000 | 17% | 26% | 32% | 60 |
| 10 | 6000 | 17% | 28% | 32% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.8 | 9.4 | 1363 | 0.89 |
| AI_2 | 8.4 | 15.7 | 2510 | 1.52 |
| AI_3 | 7.5 | 13.8 | 2296 | 1.40 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Water Works               97.9%  ############################

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
