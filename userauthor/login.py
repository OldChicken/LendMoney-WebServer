#!/usr/bin/env python
#coding:utf-8

import tornado.web
import json
from dbmanager.mysqlmanager import MysqlHandler
from dbmanager.user import UserInfo
import datetime
import jwt


# 登录请求类
class LoginRequestHandler(tornado.web.RequestHandler):

    async def post(self):

        account = self.get_body_argument("account")
        password = self.get_body_argument("password")
        # account = form.mobile.data
        # password = form.password.data
        re_data = {}
        userdata = UserInfo()
        user = await userdata.getUser(account)
        if user:
            valid_code = await user.check_password(account,password) 
            if valid_code:
                data = {
                'id':user.id,
                'nick_name':user.user_phone,
                'exp':datetime.datetime.utcnow()
                }
                # 生成json web token
                token = jwt.encode(data, 'secret_key', algorithm='HS256')
                re_data['id'] = user.id
                re_data['token'] = token.decode('utf8')
 
            else:
                self.set_status(400)
                re_data['non_fields'] = '用户名或者密码错误'
        else:
            self.set_status(400)
            re_data['account'] = '用户不存在'


        self.finish(re_data)




