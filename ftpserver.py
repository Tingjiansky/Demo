
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket

'''
1. 打开目录，中文乱码
pyftpdlib内部使用utf8，而windows使用gbk，可以将pyftpdlib进行修改：
filesystems.py  将所有的utf8 换成 gbk
handlers.py 将所有的utf8 替换成 gbk
重新CMD执行
python -m pyftpdlib -p 21
2. 编译环境运行，报错
任务管理器中关闭python后台后再试
'''


def main(dir):
    # 自动获得本机ip地址
    # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # ip = s.getsockname()[0]
    ip = socket.gethostbyname(socket.gethostname())
    port = 21

    print("提示，请在资源管理器中输入 ftp://%s:%d 进行访问" % (ip, port))

    authorizer = DummyAuthorizer()
    # 添加  用户名/密码/ftp目录。当目录用"."表示.py文件当前所在的目录
    authorizer.add_user("admin", "123456", dir, perm="elradfmwM")
    # 添加匿名访问时的 ftp目录
    # authorizer.add_anonymous(dir, perm="elradfmwM")
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # 设置ftp的本地或者ip地址/端口，可以根据自己的实际情况修改ip和端口即可。
    # server = FTPServer(("0.0.0.0", 21), handler)
    # server = FTPServer(("127.0.0.1", 21), handler)
    server = FTPServer((ip, port), handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 10

    server.serve_forever()

    return ip, port


if __name__ == '__main__':
    dir = input('请输入需要开启ftp的目录路径：\n')
    # dir = r'F:\Seafile\Seafile\测试工作'
    ip, port = main(dir)
    # print("提示，请在资源管理器中输入 ftp://%s:%d 进行访问", (ip, port))
