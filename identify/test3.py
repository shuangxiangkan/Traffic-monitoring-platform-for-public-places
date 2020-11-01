import threading
import time

global a

def run():
    global a
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    a=3
    time.sleep(2)


# if __name__ == '__main__':
def main_test():
    start_time = time.time()

    print('这是主线程：', threading.current_thread().name)
    # thread_list = []
    # for i in range(5):
    #     t = threading.Thread(target=run)
    #     thread_list.append(t)

    # for t in thread_list:
    #     t.setDaemon(True)
    #     t.start()
    t=threading.Thread(target=run)
    t.setDaemon(True)
    t.start()

    time.sleep(10)

    print('主线程结束了！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)
    print(a)

main_test()