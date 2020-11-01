import threading
import os
import time

global content

def output():
    global content
    main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 people.jpg"
    # main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 people.jpg"
    # content=None
    content = os.popen(main)#.readlines()
    print(content)

def main_test():
    # global content
    t=threading.Thread(target=output)
    t.setDaemon(True)
    t.start()
    # ids=os.getpid()

    time.sleep(15)
    # t.kill()
    # os.system("taskkill /F /IM darknet.exe")
    print(content)
    # print(ids)

    # t = threading.Thread(target=output)
    # t.setDaemon(True)
    # t.start()
    # ids=os.getpid()

    # time.sleep(15)

main_test()
