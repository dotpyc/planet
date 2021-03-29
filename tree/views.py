# -*- coding: utf-8 -*-

import os
from flask import Blueprint, render_template

tree_app = Blueprint('tree', __name__, template_folder="templates", static_folder="tree")

class Project(object):
    def __init__ (self, *args):
        pass
    
    @tree_app.route("/tree")
    def tree():
        return render_template("tree.html")
