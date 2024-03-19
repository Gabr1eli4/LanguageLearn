import uuid
import Settings, Statistics

class User:
	id: int
	settings: Settings
	statistics: Statistics

	def __init__(self):
		if self.id == None:
			self.id = uuid.uuid4()
			self.settings = Settings()
			self.statistics = Statistics()

	def getUserSettings():
		pass

	def getUserStatistics():
		pass
