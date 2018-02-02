# Snake-AI
1. To see help:
  python-3.x Snakky.py h

__TODO__
1. Adding AI still in progress 


# How it works ?

## Notes:
* while opening the game from `terminal` use the command `python-3.5 Snakky.py [flags]` or if you have default python3.5 in `/usr/bin/env` just give `chmod` execute capability to `Snakky.py` and run the game using `./Snakky.py [flags]`
* To create the data set while playing set the `s` option while opening the game from terminal.
* To run in AI mode set the `p` flag (Please don't use this feature now because it has yet to be integrated.)

When you are playing the game and if the `s` flag is set the scripts behined the model starts gathering information about the coordinates of the snake and of the apple at every iteration. The data is then shaped in the form of an image of the snake game as seen by the player. This data is then passed through the neural network model and used to train the model. The werights are saved and will be used during the gameplay.
