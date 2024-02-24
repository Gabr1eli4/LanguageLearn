from random import randint
from fileRead import readJson, writeJson

def check_message(data: dict, message: str) -> bool:
	return "message" in data and "text" in data["message"] and data["message"]["text"] == message


def generate_test(words):
	buttons = []
	for _ in range(2):
		row = []
		for _ in range(2):
			index = randint(0, len(words) - 1)
			translate = words[index]["translate"]
			row.append({ "text": translate, "callback_data": translate })
		buttons.append(row)

	return buttons


def get_word(words):
	index = randint(0, len(words) - 1)
	word = words[index]["word"]
	userSettings = readJson("settings/userSettings.json")
	userSettings["currentWord"] = word
	writeJson("settings/userSettings.json", userSettings)
	return word
