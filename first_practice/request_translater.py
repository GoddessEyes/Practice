import requests
from constants import API_TKEY, TURL, LANG_TCODE


def make_translate(text='Привет мир!', lang=LANG_TCODE[0]):
    # Делаем запрос на Яндекс.Переводчик:
    yandex_response = requests.post(
        url=TURL,
        params={
            'key': API_TKEY,
            'text': text,
            'lang': lang
        }
    )
    # Возвращаем результат:
    return yandex_response


def parse_response(response):
    # Приводим ответ в удобный нам вид и просим дать ключ `text`:
    text = response.json().get('text')
    # Проверяем является ли переменная `text` list`ом:
    if isinstance(text, list):
        # Если да вернём первое значение из list`а:
        return text[0]
    else:
        # Если нет вернём как есть:
        return text


if __name__ == '__main__':
    # Вызываем функцию make_request и ложим результат в переменную
    response = make_translate(
        'I love the Python programming language',
        LANG_TCODE[1]
    )
    # Передаём результат в след. функцию для парсинга:
    result = parse_response(response)
    # После полученного результата логгируем его:
    print(f'Результат перевода: {result}')
