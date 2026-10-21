# Monopoly self-play report

Run directory: `logs/train-20261021-190248`
Games logged: 60000
Average rounds per game: 60.0

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10165 | 16.9% |
| AI_2 | 16057 | 26.8% |
| AI_3 | 16900 | 28.2% |

## End condition

- last_standing: 59846 (99.7%)
- round_limit: 154 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 18% | 28% | 24% | 59 |
| 2 | 6000 | 17% | 27% | 28% | 58 |
| 3 | 6000 | 17% | 26% | 26% | 59 |
| 4 | 6000 | 16% | 28% | 23% | 60 |
| 5 | 6000 | 18% | 25% | 34% | 61 |
| 6 | 6000 | 17% | 22% | 34% | 62 |
| 7 | 6000 | 17% | 26% | 25% | 61 |
| 8 | 6000 | 17% | 25% | 28% | 61 |
| 9 | 6000 | 16% | 32% | 28% | 60 |
| 10 | 6000 | 17% | 30% | 32% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1346 | 0.91 |
| AI_2 | 7.3 | 13.6 | 2248 | 1.42 |
| AI_3 | 7.7 | 14.0 | 2326 | 1.46 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- New York Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.4%  ############################
- Pennsylvania Railroad     98.1%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
- Water Works               97.8%  ############################
- Indiana Avenue            97.8%  ############################

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
