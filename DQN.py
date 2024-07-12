import gym
import numpy as np
from stable_baselines3 import DQN
from stable_baselines3.common.vec_env import SubprocVecEnv
from stable_baselines3.common.utils import set_random_seed
from stable_baselines3.common.vec_env import VecMonitor
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv
from stable_baselines3.common.callbacks import EvalCallback, CheckpointCallback
import os
import retro

class TimeLimitWrapper(gym.Wrapper):
  """
  :param env: (gym.Env) Gym environment that will be wrapped
  :param max_steps: (int) Max number of steps per episode
  """
  def __init__(self, env, max_steps=10000):
    # Call the parent constructor, so we can access self.env later
    super(TimeLimitWrapper, self).__init__(env)
    self.max_steps = max_steps
    # Counter of steps per episode
    self.current_step = 0
  
  def reset(self):
    """
    Reset the environment 
    """
    # Reset the counter
    self.current_step = 0
    return self.env.reset()

  def step(self, action):
    """
    :param action: ([float] or int) Action taken by the agent
    :return: (np.ndarray, float, bool, dict) observation, reward, is the episode over?, additional informations
    """
    self.current_step += 1
    obs, reward, done, info = self.env.step(action)
    # Overwrite the done signal when 
    if self.current_step >= self.max_steps:
      done = True
      # Update the info dict to signal that the limit was exceeded
      info['time_limit_reached'] = True
    info['Current_Step'] = self.current_step
    return obs, reward, done, info

class CustomReward(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.previous_position = None
    
    def step(self, action):
        results = super().step(action)
        observation, reward, done, info = results
        xscrollLo = info.get('xscrollLo', 0)
        xscrollHi = info.get('xscrollHi', 0)
        levelLo = info.get('levelLo', 0)
        current_position = xscrollHi * 256 + xscrollLo

        # Si se queda quieto -1 reward excepto cuando esta al final del nivel (11*256+200)
        if self.previous_position is not None and current_position == self.previous_position and current_position < 3030 and levelLo == 0:
            reward -= 1
        # Si pasa el nivel reward (xscrollHi = 11, xscrollLo = 220)
        if current_position >= 3036:
            reward += 1

        self.previous_position = current_position
        print(f"Reward: {reward}, info: {info}")
        return results 

class MultiBinaryToDiscreteActionWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.action_space = gym.spaces.Discrete(2**env.action_space.n)
        
    def action(self, action):
        # Convert discrete action to MultiBinary action
        binary_action = np.array(list(np.binary_repr(action, width=self.env.action_space.n)), dtype=int)
        return binary_action
    
def make_env(env_id, rank, seed=0):
    """
    Utility function for multiprocessed env.

    :param env_id: (str) the environment ID
    :param num_env: (int) the number of environments you wish to have in subprocesses
    :param seed: (int) the inital seed for RNG
    :param rank: (int) index of the subprocess
    """
    def _init():
        env = retro.make(game=env_id)
        env = MultiBinaryToDiscreteActionWrapper(env)
        env = TimeLimitWrapper(env, max_steps=2000)
        env = MaxAndSkipEnv(env, 4)
        env = CustomReward(env)
        env.seed(seed + rank)
        return env
    set_random_seed(seed)
    return _init

if __name__ == '__main__':
    env_id = "SuperMarioBros-Nes"
    num_cpu = 4 

    env = VecMonitor(SubprocVecEnv([make_env(env_id, i) for i in range(num_cpu)]), "tmp/TestMonitor")
    
    log_path = os.path.join("Modelos", "DQN", "DQN-01")
    model = DQN('CnnPolicy', env, verbose=1, tensorboard_log=log_path, learning_rate=0.0001, buffer_size=10000, exploration_final_eps=0.02)
    #model = DQN.load("./Modelos/DQN/DQN-01/model_1240000_steps", env=env)
    eval_callback = EvalCallback(env, best_model_save_path=log_path,
                                 log_path=log_path, eval_freq=5000,
                                 deterministic=True, render=False)
    checkpoint_callback = CheckpointCallback(save_freq=10000, save_path='./Modelos/DQN/DQN-01',
                                         name_prefix='model')
    """ remaining_timesteps = 2_000_000 - 640_000
    model.learn(total_timesteps=remaining_timesteps, log_interval=1, callback=[eval_callback, checkpoint_callback], reset_num_timesteps=False) """
    model.learn(total_timesteps=2_000_000, callback=[eval_callback, checkpoint_callback])
    model_path = os.path.join("Modelos", "DQN", "DQN-01")
    model.save(model_path)