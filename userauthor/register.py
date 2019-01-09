#!/usr/bin/env python
#coding:utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
from dbmanager.mysqlmanager import MysqlHandler
import userauthor.getcode
from dbmanager.redismanager import RedisHandler
from userauthor.forms import SmsForm
import redis

# 注册请求类
class RegisterHandler(tornado.web.RequestHandler):
 
    async def post(self):
        mobile = self.get_body_argument("account")
        password = self.get_body_argument("password")
        code = self.get_body_argument("code")
        re_data = {}
        # 验证码验证
        try:
            redis_conn = redis.Redis(host='localhost', port='6379',password='')
            code_result = redis_conn.get('{}_{}'.format(mobile, code))
        except TypeError as e:
            code_result = ''
            self.set_status(400)
            re_data['code'] = '验证码过期'
 
        if code_result == b'1':
            valid_code = True
        else:
            self.set_status(400)
            re_data['code'] = '验证码有误'
            valid_code = False
 
        # 验证号码是否注册
        if valid_code:
            sqlmanager = MysqlHandler()
            result = await sqlmanager.searchUser(mobile)
            if result:
                self.set_status(400)
                re_data['mobile'] = '用户已经存在'
            else:
                await sqlmanager.addUser(mobile,password)
                self.set_status(201)
 
        self.finish(re_data)


 