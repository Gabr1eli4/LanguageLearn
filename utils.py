from datetime import datetime
from random import choice
from fileRead import readJson, writeJson
index = 0

def check_message(data: dict, message: str) -> bool:
	return "message" in data and "text" in data["message"] and data["message"]["text"] == message


def generate_test(words):
	buttons = []
	row = []
	for i in range(4):
		translate = words[i]["translate"]
		print(translate)
		row.append({ "text": translate, "callback_data": translate })
		if i % 2 == 1 and len(row) >= 1:
			buttons.append(row)
			row = []

	return buttons


def writeCurrentWord(word, translate):
	userSettings = readJson("settings/userSettings.json")
	userSettings["currentWord"] = word
	userSettings["currentTranslate"] = translate
	writeJson("settings/userSettings.json", userSettings)	


def get_random_words(words):
	randomWords = []
	while len(randomWords) < 4:
		word = choice(words)
		if word not in randomWords:
			randomWords.append(word)
	
	return randomWords


def get_word(words):
	userSettings = get_user_settings()
	userSettings["currentWord"] = word
	userSettings["currentTranslate"] = translate
	writeJson("settings/userSettings.json", userSettings)
	return word


def get_user_settings():
	return readJson("settings/userSettings.json")
	

def get_statistics():
	return readJson("settings/statistics.json")


def clearUserSettings():
	userSettings = readJson("settings/userSettings.json")
	userSettings["currentTopic"] = ""
	userSettings["currentTranslate"] = ""
	userSettings["currentWord"] = ""
	userSettings["topicRightAnswers"] = 0
	writeJson("settings/userSettings.json", userSettings)


def clearStatistics():
	stats = readJson("settings/statistics.json")
	for topic in stats["topics"]:
		topic["learnedWords"] = 0
	writeJson("settings/statistics.json", stats)

def setStatisticsDate(currentTopic):
	data = readJson("settings/statistics.json")
	for topic in data["topics"]:
		if topic["topic"] == currentTopic:
			topic["dateOfLastTest"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	print("stats = ", data)
	writeJson("settings/statistics.json", data)


def clearUserSettings():
	userSettings = get_user_settings()
	userSettings["currentTopic"] = ""
	userSettings["currentWord"] = ""
	userSettings["currentTranslate"] = ""
	userSettings["topicRightAnswers"] = 0
	print("userSettings = ", userSettings)
	writeJson("settings/userSettings.json", userSettings)