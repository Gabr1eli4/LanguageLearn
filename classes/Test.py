import json

class Test:
	words = []
	topic = ""

	def __init__(self, topic):
		with open("settings/test.json", "r", encoding="utf-8") as file:
			data = json.load(file)
			self.topic = [t for t in data["topics"] if t["title"] == topic]
			self.words = self.test["words"]

	def get_words(self):
		return self.words

	def get_test(self):
		return self.test
	

	def generateTest(self, count):
		buttons = []
		row = []

		for i in range(count):
			translate = self.words[i]["translate"]
			row.append( { "text": translate, "callback_data": translate } )
			if i % 2 == 1 and len(row) >= 1:
				buttons.append(row)
				row = []
		
		return buttons

	
	def setTopicWordAsLearned(self, word):
		for word in self.words:
			if word["word"] == word:
				word["isLearned"] = True
				break
