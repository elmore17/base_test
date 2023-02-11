from bs4 import BeautifulSoup
import requests


number = int(input("Введите номер задания: "))



def number_one():
	print("Ответ на 1 задание:\n1)Проверил бы логи\n2)Вторым вариантом я бы попробовал дебажить код\n3)Подробнее бы ознакомился с документацией API")

def result(res):
		print(res)

def create_handlers(callback):
	handlers:list = []
	for step in range(5):
		handlers.append(lambda step=step:callback(step))
	return handlers

def execute_handlers(handlers:list):
	for handler in handlers:
		handler()

execute_handlers(create_handlers(result))


def number_three():
	file = open("site.txt", encoding="utf8")
	soup = BeautifulSoup(file, "html.parser")
	a = len([tag.name for tag in soup.find_all()])
	print ("Количество HTML-тегов: " + str(a))
	attrs = 0
	for elm in soup():
	    attrs += len(list(elm.attrs.keys()))
	print("Количество атрибутов: " + str(attrs))

if number == 1:
	number_one()
elif number == 3:
	number_three()
	