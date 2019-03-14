
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入日志模块
from flask import Flask

from flask_sqlalchemy import  SQLAlchemy

from flask_restful import Api

app = Flask(__name__)

app.config.from_pyfile('../config.py')

db = SQLAlchemy(app)

api = Api(app)