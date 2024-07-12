import time
import retro
import gym
import numpy as np
from stable_baselines3 import PPO, DQN
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv

class MultiBinaryToDiscreteActionWrapper(gym.ActionWrapper):
    def __init__(self, env):
        super().__init__(env)
        self.action_space = gym.spaces.Discrete(2**env.action_space.n)
        
    def action(self, action):
        # Convert discrete action to MultiBinary action
        binary_action = np.array(list(np.binary_repr(action, width=self.env.action_space.n)), dtype=int)
        return binary_action
    
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

model = PPO.load("Modelos/PPO/PPO-01/model_320000_steps") 
#model = DQN.load("Modelos/DQN/DQN-00001/model_1200000_steps")
def main():
    steps = 0
    env = retro.make(game='SuperMarioBros-Nes')
    #env = MultiBinaryToDiscreteActionWrapper(env)
    env = TimeLimitWrapper(env)
    env = MaxAndSkipEnv(env, 4)
    obs = env.reset()
    done = False
    while not done:
        if done:
            obs = env.reset()
        time.sleep(0.01)
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)
        #print(f"Reward: {reward}, Action: {action}")
        env.render()
    env.close()

if __name__ == "__main__":
    main()