import numpy as np


class ArgMaxPolicy(object):

    def __init__(self, critic):
        self.critic = critic

    def get_action(self, obs):
        if len(obs.shape) > 3:
            observation = obs
        else:
            observation = np.expand_dims(obs, 0)
        
        ## TODO return the action that maxinmizes the Q-value 
        # at the current observation as the output
        return action.squeeze()