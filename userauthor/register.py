#!/usr/bin/env python
#coding:utf-8

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json
import dbmanager.mysqlmanager
import userauthor.getcode
from dbmanager.RedisHandler import RedisHandler
from userauthor.forms import SmsForm

# 注册请求类
class RegisterHandler(RedisHandler):
 
    async def post(self, *args, **kwargs):
        params = json.loads(self.request.body.decode('utf8'))
        form = RegisterForm.from_json(params)
        re_data = {}
        if form.validate():
            mobile = form.mobile.data
            code = form.code.data
            password = form.password.data
 
 
            # 验证码验证
            try:
                code_result = int(self.redis_conn.get('{}_{}'.format(mobile, code)))
            except TypeError as e:
                code_result = ''
                self.set_status(400)
                re_data['code'] = '验证码过期'
 
            if code_result == 1:
                valid_code = True
            else:
                self.set_status(400)
                re_data['code'] = '验证码有误'
                valid_code = False
 
            # 验证号码是否注册
            if valid_code:
                result = await self.searchUser(mobile)
                if result:
                    self.set_status(400)
                    re_data['mobile'] = '用户已经存在'
                else:
                    await self.addNewUser(mobile,password)
                    self.set_status(201)
 
        else:
            self.set_status(400)
            for fields in form.errors:
                re_data[fields] = form.errors[fields][0]
 
        self.finish(re_data)


 