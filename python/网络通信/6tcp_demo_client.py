import socket
import sys

def main():

# 创建套接字
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 目的信息 服务器的ip和port
    dst_ip = input("please input the dst ip: ")
    dst_port = int(input("please input the dst port: "))
    s_addr = (dst_ip,dst_port)

# 连接服务器
    s.connect(s_addr)

# 输入需要下载的文件名
    download_filename = input("please input the file name: ")

# 发送文件下载请求
    s.send(download_filename.encode('utf-8'))

# 接受对方发送来的数据 最大接受1024个字节
    rx_data = s.recv(1024)

# 如果接收成功 创建文件 否则不创建文件
    if rx_data:
        with open("New" + download_filename, "wb") as f:
            f.write(rx_data)

# 关闭套接字
    s.close()

if __name__ == "__main__":
    main()







