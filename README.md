# Super Mario Bros AI

This project implements various AI algorithms to play Super Mario Bros. The implemented algorithms include Deep Q-Network (DQN), Proximal Policy Optimization (PPO), and NeuroEvolution of Augmenting Topologies (NEAT).

## Project Structure

- `DQN.py`: Implementation of the Deep Q-Network algorithm.
- `NEAT.py`: Implementation of the NEAT algorithm.
- `PPO.py`: Implementation of the Proximal Policy Optimization algorithm.

## Getting Started

### Prerequisites

- Python 3.8

## Algorithms
- Deep Q-Network (DQN)

Implemented in DQN.py, DQN is a reinforcement learning algorithm that combines Q-learning with deep neural networks.

- Proximal Policy Optimization (PPO)

Implemented in PPO.py, PPO is a reinforcement learning algorithm that improves training stability by limiting the policy update step size.

- NeuroEvolution of Augmenting Topologies (NEAT)

Implemented in neat.py, NEAT is a genetic algorithm that evolves neural networks by optimizing both the network weights and topology.
The configuration for the NEAT algorithm is specified in the `config-feedforward` file.