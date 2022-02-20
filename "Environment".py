"Environment"

import numpy as np
import torch

state, action, reward, next_state, trade = experiences

trade_result = #retrieve the last single trade from API


class Environment():


    def __init__(self):
        #initialize global variables that you will need throughout the class

        self.balance = balance #collect balance from fetching api
        self.trade_result = trade_result #from api fetch trade result




    def calculate_reward(self, trade_result):

        current_balance = trade_result + balance

        ##find a reward function that works by scaling reward based on size of profits/losses
        if current_balance > balance:

            reward = trade_result * 1.05

        return reward


    def reward(self):

        #give reward to agent so it can be stored
        if trade:
            reward = Environment.calculate_reward()




    def step(self, state, action):

        #be able to take state as input of pictures
        #take action as input and send action to the api environment
        #collect reward from rewards functions


    def memory(self):

        #send all images to cloud storage
    
    



    

    

    

    