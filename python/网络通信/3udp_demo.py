import socket


def send_msg(s_udp):
    """发送消息"""
    dst_ip = input("please input the dst ip: ")
    dst_port = int(input("please input the dst port: "))
    send_data = input("please input the data: ")
    s_udp.sendto(send_data.encode("utf-8"), (dst_ip,dst_port))


def rec_msg(s_udp):
    """接收消息"""
    rx_data = s_udp.recvfrom(1024)
    print("%s : %s" % (str(rx_data[1]),rx_data[0].decode('gbk')))

def main():
    # 创建套接字
    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定信息
    s_udp.bind(("", 8899))

    # 循环处理      套接字可以同时收发数据 全双工 
    while True:
        print ("*********chat**********")
        print ("1:send message!")
        print ("2:receive message!")
        print ("0:exit!")
        op = input("Please input the function:")
        
        if op == '1':
            send_msg(s_udp)
        elif op == '2':
            rec_msg(s_udp)
        elif op == '0':
            break
        else:
            print ("WRONG INPUT!")  

    s_udp.close()

if __name__ == "__main__":
    main()
