from sendMessage import send_keyboard, send_inline_keyboard, send_message
from fileRead import get_words_of_topic
from utils import generate_test, get_word


completedQuestions = 0
isAnswerRight = False

def start_handler(chat_id):
	buttons = [
		[{"text": "Начать тест"}],
		[{"text": "Статистика"}],
		[{"text": "Настройки параметров"}],
	]
	send_keyboard(chat_id, buttons, "Меню")


def test_start_handler(chat_id, topics):
	buttons = []

	for topic in topics:
		buttons.append([{ "text": topic["title"] }])
	send_keyboard(chat_id, buttons, "Выберите тему")


def answer_handler(chat_id, topics, topicTitle, answer, currentWord):
	message = ""
	if (answer == currentWord):
		message = "Верно!!!"
	else:
		message = "Сори, не в этот раз"
	words = get_words_of_topic(topics, topicTitle)
	buttons = generate_test(words)
	send_inline_keyboard(chat_id, buttons, message)


def topic_handler(chat_id, data, topics, choosenTopic):
	choosenTopic = data["message"]["text"]
	words = get_words_of_topic(topics, choosenTopic)

	buttons = generate_test(words)
	word = get_word(words)

	send_inline_keyboard(chat_id, buttons, word)


def statistic_handler(chat_id):
	send_message(chat_id, "Ну вот тебе статистика")


def settings_handler(chat_id):
	send_message(chat_id, "Найстроки так настройки")