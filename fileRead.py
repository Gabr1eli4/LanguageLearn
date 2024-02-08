import json

def readJson(path):
	with open(path, "r") as file:
		return json.load(file)


def get_words_of_topic(topics, title):
	words = [topic for topic in topics if topic["title"] == title][0]["words"]
	return words