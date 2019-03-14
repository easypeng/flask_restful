
#!/usr/bin/python
# -*- coding: utf-8 -*-

# 引入日志模块
from config.log_config import logHandler
from config.flask_config import api, app, db
from flask_restful import reqparse, Resource
from models import User
import json
class CreateUser(Resource):
    def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser()
            parser.add_argument('username', type=str, help='username to create user')
            parser.add_argument('email', type=str, help='Email address to create user')
            parser.add_argument('password', type=str, help='Password to create user')
            args = parser.parse_args()
            _userName = args['username']
            _userEmail = args['email']
            _userPassword = args['password']
            newobj = User(username=_userName, email=_userEmail, password=_userPassword)
            dbUser  = User.query.filter_by(username=_userName).first()
            if dbUser != None and dbUser.password == _userPassword :
                return {'error': 'user has exists'}
            db.session.add(newobj)
            db.session.commit()
            listUser = db.session.query(User).all()
            objList = []
            for u in listUser:
                objList.append(u.to_json())
            return objList
        except Exception as e:
            return {'error': str(e)}


