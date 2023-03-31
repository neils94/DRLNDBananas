import torch
from torch import nn
import numpy as np


import torch
import torch.nn as nn
import torch.autograd as autograd
import torch.optim as optim

import numpy as np
import torch.nn.functional as F
import matplotlib.pyplot as plt


def hidden_init(layer):
        fan_in = layer.weight.data.size()[0]
        limit = 1.0/np.sqrt(fan_in)
        return (-limit, limit)

class Actor(nn.Module):
    
    def __init__(self, state_size, action_size, hidden_layer, hidden2_layer, seed):
        
        super(Actor, self).__init__()
        self.seed = torch.manual_seed(0)
        self.fc1 = nn.Linear(state_size, hidden_layer)
        self.fc2 = nn.Linear(hidden_layer, hidden2_layer)
        self.fc3 = nn.Linear(hidden2_layer, action_size)
        self.batch_norm = nn.BatchNorm1d(state_size)
        self.parameter_initializer()
        
        
    def parameter_initializer(self):
        #initialize weights to prevent vanishing or exploding gradients
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        
        #final layer is initialized [3*10^-3, 3*10-3]
        
        self.fc3.weight.data.uniform_(-3e-3,3e-3)
        
        
        
    def forward(self, states):
        if states.dim() == 1:
            states = torch.unsqueeze(states, 0)
        states = self.batch_norm(states)
        
        x = F.relu(self.fc1(states))
        x = F.relu(self.fc2(x))
        
        
        
        return F.tanh(self.fc3(x))
    
    
class Critic(nn.Module):
    def __init__(self, state_size, action_size, hidden_layer, hidden2_layer, seed):
        
        
        super(Critic,self).__init__()
        self.seed = torch.manual_seed(0)
        self.fc1 = nn.Linear(state_size, hidden_layer)
        self.fc2 = nn.Linear(hidden_layer + action_size, hidden2_layer)
        self.fc3 = nn.Linear(hidden2_layer, 1)
        
        self.batch_norm = nn.BatchNorm1d(state_size)
        
    def parameter_initializer(self):
        
        self.fc1.weight.data.uniform_(*hidden_init(self.fc1))
        self.fc2.weight.data.uniform_(*hidden_init(self.fc2))
        
        self.fc3.weight.data.uniform_(-3e-3, 3e-3)
        
    
    def forward(self, states, actions):
        if states.dim() == 1:
            states = torch.unsqueeze(states, 0)
            
        states = self.batch_norm(states)

        xs = F.relu(self.fc1(states))
        x = torch.cat([xs, actions], dim=1)
        x = F.relu(self.fc2(x))
        
        return self.fc3(x)
