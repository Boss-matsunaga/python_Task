from flask import Flask, session
app = Flask(__name__)
app.secret_key = 'hogehoge'

@app.route('/')
def index():
    session['name'] = 'taro'
    session['name'] = 'ziro'
    name = session.get('name')
    print(name)
    return 'hello'

if __name__ == '__main__':
    app.run(debug = True)