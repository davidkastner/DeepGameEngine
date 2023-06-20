"""Test out the best performing model on the environment."""

import retro
from stable_baselines3 import PPO
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv

model = PPO.load("tmp/best_model.zip")


def main():
    env = retro.make(game="SuperMarioBros-Nes")
    env = MaxAndSkipEnv(env, skip=4)

    obs = env.reset()

    while True:
        action, _states = model.predict(obs)
        obs, rewards, dones, info = env.step(action)
        env.render()


if __name__ == "__main__":
    main()
