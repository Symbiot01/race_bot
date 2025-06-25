import argparse
import gymnasium as gym
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Placeholder environment import
try:
    from f1tenth_gym.envs import F110Env
except ImportError:
    F110Env = None


def main(total_timesteps: int = 10000, save_path: str = "ppo_f110"):
    """Train a PPO agent on the F1TENTH environment."""
    if F110Env is None:
        raise ImportError(
            "f1tenth_gym is required for training. Install it from"
            " https://github.com/f1tenth/f1tenth_gym." 
        )

    env = make_vec_env(lambda: F110Env(map="spielberg"), n_envs=1)
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=total_timesteps)
    model.save(save_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--steps", type=int, default=10000,
                        help="Number of training timesteps")
    parser.add_argument("--save", type=str, default="ppo_f110",
                        help="Model save path")
    args = parser.parse_args()
    main(total_timesteps=args.steps, save_path=args.save)

