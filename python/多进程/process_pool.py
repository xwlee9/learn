import multiprocessing
import os, time, random

def worker(i):
    time_start = time.time()
    print ("the pid is: ",os.getpid())
    time.sleep(random.random()*2)
    time_stop = time.time()
    print(i, "end!!! use %0.3f" % (time_stop-time_start))

po = multiprocessing.Pool(3) # 定义一个进程池 最大进程为3

for i in range(10):
    # Pool().apply_async(要调用的目标,(传递的目标为元祖,))
    # 每次循环将会在空闲出来的子进程去调用目标
    po.apply_async(worker,(i,))
    """
    apply_async(func[, args[, kwds[, callback]]]) 非阻塞，
    apply(func[, args[, kwds]])是阻塞的
    """
"""
创建一个进程池pool，并设定进程的数量为3，因pool指定进程数为3，所以0、1、2会直接送到进程中执行，当其中一个执行完事后才空出一个进程处理下一个，
因为为非阻塞，主函数会自己执行，无视其他进程的执行，直接输出--------start---------
所以运行完for循环后直接输出---------end----------，主程序在pool.join()处等待各个进程的结束。

"""
print("--------start---------")
po.close() # 关闭进程池 关闭后不再接受新的请求
po.join() # 等待po中所有的子进程执行完 必须放在close之后 执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
print("---------end----------")