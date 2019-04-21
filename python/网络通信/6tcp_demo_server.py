import socket


def send_file_2_client(s_new_cilent,client_addr):
    # 接收客户端需要下载的文件名
    file_name = s_new_cilent.recv(1024).decode('utf-8')
    print("the slient %s the file name is : %s" % (str(client_addr), file_name))
    # 打开文件 读取内容
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception:
        print("this is no file: ", file_name)

    # 发送文件数据给客户端
    if file_content:
        s_new_cilent.send(file_content)
    else:
        s_new_cilent.send("there is no file!!!".encode('utf-8'))




def main():
    # 1 socket 创建一个套接字
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2 bind绑定ip和port
    s_tcp.bind(("",9987))

    # 3 listen使得套接字变为可以被动连接
    s_tcp.listen(128)
    while  True:
        # 4 等待客户端连接 accept()
        print("----------waiting for client --------------")
        s_new_cilent, client_addr = s_tcp.accept()
        print ("-------------accept from %s----------------" % str(client_addr))

        # 5 调用发送文件函数 完成客户端服务
        send_file_2_client(s_new_cilent,client_addr)

            #关闭套接字
        s_new_cilent.close()
        print ("the data is done!!!")
    s_tcp.close()  # 监听套接字


if __name__ == "__main__":
    main()