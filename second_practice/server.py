from flask import Flask

app = Flask('1234')

@app.route('/')
def get_index():
    return '<b>Привет Мир</b>'

app.run('0.0.0.0', 3000)

