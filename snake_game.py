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
		self.stop_game = True
		self.game_prepared = True

		self._create_snake()
		self._create_free_unit()


	def run_game(self):
		#Запускает один цикл игры

		while True:
			self._check_events()
			if not self.stop_game:
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
				if not self.stop_game:
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
				if self.stop_game:
					if event.key == pygame.K_SPACE and not self.game_prepared:
						self.prepare_new_game()
					if event.key == pygame.K_UP and self.game_prepared:
						self.stop_game = False
						self.game_prepared = False
						self.snake.u_flag = True


	def _create_snake(self):
		#Создает новую змейку

		for i in range(3):
			unit = Unit(self)
			unit.x_cell = 10
			unit.y_cell = 19 - i
			unit.rect.topleft = self.field.coordinates[unit.x_cell][unit.y_cell]
			self.snake.append(unit)

	def _create_free_unit(self):
		#Создает на поле свободный юнит

		self.free_unit = Unit(self)
		self.free_unit.color = (0, 0, 200)
		while True:
			self.free_unit.x_cell = random.randint(0, self.settings.u_length - 1)
			self.free_unit.y_cell = random.randint(0, self.settings.u_length - 1)
			for unit in self.snake:
				if (self.free_unit.x_cell == unit.x_cell and 
						self.free_unit.y_cell == unit.y_cell):
					break
			else:
				break
		self.free_unit.rect.topleft = \
			self.field.coordinates[self.free_unit.x_cell][self.free_unit.y_cell]



	def end_game(self):
		#Конец игры.

		self.snake.u_flag = False
		self.snake.d_flag = False
		self.snake.l_flag = False
		self.snake.r_flag = False
		self.stop_game = True

	def prepare_new_game(self):
		#Создать новую игру, но не запускать ее

		self.snake.clear()
		self._create_snake()
		self._create_free_unit()
		self.game_prepared = True


	def _update_screen(self):
		#Обновляет изображения на экране, отображает экран.

		self.screen.fill((0, 0, 0))
		self.field.draw_field()
		for unit in self.snake:
			unit.draw_unit()
		self.free_unit.draw_unit()

		#Отображение последнего прорисованного экрана.
		pygame.display.flip()
		self.clock.tick(self.settings.speed)


if __name__ == '__main__':
	#Создание экземпляра и запуск игры.
	sg = SnakeGame()
	sg.run_game()