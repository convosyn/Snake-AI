import numpy as np

class Preprocess:
	def __init__(self, file_in, file_out):
		self.file_in = file_in
		self.file_out = file_out

	def _initialize(self):
		self.board = [[0 for i in range(32)] for j in range(24)]

	def __stablise(self):
		try:
			with open(self.file_in) as fin, open(self.file_out, 'wb') as fout:
				for row in fin:
					self._initialize()
					to_list = row.split(', ')
					to_list_int = [int(i.strip()) for i in to_list]
					label = to_list_int[0]
					del to_list_int[0]
					apple_coords = (to_list_int[1], to_list_int[2])
					del to_list_int[0]
					del to_list_int[0]
					rmv = False
					for v in to_list_int:
						if v < 0 or v > 23 or v > 47:
							rmv = True
					if rmv:
						continue
					snake_coords = []
					for i in range(0, len(to_list_int), 2):
						snake_coords.append((to_list_int[i], to_list_int[i+1]))
					self.board[apple_coords[1]][apple_coords[0]] = 2
					for coord in snake_coords:
						self.board[coord[1]][coord[0]] = 1
					board = np.array(self.board)
					board = board.flatten().reshape((1, -1))
					board = np.column_stack([label, board])
					np.savetxt(fout, board)
		except Exception as e:
			print("<Error> !! {!s}".format(e))

	def pre_process(self):
		self.__stablise()