import retro

#python3 -m retro.examples.interactive --game SuperMarioBros-Nes
def main():
    env = retro.make(game="SuperMarioBros-Nes")
    env.reset()
    while True:
        action = env.action_space.sample()
        observation, reward, terminated, truncated, info = env.step(action)
        env.render()
        if terminated or truncated:
            env.reset()
    env.close()


if __name__ == "__main__":
    main()