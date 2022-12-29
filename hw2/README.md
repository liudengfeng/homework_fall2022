
## Small-Scale Experiments

### Experiment 1 (CartPole)

Run multiple experiments with the PG algorithm on the discrete CartPole-v1
environment, using the following commands:

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v1 -n 100 -b 1000 \
-dsa --exp_name q1_sb_no_rtg_dsa \
--video_log_freq 1
```

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v1 -n 100 -b 1000 \
-rtg -dsa --exp_name q1_sb_rtg_dsa
```

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v1 -n 100 -b 1000 \
-rtg --exp_name q1_sb_rtg_na
```

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v1 -n 100 -b 5000 \
-dsa --exp_name q1_lb_no_rtg_dsa
```

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v1 -n 100 -b 5000 \
-rtg -dsa --exp_name q1_lb_rtg_dsa
```

```bash
python cs285/scripts/run_hw2.py --env_name CartPole-v1 -n 100 -b 5000 \
-rtg --exp_name q1_lb_rtg_na
```

What’s happening here:

- -n : Number of iterations.
- -b : Batch size (number of state-action pairs sampled while acting according to the current policy at
each iteration).
- -dsa : Flag: if present, sets standardize_advantages to False. Otherwise, by default, standardizes
advantages to have a mean of zero and standard deviation of one.
- -rtg : Flag: if present, sets reward_to_go=True. Otherwise, reward_to_go=False by default.
- --exp_name : Name for experiment, which goes into the name for the data logging directory.
