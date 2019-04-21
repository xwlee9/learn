import socket

def main():
    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    localaddr = ("", 53918)
    s_udp.bind(localaddr)
    while True:
        # 接收数据
        rx_data = s_udp.recvfrom(1024)  # 最大的字节数
        # 接收到的数据为一个元祖(接收到的数据，(发送方ip，prot))
        rx_msg = rx_data[0]  # 存储接收到的数据
        rx_addr = rx_data[1]  # 存储发送的地址

        # print(rx_data)
        # print("%s: %s"%(str(rx_addr), rx_msg.decode('utf-8')))
        print("%s: %s"%(str(rx_addr), rx_msg.decode('gbk')))

    s_udp.close()

if __name__ == "__main__":
    main()