import gymnasium as gym

env = gym.make("HalfCheetah-v4", ctrl_cost_weight=0.1, render_mode="human")
env.spec
reward_threshold = 4800.0

env.reset()
total = 0
done = False
truncated = False
while not done and not truncated:
    action = env.action_space.sample()
    o, reward, done, truncated, _ = env.step(action)
    total += reward
    env.render()
    print(total)
env.close()
