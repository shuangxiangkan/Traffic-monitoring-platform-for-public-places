import os
import json
from data_send import send


def  traverse_image_file(folder_path):
    # dirs="D:/python_work/identify/image"
    dirs=folder_path
    # dirs=path_str
    myList=os.listdir(dirs)
    return myList

def  delete_files(folder_path):
    # dirs="D:/python_work/identify/image"
    dirs=folder_path
    # dirs=path_str
    myList=os.listdir(dirs)
    for i in myList:
        file_path=folder_path+i
        os.remove(file_path)
        print("delete...................")

# folder_path="D:/test"
# delete_files(folder_path)

# def write_to_json(folder_path,threshold):
    # # 阈值，识别出的人数大于等于阈值，才会将其写入json文件中
    # # threshold=9
    # pictures_name_list=traverse_image_file(folder_path)
    # i=0
    # number_data = {}
    # for picture_name in pictures_name_list:
    #     # main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 image/" + picture_name
    #     main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 "+ folder_path + picture_name
    #     f=os.popen(main)
    #     data=f.readlines()
    #     f.close()
    #     print(data)
    #     # 人数
    #     count=0
    #     for value in data:
    #         if "person" in value:
    #             count+=1
    #
    #     if count>=threshold:
    #         # x={"picture_"+str(i):count}
    #         i+=1
    #
    #         # 当前时间，并将其转换为字符串
    #         # now_time = datetime.datetime.now()
    #         # now_str = now_time.strftime("%Y%m%d%H%M")
    #         # 写入json文件中的数据，分别是：地点，人数，时间
    #
    #         number_data.update({"data"+str(i):{"locationName":'Soochow_university','peopleNum':count,'currentSj':picture_name.strip(".jpg")}})
    #
    # # 写入json文件
    # with open("record2.json","w") as f:
    #     json.dump(number_data,f,indent=4)
    #
    # delete_files(folder_path)

def write_to_json(folder_path, threshold, upload_address,detect_location):
    # 阈值，识别出的人数大于等于阈值，才会将其写入json文件中
    # threshold=9
    # lock.acquire()
    pictures_name_list = traverse_image_file(folder_path)
    if pictures_name_list:
        i = 0
        number_data = {}
        for picture_name in pictures_name_list:
            # main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 image/" + picture_name
            # main = "darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 " + folder_path + picture_name
            # main="darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 -dont_show people.jpg"
            main="darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 -dont_show "+ folder_path + picture_name
            f = os.popen(main)
            data = f.readlines()
            f.close()
            print(data)
            # 人数
            count = 0
            for value in data:
                if "person" in value:
                    count += 1

            if count >= threshold:
                # x={"picture_"+str(i):count}
                i += 1

                # 当前时间，并将其转换为字符串
                # now_time = datetime.datetime.now()
                # now_str = now_time.strftime("%Y%m%d%H%M")
                # 写入json文件中的数据，分别是：地点，人数，时间

                number_data.update({"data" + str(i): {"locationName": detect_location, 'peopleNum': count,
                                                      'currentSj': picture_name.strip(".jpg")}})

        # 图片中的人数超过阈值，才将其写入json文件中
        if number_data:
            # 写入json文件
            with open("record.json", "w") as f:
                json.dump(number_data, f, indent=4)

            print(upload_address)
            # 发送数据给云端
            send(upload_address)

        delete_files(folder_path)

    # lock.release()









# folder_path="D:/test/"
# write_to_json(folder_path,1)


