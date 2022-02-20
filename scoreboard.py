import pygame

class ScoreBoard():
	#Табло для вывода результатов игры на экран

	def __init__(self, snake_game):
		self.sg = snake_game
		self.screen_rect = self.sg.screen.get_rect()
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

	def prep_score(self):
		#Преобразует текущий счет в графическое изображение.
		score_str = str(self.sg.stats.score)
		self.score_image = self.font.render(score_str, True,
							self.text_color, (0, 0, 0))
		self.score_rect = self.score_image.get_rect()
		self.score_rect.y = 20
		self.score_rect.right = self.screen_rect.right - 20

	def prep_level(self):
		#Преобразует текущий уровень в изображение
		level_str = str(len(self.sg.snake) - 3)
		self.level_image = self.font.render(level_str, True,
							self.text_color, (0, 0, 0))
		self.level_rect = self.level_image.get_rect()
		self.level_rect.topright = self.score_rect.bottomright
		self.level_rect.y += 20

	def prep_record(self):
		#Преобразует рекорд в изображение
		record_str = str(self.sg.stats.record)
		self.record_image = self.font.render(record_str, True,
							self.text_color, (0, 0, 0))
		self.record_rect = self.record_image.get_rect()
		self.record_rect.bottom = self.screen_rect.bottom - 20
		self.record_rect.right = self.screen_rect.right - 20


	def update(self):
		self.prep_score()
		self.sg.screen.blit(self.score_image, self.score_rect)
		self.prep_level()
		self.sg.screen.blit(self.level_image, self.level_rect)
		self.prep_record()
		self.sg.screen.blit(self.record_image, self.record_rect)