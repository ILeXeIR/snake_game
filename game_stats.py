class GameStats():
	#Игровая статистика

	def __init__(self):

		self.score = 0
		self.filename = 'record.txt'
		with open(self.filename, 'r') as file_object:
			self.record = int(file_object.readline().strip())

	def reset_stats(self):
		self.score = 0

	def check_record(self):
		if self.score > self.record:
			self.record = self.score
			with open(self.filename, 'w') as file_object:
				file_object.write(str(self.score))



