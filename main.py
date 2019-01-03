
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import userauthor.register
import userauthor.login
import ssl

from tornado.options import define, options
define("port", default=1024, help="run on the given port", type=int)
# template_path = os.path.join(os.path.dirname(__file__), "API")

# 路由
router = [
    # 登录
    (r"/login", userauthor.login.LoginRequestHandler),
    # 注册
    (r"/register", userauthor.register.RegisterHandler),
	(r"/getcode", userauthor.getcode.GetCode)
]

def main():
    print('start web server!')
    # 监听命令行
    tornado.options.parse_command_line()
    # app = tornado.web.Application(router, template_path)
    app = tornado.web.Application(router)
    # 开启服务
    http_server = tornado.httpserver.HTTPServer(app)
    # 监听端口
    http_server.listen(options.port)
    # I/O循环
    tornado.ioloop.IOLoop.instance().start()
    # 取消ssl验证
    ssl._create_default_https_context = ssl._create_unverified_context

# 主入口
if __name__ == "__main__":
    main()