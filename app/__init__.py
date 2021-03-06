#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Module init file"""

from app import routes
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "MYSUPERSECRETSTRING"
