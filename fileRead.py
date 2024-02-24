import json

def readJson(path):
	with open(path, "r", encoding="utf-8") as file:
		return json.load(file)

def writeJson(path, data):
	with open(path, "w", encoding="utf-8") as file:
		json.dump(data, file, indent=4)


def get_words_of_topic(topics, title):
	words = [topic for topic in topics if topic["title"] == title][0]["words"]
	return words