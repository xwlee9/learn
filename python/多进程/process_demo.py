import multiprocessing
import os


def cp_file(filename, old_foldername, new_foldername, q):
    # print("====>from %s to %s copy file: %s" % (old_foldername, new_foldername, filename))
    # old_f = open(old_foldername + '/' + filename, 'rb')
    old_f = open(os.path.join(old_foldername, filename), 'rb')

    content = old_f.read()
    old_f.close()

    # new_f = open(new_foldername + '/' + filename, 'wb')
    new_f = open(os.path.join(new_foldername, filename), 'wb')
    new_f.write(content)
    new_f.close()
    
    q.put(filename)


def main():
# 获取用户要copy的文件夹的名字
    folder_testname = '/Users/li/Desktop/temp_code/muti_process/yaleB39'
    # old_foldername = input("please input the folder name: ")
    old_foldername = folder_testname
# 创建一个新的文件夹
    try:
        new_foldername = old_foldername + "[new]"
        # new_foldername = os.path.join(old_foldername, )
        os.mkdir(new_foldername)
    except:
        pass

# 复制文件夹的所有的待拷贝的文件夹的名字 listdir()
    filenames = os.listdir(old_foldername)

# 创建进程池
    po = multiprocessing.Pool(5)

#创建队列
    q = multiprocessing.Manager().Queue() 
    #pool中的进程间通信需要使用Manager


# 复制文件夹的文件 到新的文件夹中去
    for filename in filenames:
        po.apply_async(cp_file, args=(filename, old_foldername, new_foldername, q))
    
    po.close()
    # po.join()
    l = len(filenames)
    for i in range(l):
        file_name = q.get()
        # print("file: %s is done! " % file_name)
        print("\r进度为: %.2f %%" % (((i+1)/l)*100) ,end='')
    
    print()
    
    # print("     ====> end!!!")

if __name__ == "__main__":
    main()

