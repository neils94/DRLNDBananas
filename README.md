# Summary
 - Reinforcement learning is a section of machine learning with sets of algorithms that can be trained to learn how to achieve tasks from positive and negative rewards. When implemented with deep neural networks, it has been cutting edge in the world of AI. 

 - This project is designed to show the potential of the learning algorithm within a discrete state and action space.

# The Environment
- The agent is operating within an environment that is discrete; meaning the environment has 33 variables that correspond to the agents velocity, position, rotation and angular velocities. 
- The environment is a double-jointed arm can move to target locations.
- It's built using Unity and Gym packages on python, taking raw pixels from 3 dimensional space and turning it into vectors so that the problem is approachable in 2 dimensional space.

# The Agent
- The agent's job is to learn from its environment as quickly as possible; it has 4 available actions each action is a vector with four numbers, corresponding to torque applicable to two joints.
- What is the agent learning from the environment? Good question, the agent is learning to put its arm in target locations. The agent receives a reward of +0.1 for every goal target location that it reaches, and it's goal is to maintain its position at the target location for as many time steps as possible.
- The environment is considered to be solved when the agent can reach a an average score of +30 over a 100 episode period.


# Dependencies/Installations
To work with the environment you must install gym, pytorch (or any deep learning library you're comfortable with) and Unity/Unity ML-agents you can do so by using following repositories to install dependencies:

[Unity](https://unity3d.com/get-unity/download)

[Unity-mlagents](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Readme.md)

[Gym install](https://github.com/openai/gym).

[PyTorch](https://pytorch.org/)

