import socket
import threading


def recv_msg(s_udp):
    while True:
        rx_data = s_udp.recvfrom(1024)
        print (rx_data)


def send_msg(s_udp,dst_ip,dst_port):
    while True:
        tx_data = input("please input the data:")
        s_udp.sendto(tx_data.encode('utf-8'), (dst_ip, dst_port))


def main():
    #创建套接字
    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    s_udp.bind(("", 8899))

    # ip port
    dst_ip = input("please input the ip: ")
    dst_port = int(input("please input the port: "))

    # 创建两个线程
    t_rx = threading.Thread(target=recv_msg, args=(s_udp,))
    t_tx = threading.Thread(target=send_msg, args=(s_udp,dst_ip,dst_port))

    t_tx.start()
    t_rx.start()


if __name__ == "__main__":
    main()