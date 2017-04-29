#!/usr/bin/env python
# Basic restful server
# author: aiporre
# Usage: python app.py
# Dependencies: flask.

from flask import Flask, render_template, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class UserAPI(Resource):
    def __init__(self):
        self.cnt = 0

    def get(self, id):
        print 'id' +  str(id)
        return self.cnt

    def put(self, id):
        self.cnt += 1
        print 'cnt ' + str(self.cnt)
        pass

    def delete(self, id):
        self.cnt = 0
        pass

api.add_resource(UserAPI, '/users/<int:id>', endpoint = 'user')


#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# def wait_minute():
#     import time
#     time.sleep(60)
#
#
# def gen():
#     frame = 0
#     while True:
#         wait_minute()
#         frame += 1
#         yield (frame)
#
# @app.route('/data')
# def data_feed():
#     return "data"
#

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
