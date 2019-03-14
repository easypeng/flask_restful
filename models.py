#!/usr/bin/python
# -*- coding: utf-8 -*-

from config.flask_config import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict

    def query_username(self, username):
        obj = self.filter_by(username=username).first()
        return obj.password
		
if __name__ == "__main__":
	db.create_all()