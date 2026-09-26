# Monopoly self-play report

Run directory: `logs/train-20260926-181045`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9817 | 16.4% |
| AI_2 | 17553 | 29.3% |
| AI_3 | 18242 | 30.4% |

## End condition

- last_standing: 59854 (99.8%)
- round_limit: 146 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 17% | 26% | 31% | 60 |
| 2 | 6000 | 17% | 29% | 27% | 59 |
| 3 | 6000 | 17% | 22% | 34% | 60 |
| 4 | 6000 | 16% | 29% | 31% | 60 |
| 5 | 6000 | 16% | 27% | 38% | 61 |
| 6 | 6000 | 17% | 19% | 45% | 61 |
| 7 | 6000 | 16% | 24% | 35% | 61 |
| 8 | 6000 | 18% | 33% | 23% | 60 |
| 9 | 6000 | 14% | 40% | 20% | 60 |
| 10 | 6000 | 16% | 43% | 20% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.5 | 9.1 | 1321 | 0.90 |
| AI_2 | 8.0 | 14.6 | 2409 | 1.44 |
| AI_3 | 8.3 | 15.1 | 2470 | 1.47 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.5%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.1%  ############################
- Kentucky Avenue           98.0%  ############################
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
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
