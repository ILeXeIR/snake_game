import pygame
from pygame.sprite import Sprite

class Unit(Sprite):
	#Класс для определения одной клетки поля

	def __init__(self, sg):
		super().__init__()
		self.screen = sg.screen
		#self.screen_rect = self.screen.get_rect()
		self.color = (0, 200, 0)

		self.rect = pygame.Rect(0, 0, sg.field.unit_length, sg.field.unit_length)
		#self.rect.center = self.screen_rect.center


	def draw_unit(self):
		pygame.draw.rect(self.screen, self.color, self.rect)