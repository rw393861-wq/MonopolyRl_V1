# Monopoly self-play report

Run directory: `logs/train-20260925-190259`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10039 | 16.7% |
| AI_2 | 17167 | 28.6% |
| AI_3 | 15695 | 26.2% |

## End condition

- last_standing: 59840 (99.7%)
- round_limit: 160 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 24% | 33% | 59 |
| 2 | 6000 | 16% | 27% | 29% | 59 |
| 3 | 6000 | 16% | 32% | 28% | 60 |
| 4 | 6000 | 16% | 25% | 26% | 60 |
| 5 | 6000 | 17% | 27% | 21% | 61 |
| 6 | 6000 | 18% | 34% | 20% | 60 |
| 7 | 6000 | 16% | 38% | 22% | 60 |
| 8 | 6000 | 17% | 30% | 27% | 60 |
| 9 | 6000 | 17% | 24% | 27% | 61 |
| 10 | 6000 | 16% | 25% | 29% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1333 | 0.90 |
| AI_2 | 7.8 | 14.0 | 2338 | 1.45 |
| AI_3 | 7.1 | 13.5 | 2214 | 1.43 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Kentucky Avenue           98.0%  ############################
- Indiana Avenue            97.9%  ############################
- Water Works               97.9%  ############################

## Colour group pull rate (winner)

- brown      0.95 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
