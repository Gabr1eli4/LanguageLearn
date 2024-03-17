import requests
from config import TELEGRAM_API

class Message:
	def __init__(self, chat_id):
		self.chat_id = chat_id
		self.url = f"{TELEGRAM_API}"
		

	def sendMessage(self, text):
		method = "sendMessage"
		url = self.url + method
		data = { "chat_id": self.chat_id, "text": text }

		return requests.post(url, data)


	def sendReplyKeyboard(self, text, buttons):
		method = "sendMessage"
		url = self.url + method
		keyboard = { "keyboard": buttons, "resize_keyboard": True }
		data = { "chat_id": self.chat_id, "text": text, "reply_markup": keyboard }

		return requests.post(url, json=data)

	def sendInlineKeyboard(self, text, buttons):
		method = "sendMessage"
		url = self.url + method
		inline_keyboard = { "inline_keyboard": buttons }
		data = { "chat_id": self.chat_id, "text": text, "reply_markup": inline_keyboard }

		return requests.post(url, json=data)
	

	def answer_callback_query(self, callback_id):
		method = "answerCallbackQuery"
		url = self.url + method
		data = { "callback_query_id": callback_id }
		return requests.post(url, json=data)
