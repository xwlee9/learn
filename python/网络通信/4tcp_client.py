import socket


def main():
    # 创建tcp套接字
    s_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 连接服务器
    dst_ip = input("please input the dst ip: ")
    dst_port = int(input("please input the dst port: "))
    s_addr = (dst_ip,dst_port)
    s_tcp.connect(s_addr)

    # 发送数据
    send_data = input("please input the data: ")
    s_tcp.send(send_data.encode('utf-8'))

    # 关闭套接字
    s_tcp.close()


if __name__ == "__main__":
    main()