import threading
import time
from queue import Queue
"""
threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

线程模块提供了Thread类来处理线程，Thread类提供了以下方法:

run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。

"""
def thread_job():
    print("this is the added thread, the number is %s"%threading.current_thread())
    time.sleep(1)
    print ("T1end!!!!!!!!!!!!!!!!")

def thread_job2():
    print('*'*20)
    print('='*20)

def main():
    # print(threading.active_count())
    # print(threading.enumerate())
    # print(threading.current_thread())
    added_thread = threading.Thread(target=thread_job, name = 'T1')
    added_thread2 = threading.Thread(target=thread_job2, name = 'T2')
    added_thread.start() # 线程要调用start方法
    added_thread.join()  # 将此进程加入到主进程中此时等上面的线程结束后才会执行后面的
    added_thread2.start()  # 此时T2 与 主线程 并发
    print("ALL DONE *************")
# main() #多线程

# =======================================队列
"""
Python中，队列是线程间最常用的交换数据的形式。Queue模块是提供队列操作的模块

put()方法在队尾插入。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1。
    如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。

get()方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()就使调用线程暂停，
    直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。

q.qsize() 返回队列的大小
q.empty() 如果队列为空，返回True,反之False
q.full() 如果队列满了，返回True,反之False
q.full 与 maxsize 大小对应
q.get([block[, timeout]]) 获取队列，timeout等待时间
q.get_nowait() 相当q.get(False)
非阻塞 q.put(item) 写入队列，timeout等待时间
q.put_nowait(item) 相当q.put(item, False)
q.task_done() 在完成一项工作之后，q.task_done() 函数向任务已经完成的队列发送一个信号
q.join() 实际上意味着等到队列为空，再执行别的操作
"""
def job(l,q,j):
    for i in range(len(l)):
        l[i] = l[i]**2
    time.sleep(6-j)
    q.put(l) 

def multiThreading():
    q = Queue()
    threads = []
    data = [[1,2,3],[4,5,6],[7,8,9],[9,9,9],[8,8,8]]
    # u = threading.Thread(target=job,args=(data[0], q))
    # u.start()
    # # time.sleep(1)
    # threads.append(u)
    for i in range(0,5):
        t = threading.Thread(target=job,args=(data[i],q,i))
        t.start()
        print(threading.currentThread())
        # t.join()  # 若在此时加入主线程 ==》[[1, 4, 9], [16, 25, 36], [49, 64, 81], [81, 81, 81], [64, 64, 64]]
        threads.append(t)
    # for thread in threads:
    #     thread.join()     #若此时加入主线程 意义不大
        
    result = []
    for _ in range(5):
        result.append(q.get())
    print (result)

# multiThreading()

"""
锁  线程同步 
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，
    对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。

"""
def job1():
    global A,lock
    lock.acquire()
    for _ in range(10):
        A += 1
        print("job1",A)
    lock.release()
    
def job2():
    global A,lock
    lock.acquire()
    for _ in range(10):
        A += 10
        print ("job2",A)
    lock.release()
lock = threading.Lock()
A = 0
def main_lock():
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
# main_lock()

"""
继承 一定要重写父类的run方法 面向对象 class 
派生类中重写了父类threading.Thread的run()方法，其他方法（除了构造函数)都不应在子类中被重写，在子类中只有_init_()和run()方法被重写。

start()方法 开始线程活动。
    对每一个线程对象来说它只能被调用一次，它安排对象在一个另外的单独线程中调用run()方法（而非当前所处线程）。
    当该方法在同一个线程对象中被调用超过一次时，会引入RuntimeError(运行时错误)。

run()方法
    代表了线程活动的方法。
    你可以在子类中重写此方法。标准run()方法调用了传递给对象的构造函数的可调对象作为目标参数，如果有这样的参数的话，顺序和关键字参数分别从args和kargs取得。
"""
class MyThread(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter        
    def run(self):
        print ("开始线程：" + self.name)
        print(self.name, self.counter, 5)
        time.sleep(1)
        print ("退出线程：" + self.name)

t1 = MyThread(1,"Thread1",1)
t2 = MyThread(2,"Thread2",2)
t1.start()
t2.start()

