#!/usr/bin/env python
#coding:utf-8

import tornado.web
import json
from dbmanager.mysqlmanager import mysqlhandler


# 登录请求类
class LoginRequestHandler(tornado.web.RequestHandler):

    async def post(self):

        account = self.get_body_argument("account")
        password = self.get_body_argument("password")
        account = form.mobile.data
		password = form.password.data
		re_data = {}
		try:
			user = await self.application.objects.get(User, mobile=mobile)
                if user.password.check_password(password):
                    data = {
                        'id':user.id,
                        'nick_name':user.nick_name,
                        'exp':datetime.utcnow()
                    }
                    # 生成json web token
                    token = jwt.encode(data, self.settings['secret_key'], algorithm='HS256')
                    re_data['id'] = user.id
                    re_data['token'] = token.decode('utf8')
 
                else:
                    self.set_status(400)
                    re_data['non_fields'] = '用户名或者密码错误'
 
            except User.DoseNotExist:
                self.set_status(400)
                re_data['mobile'] = '用户不存在'
 
        else:
            self.set_status(400)
            re_data['non_fields'] = '用户名或者密码错误'
 
        self.finish(re_data)




