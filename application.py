# -*- coding: utf-8 -*-

from flask import Flask
from tree.views import tree_app

app = Flask(__name__)
app.register_blueprint(tree_app)

class Project(object):
    def __init__(self, *args):
        pass
        
    @app.route("/")
    def index():
        return "Hello, World!"

    def start(self):
        app.run(debug=True)