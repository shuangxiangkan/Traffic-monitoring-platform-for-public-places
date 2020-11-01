import cv2
import os
import json
import datetime
from threading import Lock,Thread

lock=Lock()
file=None


# 获取本地摄像头
# folder_path 截取图片的存储目录
def get_img_from_camera_local(upload_address,folder_path,screenshot_interval,threshold):
    global file
    cap = cv2.VideoCapture(0)
    # 每10秒钟截一次图片
    time_interval=datetime.timedelta(seconds=screenshot_interval)
    # 开始时间
    start_time=datetime.datetime.now()
    while True:
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        #当前时间
        current_time=datetime.datetime.now()
        times=int((current_time-start_time).total_seconds())%int(time_interval.total_seconds())
        if times==0:
            photo_name=current_time.strftime("%Y%m%d%H%M%S")
            # 存储为图像
            cv2.imwrite(folder_path + photo_name  + '.jpg', frame)
            data=write_to_json(folder_path, threshold)
            send(upload_address, data)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


def  traverse_image_file(folder_path):
    # dirs="D:/python_work/identify/image"
    dirs=folder_path
    # dirs=path_str
    myList=os.listdir(dirs)
    return myList


def write_to_json(folder_path,threshold):
    # 阈值，识别出的人数大于等于阈值，才会将其写入json文件中
    # threshold=9
    pictures_name_list=traverse_image_file(folder_path)
    i=0
    number_data = {}
    for picture_name in pictures_name_list:
        # main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 image/" + picture_name
        main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 "+ folder_path + picture_name
        f=os.popen(main)
        data=f.readlines()
        f.close()
        print(data)
        # 人数
        count=0
        for value in data:
            if "person" in value:
                count+=1

        if count>=threshold:
            i+=1
            data={"data" + str(i): {"locationName": 'Soochow_university', 'peopleNum': count,
                               'currentSj': picture_name.strip(".jpg")}}
            return data
            # number_data.update({"data"+str(i):{"locationName":'Soochow_university','peopleNum':count,'currentSj':picture_name.strip(".jpg")}})


    # 写入json文件
    # with open("record.json","w") as f:
    #     json.dump(number_data,f,indent=4)

def send(upload_address,data):
        # url = 'http://10.10.64.221:8088/saveTraffic'
        url = upload_address
        with open("record2.json", "a+") as f:
            json.dump(data,f,indent=4)

        # for key in all_data.keys():
        #     print(all_data[key])
            # r=requests.post(url,all_data[key])
            # print(r.text)

upload_address='http://10.10.64.221:8088/saveTraffic'
folder_path="D://test//"
screenshot_interval=10
threshold=1

get_img_from_camera_local(upload_address,folder_path,screenshot_interval,threshold)