import sys
import pygame
import random
from settings import Settings
from field import Field
from unit import Unit

class SnakeGame:
	#Класс для управления ресурсами и поведением игры.

	def __init__(self):
		#Инициализирует игру и создает игровые ресурсы.

		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.screen_width, self.screen_height = pygame.display.get_desktop_sizes()[0]
		pygame.display.set_caption('Snake Game')
		self.clock = pygame.time.Clock()

		self.field = Field(self)
		self.snake = pygame.sprite.Group()

	def run_game(self):
		#Запускает один цикл игры

		while True:
			self._check_events()
			self._update_screen()


	def _check_events(self):
		#Проверяет и реагирует на события.

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				#Реагирует на нажатия клавиш.
				if event.key == pygame.K_ESCAPE:
					sys.exit()

	def _creat_snake(self):
		#Создает новую змейку.

		unit = Unit(self)
		#unit.rect = self.field.coordinates[10][10]
		unit.rect.center = self.field.rect.center

		self.snake.add(unit)

	def _update_screen(self):
		#Обновляет изображения на экране, отображает экран.

		self.screen.fill((0, 0, 0))
		self.field.draw_field()
		for unit in self.snake.sprites():
			unit.draw_unit()

		#Отображение последнего прорисованного экрана.
		pygame.display.flip()
		self.clock.tick(30)


if __name__ == '__main__':
	#Создание экземпляра и запуск игры.
	sg = SnakeGame()
	sg.run_game()