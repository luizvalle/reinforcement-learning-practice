import gymnasium as gym

if __name__ == '__main__':
    env = gym.make('CartPole-v1')
    total_reward = 0
    total_steps = 0
    obs, _ = env.reset()

    is_done = False

    while not is_done:
        action = env.action_space.sample()
        obs, reward, is_done, is_trunc, _ = env.step(action)
        total_reward += reward
        total_steps += 1
    
    print(
        f'Episode done in {total_steps} steps, total reward {total_reward:.2f}')
