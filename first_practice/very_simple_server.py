from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
def request_handler(request):
    # Парсим поступивший запрос и достаём информацию:
    parse_number = int(request.raw_args['number'])

    # Логгируем поступившее число в консоль:
    print(f'Поступил запрос с числом: {parse_number}')

    # Умножаем число на 2, перед ответом:
    response = parse_number * 2

    # Возвращаем ответ:
    print(f'Дан ответ {response}')

    return json({
        'response': response
    })


if __name__ == '__main__':
    # Запускаем приложение-сервер:
    app.run(host='0.0.0.0', port=3000)
