from flask import Flask, request
from pytube import YouTube


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hi"


@app.route('/download', methods=['GET'])
def download():
    url = request.args.get('url', default='', type=str)

    return YouTube(url).streams.filter(type="audio").first().download(".\\songs\\")


if __name__ == '__main__':
    app.run()
