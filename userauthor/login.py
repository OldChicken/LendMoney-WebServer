#!/usr/bin/env python
#coding:utf-8

import tornado.web
import json
from dbmanager.mysqlmanager import MysqlHandler


# 登录请求类
class LoginRequestHandler(tornado.web.RequestHandler):

    def get(self):

        account = self.get_argument("account")
        password = self.get_argument("password")
        sqlmanager = MysqlHandler()
        resp = sqlmanager.matchUser(account, password)
        self.write(json.dumps(resp, indent=2))
        self.set_header('Content-Type', 'application/json;charset=utf-8')


    def post(self):

        account = self.get_body_argument("account")
        password = self.get_body_argument("password")
        sqlmanager = MysqlHandler()
        resp = sqlmanager.matchUser(account, password)
        self.write(json.dumps(resp, indent=2))
        self.set_header('Content-Type', 'application/json;charset=utf-8')




