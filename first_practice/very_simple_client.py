import requests
from constants import LURL, LPORT
from random import randint
from time import sleep


def make_request():
    # Генерируем рандомные числа в list-compr. и посылаем их на сервер в цикле:
    for number in [randint(1, 100) for i in range(5)]:
        # Логгируем запрос:
        print(f'Будет отправлено число: {number}')
        # Запрос методом GET:
        response = requests.get(
            # URL запроса:
            url=f'http://{LURL}:{LPORT}',
            # Параметры запросы (наше случайное число):
            params={
                'number': number,
            }
        )
        # Печатаем поступивший ответ:
        print(f'Поступил ответ с числом: {response.json()["response"]}')
        # Просим программу заснуть на 3 секунды.
        sleep(5)


if __name__ == '__main__':
    # Запускаем приложение-клиент
    make_request()
