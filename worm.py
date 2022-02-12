import pygame

class Worm(list):
	#Определяет саму змейку

	def __init__(self, sg):
		super().__init__()
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
				pass
			else:
				self[0].y_cell = self[-1].y_cell - 1
				self[0].x_cell = self[-1].x_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		elif self.d_flag:
			if self[-1].y_cell == (self.u_length - 1):
				pass
			else:
				self[0].y_cell = self[-1].y_cell + 1
				self[0].x_cell = self[-1].x_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		elif self.r_flag:
			if self[-1].x_cell == (self.u_length - 1):
				pass
			else:
				self[0].x_cell = self[-1].x_cell + 1
				self[0].y_cell = self[-1].y_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]
		elif self.l_flag:
			if self[-1].x_cell == 0:
				pass
			else:
				self[0].x_cell = self[-1].x_cell - 1
				self[0].y_cell = self[-1].y_cell
				self.append(self.pop(0))
				self[-1].rect.topleft = self.field.coordinates[self[-1].x_cell][self[-1].y_cell]