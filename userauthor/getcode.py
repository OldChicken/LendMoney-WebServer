#!/usr/bin/env python
#coding:utf-8
import asyncio
 
from urllib.parse import urlencode
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
import json
 
from tornado import web
from forms import SmsForm
from random import choice
import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options 
import redis_handler

#生成注册验证码
class GetCode(RedisHandler):
    def create_code(self):
        # 创建四位数短信验证码
        seeds = '01234566789'
        code = []
        for i in range(4):
            code.append(choice(seeds))
        return ''.join(code)
    
    def post(self):
        phone = self.get_body_argument("user_phone")
        tp = self.get_body_argument("type")
        code = self.create_code()
        text = {'user_phone':phone,'content':'您的验证码为' + code}
        resp = json.dumps(text)
        self.redis_conn.set('{}_{}'.format(mobile, code), 1, 5*60)
        self.write(resp)
        self.set_header('Content-Type','application/json;charset=utf-8')
