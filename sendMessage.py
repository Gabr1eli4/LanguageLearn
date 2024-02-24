import json
import requests
from config import TELEGRAM_API

def send_message(chat_id, text=""):
	method = "sendMessage"
	url = f"{TELEGRAM_API}/{method}"
	data = { "chat_id": chat_id, "text": text }

	requests.post(url, data)


def send_keyboard(chat_id, buttons=[[{}]], text=""):
	method = "sendMessage"
	url = f"{TELEGRAM_API}/{method}"
	keyboard = { "keyboard": buttons, "resize_keyboard": True }
	data = { "chat_id": chat_id, "text": text, "reply_markup": keyboard }

	requests.post(url, json=data)

def send_inline_keyboard(chat_id, buttons, text):
	method = "sendMessage"
	url = f"{TELEGRAM_API}/{method}"
	inline_keyboard = { "inline_keyboard": buttons }
	data = { "chat_id": chat_id, "text": text, "reply_markup": inline_keyboard }

	requests.post(url, json=data)


def answer_callback_query(callback_id):
	answerMethod = "answerCallbackQuery"
	url = f"{TELEGRAM_API}/{answerMethod}"
	data = { "callback_query_id": callback_id }
	requests.post(url, json=data)
