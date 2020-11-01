import os


main="darknet.exe detector test data/coco.data yolov3.cfg yolov3.weights -i 0 -thresh 0.25 -dont_show people.jpg"
# os.popen(main)
# os.system(main)
content=os.popen(main).read()
print(content)
# time.sleep(10)
