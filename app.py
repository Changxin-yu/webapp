import os
from flask import Flask

app = Flask(__name__)

word = os.environ.get('APP_WORD')

@app.route('/')
def hello():
    return(word)

def main():
    app.run(host='127.0.0.1', port=5678, debug=False)


if __name__ == '__main__':
    main()
