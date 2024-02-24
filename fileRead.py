import json

def readJson(path):
	with open(path, "r") as file:
		return json.load(file)

def writeJson(path, data):
	with open(path, "w") as file:
		json.dump(data, file, indent=4)


def get_words_of_topic(topics, title):
	words = [topic for topic in topics if topic["title"] == title][0]["words"]
	return words