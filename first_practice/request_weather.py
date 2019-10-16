import requests
from constants import WURL, KHABAROVSK_LAT, KHABAROVSK_LON, YANDEX_API_KEY


def make_request():
    # Делаем request:
    yandex_api_request = requests.get(
        WURL,
        params={
            'lon': KHABAROVSK_LON,
            'lat': KHABAROVSK_LAT,
        },
        # Передаём в заголовки API ключ от Яндекса:
        headers={'X-Yandex-API-Key': YANDEX_API_KEY},
    )
    return yandex_api_request


def recursive_parsing(json_response, values_list, *args):
    # Проверяем values_list на None. При 1 итерации должен быть True
    if values_list is None:
        values_list = []
    # Начинаем итерацию по ключу, значению в словаре json_response:
    for key, value in json_response.items():
        # Если значение является словарём вызываем эту же функцию.
        if isinstance(value, dict):
            recursive_parsing(value, values_list, *args)
        # Если строка, чисто или булево добавим в наш массив values_list:
        elif isinstance(value, (str, int, bool)):
            if key in args:
                values_list.append(f'{key} = {value}')
    # Вернём list получившийся из dict в открытом виде:
    return values_list


def parse_response(response, *args):
    # Вызываем метод приведения к dict у response:
    json_response = response.json()
    # Вернём результат функции recursive_parsing:
    return recursive_parsing(json_response, None, *args)


if __name__ == '__main__':
    # Получим данные о погоде в ХБК:
    yandex_response = make_request()
    # Распечатаем нужные нам значения из ответа:
    for item in parse_response(
            yandex_response,
            'url',
            'name',
            'temp',
            'season'
    ):
        print(item)
