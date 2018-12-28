#!/usr/bin/env python
#coding:utf-8

import tornado.web
import json
import dbmanager.mysqlmanager

# 登录请求类
class LoginRequestHandler(tornado.web.RequestHandler):

    def get(self):

        account = self.get_argument("account")
        password = self.get_argument("password")
        resp = self.matchUser(account, password)
        self.write(json.dumps(resp, indent=2))
        self.set_header('Content-Type', 'application/json;charset=utf-8')


    def post(self):

        account = self.get_body_argument("account")
        password = self.get_body_argument("password")
        resp = self.matchUser(account, password)
        self.write(json.dumps(resp, indent=2))
        self.set_header('Content-Type', 'application/json;charset=utf-8')


    # 数据库匹配,成功后返回成功信息
    def matchUser(self, account, password):
        print('account', account)
        print('password', password)
        if dbmanager.mysqlmanager.matchUser(account, password) == True:
            resp = {
                'data': {
                    'account': account,
                    'password': password
                },
                'msg': {
                    'success': '1',
                    'msg': 'login success!'
                }
            }
        else:
            resp = {
                'data': {
                },
                'msg': {
                    'success': '0',
                    'msg': 'login failed!'
                }
            }
        return resp


