# Monopoly self-play report

Run directory: `logs/train-20260927-184714`
Games logged: 60000
Average rounds per game: 59.9

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 10025 | 16.7% |
| AI_2 | 15467 | 25.8% |
| AI_3 | 16443 | 27.4% |

## End condition

- last_standing: 59854 (99.8%)
- round_limit: 146 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 30% | 27% | 59 |
| 2 | 6000 | 17% | 26% | 28% | 59 |
| 3 | 6000 | 16% | 24% | 26% | 59 |
| 4 | 6000 | 16% | 28% | 27% | 60 |
| 5 | 6000 | 18% | 25% | 28% | 61 |
| 6 | 6000 | 17% | 26% | 23% | 61 |
| 7 | 6000 | 17% | 21% | 31% | 60 |
| 8 | 6000 | 18% | 22% | 39% | 60 |
| 9 | 6000 | 16% | 29% | 25% | 61 |
| 10 | 6000 | 16% | 27% | 20% | 59 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.2 | 1330 | 0.90 |
| AI_2 | 7.0 | 13.4 | 2193 | 1.41 |
| AI_3 | 7.5 | 14.0 | 2280 | 1.48 |

## Properties most often held by the winner

- Illinois Avenue           98.7%  ############################
- Reading Railroad          98.7%  ############################
- New York Avenue           98.5%  ############################
- St. Charles Place         98.4%  ############################
- Tennessee Avenue          98.4%  ############################
- B&O Railroad              98.3%  ############################
- St. James Place           98.2%  ############################
- Pennsylvania Railroad     98.2%  ############################
- Electric Company          98.0%  ############################
- Water Works               97.9%  ############################
- Kentucky Avenue           97.9%  ############################
- Indiana Avenue            97.8%  ############################

## Colour group pull rate (winner)

- brown      0.96 per space
- rail       0.98 per space
- lightblue  0.97 per space
- pink       0.98 per space
- util       0.98 per space
- orange     0.98 per space
- red        0.98 per space
- yellow     0.97 per space
- green      0.97 per space
- darkblue   0.97 per space
