import json
from flask import Flask, request
from utils import check_message
from handlers import start_handler, test_start_handler, topic_handler, statistic_handler, settings_handler, answer_handler
from fileRead import readJson, writeJson

topics = readJson("settings/test.json")["topics"]
titles = [topic["title"] for topic in topics]

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def start():
	data = request.json
	print(json.dumps(data, indent=2, ensure_ascii=False))
	if "message" in data and "chat" in data["message"] and "id" in data["message"]["chat"]:
		chat_id = data["message"]["chat"]["id"]
	else:
		chat_id = data["callback_query"]["message"]["chat"]["id"]

	# Обработка сообщения /start
	if check_message(data, "/start"):
		start_handler(chat_id)
		return '', 200

	# Начать теста
	if check_message(data, "Начать тест"):
		test_start_handler(chat_id, topics)
		return '', 200

	# Выбор теста
	if "message" in data and "text" in data["message"] and data["message"]["text"] in titles:
		currentTopic = data["message"]["text"]
		userSettings = readJson("settings/userSettings.json")
		userSettings["currentTopic"] = currentTopic
		writeJson("settings/userSettings.json", userSettings)
		topic_handler(chat_id, data, topics, currentTopic)
		return '', 200

	# Проверка теста
	if "callback_query" in data:
		userSettings = readJson("settings/userSettings.json")
		answer = data["callback_query"]["data"]
		answer_handler(chat_id, topics, userSettings["currentTopic"], answer, userSettings["currentWord"])
		return '', 200

	# Статистика
	if check_message(data, "Статистика"):
		statistic_handler(chat_id)
		return '', 200

	# Настройка параметров
	if check_message(data, "Настройка параметров"):
		settings_handler(chat_id)
		return '', 200
	
	return 'Сообщение я конечно получил, но что на него отвечать я хз', 200


if __name__ == "__main__":
	app.run(debug=True)
