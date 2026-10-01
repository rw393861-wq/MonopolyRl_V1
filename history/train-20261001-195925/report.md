# Monopoly self-play report

Run directory: `logs/train-20261001-195925`
Games logged: 60000
Average rounds per game: 60.3

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10173 | 17.0% |
| AI_2 | 15562 | 25.9% |
| AI_3 | 17500 | 29.2% |

## End condition

- last_standing: 59840 (99.7%)
- round_limit: 160 (0.3%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 25% | 27% | 59 |
| 2 | 6000 | 17% | 25% | 29% | 59 |
| 3 | 6000 | 16% | 29% | 30% | 60 |
| 4 | 6000 | 17% | 29% | 26% | 61 |
| 5 | 6000 | 17% | 26% | 28% | 61 |
| 6 | 6000 | 18% | 24% | 26% | 61 |
| 7 | 6000 | 17% | 25% | 28% | 61 |
| 8 | 6000 | 17% | 29% | 28% | 61 |
| 9 | 6000 | 17% | 25% | 35% | 60 |
| 10 | 6000 | 17% | 23% | 34% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.7 | 9.2 | 1335 | 0.88 |
| AI_2 | 7.1 | 13.5 | 2199 | 1.45 |
| AI_3 | 8.0 | 15.2 | 2419 | 1.52 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- St. Charles Place         98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- B&O Railroad              98.4%  ############################
- St. James Place           98.3%  ############################
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
