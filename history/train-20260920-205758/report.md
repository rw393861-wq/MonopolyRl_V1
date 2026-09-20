# Monopoly self-play report

Run directory: `logs/train-20260920-205758`
Games logged: 5000
Average rounds per game: 59.2

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 780 | 15.6% |
| AI_2 | 1535 | 30.7% |
| AI_3 | 1217 | 24.3% |

## End condition

- last_standing: 4993 (99.9%)
- round_limit: 7 (0.1%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 500 | 15% | 26% | 26% | 59 |
| 2 | 500 | 18% | 33% | 22% | 58 |
| 3 | 500 | 16% | 31% | 21% | 58 |
| 4 | 500 | 14% | 31% | 25% | 59 |
| 5 | 500 | 13% | 36% | 24% | 59 |
| 6 | 500 | 14% | 34% | 25% | 59 |
| 7 | 500 | 18% | 25% | 24% | 62 |
| 8 | 500 | 16% | 34% | 22% | 59 |
| 9 | 500 | 15% | 32% | 25% | 59 |
| 10 | 500 | 18% | 26% | 30% | 61 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.3 | 8.5 | 1230 | 0.88 |
| AI_2 | 8.4 | 14.6 | 2401 | 1.49 |
| AI_3 | 6.7 | 12.0 | 2015 | 1.33 |

## Properties most often held by the winner

- Reading Railroad          98.7%  ############################
- New York Avenue           98.6%  ############################
- St. Charles Place         98.4%  ############################
- Illinois Avenue           98.3%  ############################
- Water Works               98.3%  ############################
- Electric Company          98.3%  ############################
- Tennessee Avenue          98.3%  ############################
- St. James Place           98.3%  ############################
- Kentucky Avenue           98.2%  ############################
- B&O Railroad              98.1%  ############################
- Pennsylvania Railroad     97.9%  ############################
- Vermont Avenue            97.8%  ############################

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
