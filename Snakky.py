#!/usr/bin/env python3.5
import sys
import snake
def main(args):
	my_snake = snake.SnakeGame(frame_count = args['frame_count'],
								save_moves = args['save_moves'],
								play_ai = args['play_ai'],
								disp_board_grid = args['disp_board_grid'])
	my_snake.main_loop()

if __name__ == '__main__':
	args = {'frame_count':10,
			'save_moves': False,
			'play_ai': False,
			'disp_board_grid': True}
	if 'h' in sys.argv:
		print("Usage: [python3.5 |./]{!s} h f <value>| s | p | d ".format(sys.argv[0]))
		sys.exit()
	if 'f' in sys.argv:
		val = sys.argv.index('f')
		args['frame_count'] = int(sys.argv[val+1])
	if 's' in sys.argv:
		args['save_moves'] = True
	if 'p' in sys.argv:
		args['play_ai'] = True
	if 'd' in sys.argv:
		args['disp_board_grid'] = False
	print("Frame Count: {!s}".format(args['frame_count']))
	print("Save Moves: {!s}".format("Enabled" if args['save_moves'] == True else "Disabled"))
	print("Playing: {!s}".format("Computer AI" if args['play_ai'] == True else "Human"))
	print("Grid Display: {!s}".format("Enabled" if args['disp_board_grid'] == True else "Disabled"))
	main(args)
