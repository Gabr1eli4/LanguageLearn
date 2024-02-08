import json
from flask import Flask, request
from utils import check_message
from handlers import start_handler, test_start_handler, topic_handler, statistic_handler, settings_handler, answer_handler
from fileRead import readJson

topics = readJson("settings/test.json")["topics"]
titles = [topic["title"] for topic in topics]
choosenTopic = ""

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def message_processing():
	data = request.json
	print(json.dumps(data, indent=2))
	chat_id = data["message"]["chat"]["id"]

	# Обработка сообщения /start
	if check_message(data, "/start"):
		start_handler(chat_id)
		return '', 200

	# Начать теста
	if check_message(data, "Начать тест"):
		test_start_handler(chat_id, topics)
		return '', 200

	# Выбор теста
	if data["message"]["text"] in titles and len(choosenTopic) == 0:
		topic_handler(chat_id, data, topics, choosenTopic)
		return '', 200

	# Проверка теста
	if "callback_query" in data and len(choosenTopic) != 0:
		print(data["callback_query"])
		answer = data["message"]["text"]
		answer_handler(chat_id, data, choosenTopic, topics, answer)

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
