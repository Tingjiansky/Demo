
import http.server
import socketserver
import socket


'''
1. 在cmd运行 python -m http.server 8000 --bind 127.0.0.1 --directory /tmp/
   开启该目录的http服务
   不指定目录则在cmd当前的目录开启
2. 使用脚本运行，在脚本运行的目录开启http服务
3. 脚本模式暂不支持指定目录，需优化
'''


def main(path):
    ip = socket.gethostbyname(socket.gethostname())
    # print(ip)
    port = 8080
    print("提示，请在浏览器中输入 http://%s:%d 进行访问" % (str(ip), port))
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", port), Handler) as httpd:
        print("serving at port", port)

        httpd.serve_forever()


if __name__ == '__main__':
    # dir = input('请输入需要开启ftp的目录路径：\n')
    dir = r'F:\Seafile\Seafile\测试工作'
    main(dir)
