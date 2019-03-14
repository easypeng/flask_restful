
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入日志模块
from logging.handlers import RotatingFileHandler

logHandler = RotatingFileHandler('info.log', maxBytes=100000, backupCount=10)
