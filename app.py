# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print('mundo')
    return "hola mundo basura"

if __name__ == '__main__':
    print('initializing este cosa')
    app.run(debug=True, host='0.0.0.0', port=8080)
