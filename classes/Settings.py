import json

class Settings:
	def __init__(self, id):
		with open("", encoding="utf-8") as file:
			self.data = json.load(file)

	def setSetting(key, value):
		pass