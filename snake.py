#!/usr/bin/env python3.5
import pygame as pg
import sys
import pygame.locals as pg_local
import random
import time
import pygame.gfxdraw
random.seed(int((time.time())%1000))
class Board:

	def __init__(self, disp_surf = None, height = 480, width = 640, step = 20,
		 			back_color = pg.Color(143, 252, 131), 
	 				line_color = pg.Color(255, 255, 255), 
	 				line_thickness = 2, disp_board_grid = True):
		self._height = height
		self._width = width
		self._step = step
		self._back_color = back_color
		self._line_color = line_color
		self._disp_surf = disp_surf
		self._line_thickness = line_thickness
		self.disp_board_grid = disp_board_grid

	def draw(self):
		self._disp_surf.fill(self._back_color)
		if self.disp_board_grid == True:
			for i in range(0, self._width, self._step):
				pg.draw.line(self._disp_surf, self._line_color, (i, 0), (i, self._height), self._line_thickness)
			for i in range(0, self._height, self._step):
				pg.draw.line(self._disp_surf, self._line_color, (0, i), (self._width, i), self._line_thickness)

	def get_box_form(self):
		return  (int(self._width / self._step), int(self._height / self._step))

	def conv_left_top(self, boxx, boxy):
		return (boxx * self._step, boxy * self._step)

	def conv_box(self, left, top):
		return (int(left / self._step), int(top, self._step))

	def box_dim(self):
		return (self._step, self._step)

	def get_dim(self):
		return (self._width, self._height)


class Apple:
	def __init__(self, disp_surf, board, snake):
		self._board = board
		self.snake = snake
		self._disp_surf = disp_surf
		self._horizontal_boxes, self._vertical_boxes = self._board.get_box_form()
		self._coords_of_apple = self.__generate_random()
		self._color_inner = pg.Color(252, 92, 68)
		self._length,self._width = self._board.box_dim()
		self._color_outer = pg.Color(178, 68, 51)
		self.coords = self._coords_of_apple
		self._radius = 8

	def __generate_random(self):
		body =  self.snake.get_body()
		body_x = [x[0] for x in body]
		body_y = [x[1] for x in body]
		seq = [(i, j) for i in range(5, self._horizontal_boxes-5) for j  in range(5, self._vertical_boxes-5) if not (i in body_x and j in body_y)]
		#print("Sequence" + str(seq))
		ch = random.choice(seq)
		return (ch[0], ch[1])

	def draw(self, generate_new = False):
		if generate_new == True:
			self._coords_of_apple = self.coords = self.__generate_random()
		coords = self._board.conv_left_top(self._coords_of_apple[0], self._coords_of_apple[1])
		pg.draw.rect(self._disp_surf, self._color_outer, (coords[0], coords[1], self._length, self._width))
		pg.draw.rect(self._disp_surf, self._color_inner, (coords[0]+3, coords[1]+3, self._length-6, self._width-6))
		"""pg.gfxdraw.filled_circle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius, self._color_inner)
		pg.gfxdraw.aacircle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius, self._color_outer)
		pg.gfxdraw.aacircle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius-1, self._color_outer)
		pg.gfxdraw.aacircle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius-2, self._color_outer)
		pg.gfxdraw.aacircle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius, self._color_outer)
		pg.gfxdraw.aacircle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius-1, self._color_outer)
		pg.gfxdraw.aacircle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius-2, self._color_outer)"""

	def get_coords(self):
		return self._coords_of_apple


class Snake:
	def __init__(self, disp_surf, board):
		self._disp_surf = disp_surf
		self._board = board
		self._horizontal_boxes, self._vertical_boxes = self._board.get_box_form()
		self._length,self._width = self._board.box_dim()
		self.head = self.__generate_random()
		self.body = [{'x': self.head[0], 'y':self.head[1]},
					{'x': self.head[0]-1, 'y':self.head[1]},
					{'x': self.head[0]-2, 'y':self.head[1]}]
		self._color_inner = pg.Color(38, 168, 15)
		self._color_outer = pg.Color(36, 104, 17)
		self.cur_dir = 'right'
		self._radius = 9

	def specify_head(self, coords):
		self.head = coords
		self.body = [{'x': self.head[0], 'y':self.head[1]},
					{'x': self.head[0]-1, 'y':self.head[1]},
					{'x': self.head[0]-2, 'y':self.head[1]}]
	def draw(self):
		for i in range(len(self.body)):
			coords = self._board.conv_left_top(self.body[i]['x'], self.body[i]['y'])
			pg.draw.rect(self._disp_surf, self._color_outer, (coords[0], coords[1], self._length, self._width))
			pg.draw.rect(self._disp_surf, self._color_inner, (coords[0]+3, coords[1]+3, self._length-6, self._width-6))
			#pg.gfxdraw.filled_circle(self._disp_surf, coords[0] + int(self._width/2), coords[1] + int(self._length/2), self._radius, self._color_inner)

	def __generate_random(self):
		return (random.randint(10, self._horizontal_boxes-10), 
				random.randint(10, self._vertical_boxes-10))

	def cross_over(self):
		if self.head[0] < 0 or self.head[0] >= self._horizontal_boxes or \
		 self.head[1] < 0 or self.head[1] >= self._vertical_boxes:
		 	return True
		for i in range(1, len(self.body)):
			if self.body[i]['x'] == self.head[0] and self.body[i]['y'] == self.head[1]:
				return True
		return False

	def remove_tail(self):
		if len(self.body) != 0:
				self.body.pop()

	def push_coords(self, coords, on_tail = False):
		if on_tail == True:
			self.body.append({'x': coords[0], 'y':coords[1]})
			return
		self.body.insert(0, {'x': coords[0], 'y': coords[1]})
		self.head = coords

	def _get_possible(self, val):
		if val in ('up', 'down'):
			return ['left', 'right']
		elif val in ('left', 'right'):
			return ['up', 'down']

	def change_dir(self, new_dir):
		possibles = self._get_possible(self.cur_dir)
		if not new_dir in possibles:
			return
		else:
			self.cur_dir = new_dir
		self.make_changes()

	def make_changes(self, remove_tail_bool = True):
		if remove_tail_bool == True:
			self.remove_tail()
		to_add = None
		if self.cur_dir == 'up':
			to_add = (self.head[0], self.head[1] - 1)
		elif self.cur_dir == 'down': 
			to_add = (self.head[0], self.head[1] + 1)
		elif self.cur_dir == 'left':
			to_add = (self.head[0] - 1, self.head[1])
		elif self.cur_dir == 'right':
			to_add = (self.head[0] + 1, self.head[1])
		self.push_coords(to_add)

	def move(self, generate_tail = False):
		if generate_tail == False:
			self.make_changes()
		else:
			self.make_changes(remove_tail_bool = False)

	def get_body(self):
		to_ret = []
		for i in self.body:
			to_ret.append((i['x'], i['y']))
		return to_ret

class ComicWrites:
	def __init__(self, disp_surf, font_spec = "./fonts/font_to_use.ttf", font_size = 32):
		self.font_spec = font_spec
		self.font_size = font_size
		self.disp_surf = disp_surf
		self.__font_obj = pg.font.Font(self.font_spec, self.font_size)

	def get_write(self, to_write, coords, anti_alias = True, text_color = pg.Color(46, 173, 53)):
		text_surf_obj = self.__font_obj.render(to_write, anti_alias, text_color)
		text_rect_obj = text_surf_obj.get_rect()
		text_rect_obj.center = coords
		self.disp_surf.blit(text_surf_obj, text_rect_obj)
		return self.disp_surf

class SnakeGame:
	def __init__(self, frame_count = 30, save_moves = True, play_ai = False, disp_board_grid = True):
		pg.init()
		self.disp_surf = pg.display.set_mode((640, 480))
		pg.display.set_caption(("Twister"))
		self.board = Board(self.disp_surf, disp_board_grid = disp_board_grid)
		self.fps_clock = pg.time.Clock()
		self.FPS = frame_count
		self.apple = None
		self.snake = None
		self.score = 0
		self.state_capture = Capture("SnakeEvents.txt")
		self.score_board = ComicWrites(self.disp_surf, font_size = 16)
		self.save_moves = save_moves
		self.play_ai = play_ai
		if self.play_ai == True:
			self.random_move_gen = MoveGenerate()

	def new_pieces(self):
		snake = Snake(self.disp_surf, self.board)
		apple = Apple(self.disp_surf, self.board, snake)
		score = 0
		return (apple, snake, 0)

	def main_loop(self):
		self.start_game()
		while True:
			self.run()
			self.state_capture.submit_event(request_save = True)
			self.game_over()

	def run(self):
		self.apple, self.snake, self.score = self.new_pieces()
		dim = self.board.get_dim()
		count = -1
		event_detected = False
		key = None
		change_dir = False
		while True:	
			event_detected = False
			count+=1
			change_dir = False
			key = None
			for event in pg.event.get():
				event_detected = True
				if event.type == pg_local.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg_local.KEYUP and self.play_ai == False:
					change_dir = True
					if event.key in (pg_local.K_LEFT, pg_local.K_a):
						#self.snake.change_dir(key)	
						key = 'left'
					elif event.key in (pg_local.K_RIGHT, pg_local.K_d):
						#self.snake.change_dir("right")
						key = 'right'
					elif event.key in (pg_local.K_UP, pg_local.K_w):
						#self.snake.change_dir('up')
						key = 'up'
					elif event.key in (pg_local.K_DOWN, pg_local.K_s):
						#self.snake.change_dir('down')
						key = 'down'
				if self.save_moves	 == True:
					self.state_capture.submit_event(self.get_status(key))
				self.snake.change_dir(key)
			if self.play_ai == True:
				key = self.translate_number_to_event(self.random_move_gen.gen_move())
				#print('gen >> {!s}'.format(key))
				self.snake.change_dir(key)
			self.board.draw()
			self.snake.draw()
			if self.snake.cross_over():
				break
			if self.snake.head == self.apple.coords:
				self.score+=1;
				self.apple.draw(generate_new = True)
				self.snake.move(generate_tail = True)
			else:
				self.apple.draw()
				self.snake.move()
			self.score_board.get_write("Score: {!s}".format(self.score),(dim[0]-50, 10), text_color = pg.Color(0, 41, 39))
			pg.display.update()
			self.fps_clock.tick(self.FPS)

	def game_over(self):
		dim = self.board.get_dim()
		game_over_surf = pg.Surface(dim)
		game_over_surf = game_over_surf.convert_alpha()
		back_color = pg.Color(0, 0, 0, 200)
		game_over_surf.fill(back_color)
		game_over_font = ComicWrites(game_over_surf, font_size = 60)
		game_over_surf = game_over_font.get_write("Game over", (dim[0]/2, dim[1]/2))
		self.disp_surf.blit(game_over_surf, (0, 0))
		while True:
			for event in pg.event.get():
				if event.type == pg_local.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg_local.KEYUP:
					return
			pg.display.update()

	def start_game(self):
		dim = self.board.get_dim()
		game_start_surf = pg.Surface(dim).convert_alpha()
		back_color = pg.Color(35, 147, 46, 200)
		game_start_surf.fill(back_color)
		game_start_font = ComicWrites(game_start_surf, font_size = 50)
		game_start_press_any_font = ComicWrites(game_start_surf, font_size = 20)
		game_start_surf = game_start_font.get_write("Snakky!", (dim[0]/2, dim[1]/2), text_color = pg.Color(125, 237, 127))
		game_start_surf = game_start_press_any_font.get_write("Press any key to continue...", (dim[0]/2, dim[1]-20))
		self.disp_surf.blit(game_start_surf, (0, 0))
		snake = Snake(game_start_surf, self.board)
		while True:
			for event in pg.event.get():
				if event.type == pg_local.QUIT:
					pg.quit()
					sys.exit()
				if event.type == pg_local.KEYUP:
					return
			pg.display.update()

	def get_status(self, event):
		#print("inside get_status \<-->/")
		snake_body_coords = self.snake.get_body()
		apple_coords = self.apple.get_coords()
		to_append = []
		to_append.append(self.translate_event_to_number(event))
		to_append.append(apple_coords[0])
		to_append.append(apple_coords[1])
		for i in snake_body_coords:
			to_append.append(i[0])
			to_append.append(i[1])
		#print(to_append)
		return to_append

	def translate_event_to_number(self, event):
		if event == None:
			return 0
		elif event == 'left':
			return 1
		elif event == 'right':
			return 2
		elif event == 'up':
			return 3
		elif event == 'down':
			return 4

	def translate_number_to_event(self, number):
		if number  == 0:
			return None
		elif number == 1:
			return 'left'
		elif number == 2:
			return 'right'
		elif number == 3:
			return 'up'
		elif number == 4:
			return  'down'

class Capture:
	def __init__(self, filename="cap_events.csv"):
		self.filename = filename
		self.events = []
		self.cur_size = 0
		self.max_size = 60

	def submit_event(self, status = None, request_save = False):
		if not status == None:
			self.events.append(status)
			self.cur_size+=1
		if self.cur_size >= self.max_size or request_save == True:
			try:
				with open(self.filename, 'a') as fout:
					to_write = ''
					for i in self.events:
						to_write = ', '.join([str(v) for v in i]) + '\n'
						fout.write(to_write)
				self.events = []
				self.cur_size = 0
			except Exception as e:
				print("[Error] >> {!s}".format(e))

class MoveGenerate:
	def __init__(self, method = 'random'):
		self.method = method
		self.valid = [1, 2, 3, 4]

	def gen_move(self):
		if self.method == 'random':
			return self.__random_move()
		else:
			return self.__ai_move()

	def __random_move(self):
		return random.choice(self.valid)

	def __ai_move(self):
		pass