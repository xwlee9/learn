import socket
def main():
    # s_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s_tcp.close()

    s_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    
    dest_addr = ('172.16.141.140',8080)
    s_udp.bind(("",8899))

    while True:
        send_data = input("please input the data:")
        if send_data == 'exit':
            break
        # s_udp.sendto(b"nice", dest_addr)
        s_udp.sendto(send_data.encode('utf-8'),dest_addr)
    s_udp.close()
if __name__ == "__main__":
    main()