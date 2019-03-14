
#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from config.log_config import logHandler
from config.flask_config import api, app, db
from resource.user_resource import CreateUser
from dotenv import find_dotenv,load_dotenv
import os
load_dotenv(find_dotenv())
api.add_resource(CreateUser,'/CreateUser')

@app.route("/log")
def logTest():
    return "Code Handbook !! Log testing."

if __name__ == "__main__":

# set the log handler level
    logHandler.setLevel(logging.INFO)
# set the app logger level
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(logHandler)
    app.run(host=os.environ.get('FLASK_RUN_HOST'),port=os.environ.get('FLASK_RUN_PORT'),debug=False)
