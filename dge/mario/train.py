"""Train DQN model on super mario bros"""
import os
import gym
import retro
import numpy as np

# from RandomAgent import TimeLimitWrapper
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, SubprocVecEnv
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.results_plotter import load_results, ts2xy, plot_results
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.common.vec_env import VecMonitor
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv


class SaveOnBestTrainingRewardCallback(BaseCallback):
    """
    Callback for saving a model (the check is done every ``check_freq`` steps).
    Based on the training reward (in practice, we recommend using ``EvalCallback``).

    Parameters
    ----------
    check_freq : bool
        Whether to check the frequency
    log_dir : str
        Path to the folder where the model will be saved, must contains the file created by the ``Monitor`` wrapper.
    verbose : int
        Verbosity level: 0 for no output, 1 for info messages, 2 for debug messages

    """

    def __init__(self, check_freq: int, log_dir: str, verbose: int = 1):
        super(SaveOnBestTrainingRewardCallback, self).__init__(verbose)
        self.check_freq = check_freq
        self.log_dir = log_dir
        self.save_path = os.path.join(log_dir, "best_model")
        self.best_mean_reward = -np.inf

    def _init_callback(self) -> None:
        # Create folder if needed
        if self.save_path is not None:
            os.makedirs(self.save_path, exist_ok=True)

    def _on_step(self) -> bool:
        if self.n_calls % self.check_freq == 0:
            # Retrieve training reward
            x, y = ts2xy(load_results(self.log_dir), "timesteps")
            if len(x) > 0:
                # Mean training reward over the last 100 episodes
                mean_reward = np.mean(y[-100:])
                if self.verbose >= 1:
                    print(f"Num timesteps: {self.num_timesteps}")
                    print(
                        f"Best mean reward: {self.best_mean_reward:.2f} - Last mean reward per episode: {mean_reward:.2f}"
                    )

                # New best model, you could save the agent here
                if mean_reward > self.best_mean_reward:
                    self.best_mean_reward = mean_reward
                    # Example for saving best model
                    if self.verbose >= 1:
                        print(f"Saving new best model to {self.save_path}")
                    self.model.save(self.save_path)

        return True


def make_env(env_id, rank, seed=0):
    """
    Utility function for multiprocessed env.

    Paramaters
    ----------
    env_id : str
        The environment ID
    num_env : int
        The number of environment you wish to have in subprocesses
    seed : int
        The inital seed for RNG
    rank : int
        Index of the subprocess

    """

    def _init():
        env = retro.make(game=env_id)
        # env = TimeLimitWrapper(env, max_steps=2000)
        env = MaxAndSkipEnv(env, skip=2)
        env.seed(seed + rank)
        return env

    set_random_seed(seed)
    return _init


def train():
    """
    Function for training on the model.

    Notes
    -----
    Open tensorboard with `tensorboard --logdir tensorboard`

    """
    # Create log dir
    log_dir = "tmp/"
    os.makedirs(log_dir, exist_ok=True)

    env_id = "SuperMarioBros-Nes"
    num_cpu = 12  # Number of simultaneous traning instances

    # Create the vectorized environment
    env = VecMonitor(
        SubprocVecEnv([make_env(env_id, i) for i in range(num_cpu)]), log_dir
    )

    # Directly load the model
    model_path = os.path.join(log_dir, "best_model.zip")
    if os.path.isfile(model_path):
        model = PPO.load(model_path, env=env, tensorboard_log="./tensorboard/")
    else:
        model = PPO(
            "CnnPolicy",
            env,
            verbose=1,
            tensorboard_log="./tensorboard/",
            learning_rate=0.00003,
        )

    print("<<<<< Start learning >>>>>")
    callback = SaveOnBestTrainingRewardCallback(check_freq=1000, log_dir=log_dir)
    model.learn(total_timesteps=20000000, callback=callback, tb_log_name="PPO-00003")
    model.save(f"{env_id}")
    print("<<<<< Stop learning >>>>>")


if __name__ == "__main__":
    train()
