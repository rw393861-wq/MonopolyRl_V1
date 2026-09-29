# Monopoly self-play report

Run directory: `logs/train-20260929-194307`
Games logged: 60000
Average rounds per game: 60.1

## Overall win share

| agent | wins | share |
|---|---|---|
| rulebot | 9998 | 16.7% |
| AI_2 | 16304 | 27.2% |
| AI_3 | 15823 | 26.4% |

## End condition

- last_standing: 59853 (99.8%)
- round_limit: 147 (0.2%)

## Win rate over training windows

| window | games | rulebot | AI_2 | AI_3 | avg rounds |
|---|---|---|---|---|---|
| 1 | 6000 | 16% | 27% | 26% | 59 |
| 2 | 6000 | 15% | 26% | 27% | 60 |
| 3 | 6000 | 15% | 28% | 28% | 60 |
| 4 | 6000 | 16% | 34% | 24% | 61 |
| 5 | 6000 | 17% | 26% | 24% | 60 |
| 6 | 6000 | 17% | 21% | 26% | 60 |
| 7 | 6000 | 17% | 28% | 30% | 61 |
| 8 | 6000 | 18% | 30% | 25% | 60 |
| 9 | 6000 | 17% | 30% | 26% | 60 |
| 10 | 6000 | 17% | 22% | 28% | 60 |

## Per-agent averages

| agent | props held | houses built | rent received | trades |
|---|---|---|---|---|
| rulebot | 4.6 | 9.1 | 1324 | 0.89 |
| AI_2 | 7.4 | 14.3 | 2258 | 1.51 |
| AI_3 | 7.2 | 13.3 | 2219 | 1.40 |

## Properties most often held by the winner

- Illinois Avenue           98.6%  ############################
- Reading Railroad          98.6%  ############################
- Tennessee Avenue          98.5%  ############################
- St. Charles Place         98.4%  ############################
- New York Avenue           98.4%  ############################
- St. James Place           98.3%  ############################
- B&O Railroad              98.3%  ############################
- Pennsylvania Railroad     98.1%  ############################
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
- darkblue   0.96 per space
