#!/usr/bin/env python
# Basic restful server
# author: aiporre
# Usage: python app.py
# Dependencies: flask.

from flask import Flask, render_template, Response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def wait_minute():
    import time
    time.sleep(60)


def gen():
    frame = 0
    while True:
        wait_minute()
        frame += 1
        yield (frame)


@app.route('/data')
def video_feed():
    return Response(gen())


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
