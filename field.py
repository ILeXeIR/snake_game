import pygame
import math

class Field():
	#Определение игрового поля, по которому может двигаться змейка

	def __init__(self, sg):
		self.screen = sg.screen
		self.screen_rect = self.screen.get_rect()
		self.color = (230, 230, 230)
		self.length = math.floor(sg.screen_height/sg.settings.u_length)*sg.settings.u_length
		self.unit_length = self.length/sg.settings.u_length

		self.rect = pygame.Rect(0, 0, self.length, self.length)
		self.rect.center = self.screen_rect.center

		self.coordinates = []
		x, y = self.rect.x, self.rect.y
		for i in range(sg.settings.u_length):
			self.coordinates.append([])
			for j in range(sg.settings.u_length):
				self.coordinates[i].append((x, y))
				y += self.unit_length
			x += self.unit_length

	def draw_field(self):
		pygame.draw.rect(self.screen, self.color, self.rect)