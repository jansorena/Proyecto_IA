import os
import retro
import numpy as np
import cv2
import neat
import pickle

env = retro.make(game='SuperMarioBros-Nes', state='Level1-1', record=True)
imgArray = []

def eval_genomes(genomes, config):

    for genome_id, genome in genomes:
        
        ob = env.reset() 
        random_action = env.action_space.sample()
        inx,iny,inc = env.observation_space.shape 
        
        inx = int(inx/8)
        iny = int(iny/8)
        
        net = neat.nn.RecurrentNetwork.create(genome,config)
        current_max_fitness = 0
        fitness_current = 0
        frame = 0
        counter = 0

        done = False
        actions = [
            [1, 0, 0, 0, 0, 0, 0, 1, 0], #correr a la derecha
            [1, 0, 0, 0, 0, 0, 0, 1, 1] #correr a la derecha y saltar
        ]
        def _get_actions(a):
            return actions[a.index(max(a))]
        while not done:
            env.render()
            frame+=1

            ob = cv2.resize(ob,(inx,iny)) 
            ob = cv2.cvtColor(ob, cv2.COLOR_BGR2GRAY) 
            
            imgArray = np.ndarray.flatten(ob)
            neuralnet_output = net.activate(imgArray)
            action = _get_actions(neuralnet_output)
            ob, rew, done, info = env.step(action)

            fitness_current += rew

            if fitness_current>current_max_fitness:
                current_max_fitness = fitness_current
                counter = 0
            else:
                counter+=1
            
            if done or counter == 250:
                done = True 
                print(genome_id,fitness_current)
            
            genome.fitness = fitness_current
    print(stats.get_fitness_mean())
    with open('average_fitness.txt', 'a') as file:
        file.write(str(stats.get_fitness_mean()) + "\n")

if os.path.exists('----neat-checkpoint-600'):
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-600')
else:
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                        neat.DefaultSpeciesSet, neat.DefaultStagnation,
                        'config-feedforward')
    p = neat.Population(config)

p.add_reporter(neat.StdOutReporter(True))
stats = neat.StatisticsReporter()
p.add_reporter(stats)

p.add_reporter(neat.Checkpointer(10))


winner = p.run(eval_genomes)

with open('winner.pkl', 'wb') as output:
    pickle.dump(winner, output, 1)