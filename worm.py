import pygame

class Worm(list):
	#Определяет саму змейку

	def __init__(self, sg):
		super().__init__()
		self.snake_game = sg
		self.field = sg.field
		self.u_length = sg.settings.u_length
		self.u_flag = False
		self.d_flag = False
		self.r_flag = False
		self.l_flag = False

	def move_it(self):
		#Движения змейки
		if self.u_flag:
			if self[-1].y_cell == 0:
				self.snake_game.end_game()
			else:
				self[0].y_cell = self[-1].y_cell - 1
				self[0].x_cell = self[-1].x_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		elif self.d_flag:
			if self[-1].y_cell == (self.u_length - 1):
				self.snake_game.end_game()
			else:
				self[0].y_cell = self[-1].y_cell + 1
				self[0].x_cell = self[-1].x_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		elif self.r_flag:
			if self[-1].x_cell == (self.u_length - 1):
				self.snake_game.end_game()
			else:
				self[0].x_cell = self[-1].x_cell + 1
				self[0].y_cell = self[-1].y_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		elif self.l_flag:
			if self[-1].x_cell == 0:
				self.snake_game.end_game()
			else:
				self[0].x_cell = self[-1].x_cell - 1
				self[0].y_cell = self[-1].y_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		for i in range(len(self)-1):
			if (self[-1].x_cell == self[i].x_cell) and (self[-1].y_cell == self[i].y_cell):
				self.snake_game.end_game()
		if (self.snake_game.free_unit.x_cell == self[-1].x_cell and 
						self.snake_game.free_unit.y_cell == self[-1].y_cell):
			self.snake_game.free_unit.color = (0, 200, 0)
			self.insert(0, self.snake_game.free_unit)
			self.snake_game._create_free_unit()
			self.snake_game.stats.score += int(20 * self.snake_game.settings.speed) 
			self.snake_game.settings.speed += 0.5