#!/usr/bin/env python
#coding:utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import dbmanager.mysqlmanager

# 注册请求类
class RegisterRequestHandler(tornado.web.RequestHandler):

    def get(self):
        new_phone = self.get_argument("account")
        user_password = self.get_argument("password")
        resp = self.registerUser(new_phone, user_password)
        self.write(json.dumps(resp, indent=2))
        self.set_header('Content-Type', 'application/json;charset=utf-8')

    def post(self):
        new_phone = self.get_body_argument("account")
        user_password = self.get_body_argument("password")
        resp = self.registerUser(new_phone, user_password)
        self.write(json.dumps(resp, indent=2))
        self.set_header('Content-Type', 'application/json;charset=utf-8')


    def registerUser(self, new_phone, password):
        # 注册用户,成功后返回成功信息
        # 注：这里可能还需要一些帐号、密码格式的校验，客户端若校验过，则可省略
        # 注：实际注册流程中，需要先发送验证码，此处省略此流程，搜索不到手机号直接注册
        print('account', new_phone)
        print(password)
        if dbmanager.mysqlmanager.searchUser(new_phone) == False:
            dbmanager.mysqlmanager.addNewUser()
            resp = {
                'data': {
                    'phone': new_phone,
                    'password': password
                },
                'msg': {
                    'success': '1',
                    'msg': 'register success!'
                }
            }
        else:
            resp = {
                'data': {
                },
                'msg': {
                    'success': '0',
                    'msg': 'register faled!'
                }
            }
        return resp