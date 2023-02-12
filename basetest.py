from bs4 import BeautifulSoup
import requests
from art import tprint
import http.client


tprint('TEST', font='bulbhead')
def number_one():
	print("Задание №1: ")
	print("Ответ на 1 задание:\n1)Проверил бы логи\n2)Вторым вариантом я бы попробовал дебажить код\n3)Подробнее бы ознакомился с документацией API")

number_one()
print("\n")

print("Задание №2: ")
def result(res):
	print(res)

# Код к заданию 2, были типизированы некоторые строки, и исправлена строка "lambda: callback(step)" 
def create_handlers(callback):
	handlers:list = []
	for step in range(5):
		handlers.append(lambda step=step:callback(step))
	return handlers

def execute_handlers(handlers:list):
	for handler in handlers:
		handler()

execute_handlers(create_handlers(result))
# Конец кода к 3 заданию
print("\n")
def number_three():
	print("Задание №3: ")
	file = open("site.txt", encoding="utf8")
	soup = BeautifulSoup(file, "html.parser")
	a = len([tag.name for tag in soup.find_all()])
	print ("Количество HTML-тегов: " + str(a))
	attrs = 0
	for elm in soup():
	    attrs += len(list(elm.attrs.keys()))
	print("Количество атрибутов: " + str(attrs))

number_three()
print("\n")

def number_four():
	my_ip = http.client.HTTPConnection("ifconfig.me")
	my_ip.request("GET", "/ip")
	print("Текущий публичный IP-адрес: " + my_ip.getresponse().read().decode('utf-8'))
print("Задание 4: ")
number_four()