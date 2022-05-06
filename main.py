import gym


def naive_action(observation):
    return 0 if observation[2] < 0 else 1


def main():
    policy = naive_action
    env = gym.make("CartPole-v0")
    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            env.render()
            action = policy(observation)
            observation, reward, done, info = env.step(action)
            if done:
                print(f"Episode finished after {t + 1} timesteps")
                break
    env.close()


if __name__ == "__main__":
    main()
