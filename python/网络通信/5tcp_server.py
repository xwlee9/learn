import socket


def main():
    # socket 创建一个套接字
    s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind绑定ip和port
    s_tcp.bind(("",9988))

    # listen使得套接字变为可以被动连接
    s_tcp.listen(128) # 最大连接客户端数
    while True:  # 循环为多个客户端服务
    # accept 等待客户端  
        #  监听套接字负责等待新的客户端进行连接 
        #  accept 负责产生新的套接字为客户端进行服务
        print("----------waiting for client --------------")
        s_new_cilent, client_addr = s_tcp.accept()
        print ("-------------accept from %s----------------" % str(client_addr))
        # print (s_new_cilent)  # 套接字 <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('172.16.141.1', 9988), raddr=('172.16.141.140', 49178)>
        # print (client_addr)  # 客户端地址
        while True:  # 循环为同一个客户端服务多次
        # 接收客户端发送过来的请求
            rx_data = s_new_cilent.recv(1024)
            print("the data is :", rx_data)
        # recv解堵塞 两种方式：
        #   1. 客户端发送数据
        #   2. 客户端调用close导致 recv解堵塞
            if rx_data:
                # 回送数据 
                s_new_cilent.send("accpet successful!".encode('utf-8'))
            else:
                break

        #关闭套接字
        s_new_cilent.close()
        print ("the data is done!!!")
    s_tcp.close()  # 监听套接字


if __name__ == "__main__":
    main()