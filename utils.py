from random import randint

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


def callback_query_answer():
	pass
