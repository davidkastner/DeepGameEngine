import retro
import gym

# Import your game first 
# python3.8 -m retro.import "Super Mario Bros. (World)"
# Note that the .nes needs to be in a directory

# Create your game environment
env = retro.make(game='SuperMarioBros-Nes')

# Start the game at the beginning
obs = env.reset()

# Set up the game loop
done = False
while not done:
    obs, rew, done, info = env.step(env.action_space.sample())
    env.render()
    
env.close()