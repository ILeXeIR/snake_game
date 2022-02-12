import sys
import pygame
import random
from settings import Settings
from field import Field
from unit import Unit
from worm import Worm

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
		self.snake = Worm(self)


	def run_game(self):
		#Запускает один цикл игры

		while True:
			self._check_events()
			self.snake.move_it()
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
				if event.key == pygame.K_c:
					self._creat_snake()
				if event.key == pygame.K_UP and not self.snake.d_flag:
					self.snake.u_flag = True
					self.snake.l_flag = False
					self.snake.r_flag = False
				if event.key == pygame.K_DOWN and not self.snake.u_flag:
					self.snake.d_flag = True
					self.snake.l_flag = False
					self.snake.r_flag = False
				if event.key == pygame.K_RIGHT and not self.snake.l_flag:
					self.snake.r_flag = True
					self.snake.u_flag = False
					self.snake.d_flag = False
				if event.key == pygame.K_LEFT and not self.snake.r_flag:
					self.snake.l_flag = True
					self.snake.u_flag = False
					self.snake.d_flag = False

	def _creat_snake(self):
		#Создает новую змейку.

		for i in range(3):
			unit = Unit(self)
			unit.x_cell = 10
			unit.y_cell = 19 - i
			unit.rect.topleft = self.field.coordinates[unit.x_cell][unit.y_cell]
			self.snake.append(unit)

	def _update_screen(self):
		#Обновляет изображения на экране, отображает экран.

		self.screen.fill((0, 0, 0))
		self.field.draw_field()
		for unit in self.snake:
			unit.draw_unit()

		#Отображение последнего прорисованного экрана.
		pygame.display.flip()
		self.clock.tick(self.settings.speed)


if __name__ == '__main__':
	#Создание экземпляра и запуск игры.
	sg = SnakeGame()
	sg.run_game()