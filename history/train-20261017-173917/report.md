# Monopoly self-play report

Run directory: `logs/train-20261017-173917`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10241 | 17.1% |
| AI_2 | 16199 | 27.0% |
| AI_3 | 15706 | 26.2% |

## End condition

- last_standing: 59848 (99.7%)
- round_limit: 152 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 32% | 25% | 59 |
| 2 | 6000 | 18% | 30% | 25% | 60 |
| 3 | 6000 | 17% | 30% | 27% | 61 |
| 4 | 6000 | 17% | 27% | 35% | 60 |
| 5 | 6000 | 18% | 29% | 26% | 60 |
| 6 | 6000 | 19% | 25% | 28% | 62 |
| 7 | 6000 | 17% | 28% | 24% | 61 |
| 8 | 6000 | 17% | 22% | 29% | 61 |
| 9 | 6000 | 15% | 20% | 24% | 59 |
| 10 | 6000 | 16% | 27% | 19% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.3 | 1346 | 0.91 |
| AI_2 | 7.4 | 13.8 | 2281 | 1.41 |
| AI_3 | 7.2 | 13.6 | 2233 | 1.48 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.7%  ############################
- St. Charles Place         98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- New York Avenue           98.4%  ############################
- St. James Place           98.4%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Kentucky Avenue           98.1%  ############################
- Electric Company          98.0%  ############################
- Water Works               98.0%  ############################
- Indiana Avenue            97.9%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.98 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.98 per space
- green      0.97 per space
- darkblue   0.97 per space
