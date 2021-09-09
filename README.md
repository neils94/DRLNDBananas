# Summary
 - Reinforcement learning is a section of machine learning that designs an algorithm to learn how to achieve tasks from positive and negative rewards. When implemented with deep neural networks, it has been cutting edge in the world of AI. 
 - This project was designed to show the potential of the learning algorithm within a discrete space.

# The Environment
- The agent is operating within an environment that is discrete; meaning it has a finite set of state spaces (37) that it can travel to. 
- The environment also has bananas scattered around it, blue and yellow.
- It's built using Unity and Gym, taking raw pixels from 3 dimensional space and turning it into vectors so that the problem is approachable in 2 dimensional space.

# The Agent
- The agent's job is to learn from its environment as quickly as possible; it has 4 available actions to it (forwards, backwards, left, right).
- What is the agent learning from the environment? Good question, the agent is learning whether it should collect or avoid certain bananas: Blue bananas give the agent a negative reward while yellow bananas give it a positive reward. The agent is trying to maximize the number of rewards it receives, and in doing so will learn to avoid blue bananas as much as possible while collecting yellow bananas.


# Dependencies/Installations
To work with the environment you must install gym, pytorch (or any deep learning library you're comfortable with) and Unity/Unity ML-agents you can do so by using following repositories to install dependencies:

[Unity](https://unity3d.com/get-unity/download)

[Unity-mlagents](https://github.com/Unity-Technologies/ml-agents/blob/main/docs/Readme.md)

[Gym install](https://github.com/openai/gym).

[PyTorch](https://pytorch.org/)

