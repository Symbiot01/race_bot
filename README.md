# race_bot

This package contains a basic ROS2 description of a race car. It is based on the
[f1tenth_gym_ros](https://github.com/f1tenth/f1tenth_gym_ros) project.

## Reinforcement Learning

A simple training script using [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3)
can be found in `scripts/train_ppo.py`. It expects the `f1tenth_gym` Python
package to be available. You can install it from the upstream repository:

```bash
pip install git+https://github.com/f1tenth/f1tenth_gym.git
```

Then run the training script:

```bash
python3 scripts/train_ppo.py --steps 100000 --save ppo_f110
```

This will train a PPO agent on the F1TENTH environment and save the model.
