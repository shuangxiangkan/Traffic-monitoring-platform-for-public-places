from get_image_from_video import get_img_from_camera_local
from get_output import write_to_json
from data_send import send
import threading
import json
import os


folder_path="D:\\test\\"
screenshot_interval=30
threshold=1
upload_address='http://10.10.64.221:8088/saveTraffic'

def get_img():
    while True:
        path = "D:/test"
        ls = os.listdir(path)
        count = 0
        for i in ls:
            if os.path.isfile(os.path.join(path, i)):
                count += 1
        print(count)
        if count<=100:
            get_img_from_camera_local(folder_path,screenshot_interval)

def write_to():
    write_to_json(folder_path,threshold)

def send_data():
    send(upload_address)

def main():
    threads=[]
    t1=threading.Thread(target=get_img)
    threads.append(t1)
    t2 = threading.Thread(target=write_to)
    threads.append(t2)
    t3 = threading.Thread(target=send_data)
    threads.append(t3)

    for thread in threads:
        thread.start()

    for threads in threads:
        threads.join()

    print("ALL DONE")

get_img()