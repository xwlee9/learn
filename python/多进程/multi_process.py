import multiprocessing
import time

def fun1():
    while True:
        print("1------------")
        time.sleep(1)


def fun2():
    while True:
        print("2------------")
        time.sleep(1)

def download_data(q):
    data = [11,22,33,44,55]
    for temp in data:
        q.put(temp)
    
    print("put all data to queue!!!")

def process_data(q):
    data_store = []
    while True:
        data = q.get()
        data_store.append(data)

        if q.empty():
            break
    print(data_store)

def main():
    # p1 = multiprocessing.Process(target= fun1)
    # p2 = multiprocessing.Process(target= fun2)
    # p1.start()
    # p2.start()

    q = multiprocessing.Queue()
    p3 = multiprocessing.Process(target= download_data, args=(q,))
    p4 = multiprocessing.Process(target= process_data, args=(q,))
    p3.start()
    p4.start()


if __name__ == "__main__":
    main()