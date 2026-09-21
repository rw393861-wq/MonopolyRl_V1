# Monopoly self-play report

Run directory: `logs/train-20260921-194911`
Games logged: 60000
Average rounds per game: 59.6

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9493 | 15.8% |
| AI_2 | 17440 | 29.1% |
| AI_3 | 17269 | 28.8% |

## End condition

- last_standing: 59873 (99.8%)
- round_limit: 127 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 15% | 27% | 29% | 58 |
| 2 | 6000 | 16% | 25% | 33% | 57 |
| 3 | 6000 | 16% | 27% | 31% | 59 |
| 4 | 6000 | 16% | 27% | 30% | 60 |
| 5 | 6000 | 16% | 23% | 28% | 59 |
| 6 | 6000 | 16% | 19% | 33% | 61 |
| 7 | 6000 | 17% | 35% | 26% | 60 |
| 8 | 6000 | 17% | 35% | 24% | 61 |
| 9 | 6000 | 15% | 36% | 29% | 60 |
| 10 | 6000 | 15% | 36% | 25% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.4 | 8.7 | 1256 | 0.88 |
| AI_2 | 7.9 | 14.7 | 2348 | 1.45 |
| AI_3 | 7.9 | 14.0 | 2317 | 1.45 |

## Properties most often held by the winner

- Reading Railroad          98.6%  ############################
- Illinois Avenue           98.6%  ############################
- New York Avenue           98.5%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.2%  ############################
- Electric Company          98.0%  ############################
- Pennsylvania Railroad     98.0%  ############################
- Water Works               97.8%  ############################
- Vermont Avenue            97.8%  ############################
- Kentucky Avenue           97.8%  ############################

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
- darkblue   0.96 per space
