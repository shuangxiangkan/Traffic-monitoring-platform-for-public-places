import tkinter
from tkinter import ttk
from tkinter.filedialog import askdirectory
from get_output import write_to_json


win=tkinter.Tk()
file_path_str = "D:/python_work/identify/image"
cv=tkinter.StringVar()
interval="5min"
threshold_value=tkinter.StringVar()
upload_address=tkinter.StringVar()
flag=False




def get_threshold():
    print(threshold_value)
    return threshold_value


def create_threshold():

    # 阈值标签
    frame_threshold = tkinter.Frame()
    frame_threshold.pack(side=tkinter.TOP)

    label_threshold = tkinter.Label(frame_threshold, text="阈值").grid(row=0, column=0)
    # entry_threshold = tkinter.Entry(frame_threshold,textvariable=self.threshold_value).grid(row=0, column=1)
    com_threshold=com = ttk.Combobox(frame_threshold,textvariable=threshold_value)
    com_threshold.grid(row=0, column=1)
    # 设置下拉数据
    com_threshold["value"] = ("1人", "3人", "5人", "10人", "20人", "30人", "50人", "100人")
    # 设置默认值为只要图片中超过3人就将其保存到json文件中
    com_threshold.current(1)
    com_threshold.bind("<<ComboboxSelected>>")

# 返回时间间隔
def getinterval(event):
    print(cv.get())

# 创建上传时间间隔控件
def create_interval():
    # 上传时间间隔标签
    frame_interval = tkinter.Frame()
    frame_interval.pack(side=tkinter.TOP)

    label_interval = tkinter.Label(frame_interval, text="上传时间间隔").grid(row=0, column=0)

    # 下拉列表，选择时间间隔
    com = ttk.Combobox(frame_interval,textvariable=cv)
    com.grid(row=0, column=1)
    # 设置下拉数据
    com["value"] = ("10秒", "30秒", "1分钟", "3分钟", "5分钟", "10分钟", "30分钟", "1小时", "3小时", "5小时")
    # 设置默认值为5分钟
    com.current(5)
    com.bind("<<ComboboxSelected>>",getinterval)

def End_UI():
    flag=True
    # win.quit()
    win.destroy()

# 确认按钮控件
def create_confirm():
    button = tkinter.Button(text="确认", width=10, height=1, command=End_UI)
    button.pack(side=tkinter.BOTTOM, pady=20)

# 选择文件夹
def selectPath(path_file):
    path_ = askdirectory()
    path_file.set(path_)
    file_path_str = path_file.get()

# 创建选择街区图片文件夹控件
def create_filepath():
    # 选中的文件夹变量
    path_file = tkinter.StringVar()

    frame_file = tkinter.Frame()
    frame_file.pack(side=tkinter.BOTTOM, pady=40)
    label_file = tkinter.Label(frame_file, text="目标路径:").grid(row=0, column=0)
    entry_file = tkinter.Entry(frame_file, textvariable=path_file).grid(row=0, column=1)
    button_file = tkinter.Button(frame_file, text="路径选择", command=lambda: selectPath(path_file)).grid(row = 0, column = 2)

# 输入上传地址控件
def create_uploadpath():
    # 上传地址
    # path_upload = tkinter.StringVar()

    frame_upload_address = tkinter.Frame()
    frame_upload_address.pack(side=tkinter.TOP)
    label_upload_address = tkinter.Label(frame_upload_address, text="上传地址").grid(row=0, column=0)
    entry_upload_address = tkinter.Entry(frame_upload_address, textvariable=upload_address).grid(row=0, column=1)



def draw():
    create_threshold()
    create_interval()
    create_filepath()
    create_uploadpath()
    create_confirm()

    win.mainloop()


def ui():
    win.title("人流量检测设置页面")
    win.geometry("700x500+250+100")
    # 禁止窗口拉伸
    win.resizable(width=False,height=False)

    # 存放图片的文件夹的变量

    # Combobox绑定的变量
    cv.set("10分钟")

    # 阈值变量
    threshold_value.set("3人")
    # 上传地址变量
    draw()



def conversion_interval(time_str):
    second_str = 0
    if time_str == "10秒":
        second_str = 10
    elif time_str == "30秒":
        second_str=30
    elif time_str=="1分钟":
        second_str=60
    elif time_str=="3分钟":
        second_str=3*60
    elif time_str=="5分钟":
        second_str=5*60
    elif time_str=="10分钟":
        second_str=10*60
    elif time_str=="30分钟":
        second_str=30*60
    elif time_str=="1小时":
        second_str=1*60*60
    elif time_str=="3小时":
        second_str=3*60*60
    elif time_str=="5小时":
        second_str=5*60*60
    return second_str

def conversion_threshold(threshold_str):
    threshold_num = 0
    if threshold_str == "1人":
        threshold_num = 1
    elif threshold_str == "3人":
        threshold_num=3
    elif threshold_str=="5人":
        threshold_num=5
    elif threshold_str=="10人":
        threshold_num=10
    elif threshold_str=="20人":
        threshold_num=20
    elif threshold_str=="30人":
        threshold_num=30
    elif threshold_str=="50人":
        threshold_num=50
    elif threshold_str=="100人":
        threshold_num=100
    return threshold_num







def function():
    print("1")
    file_path=file_path_str.replace("/","\\\\")+"\\\\"
    print(file_path)
    print("file_path:",file_path)
    screenshot_interval = conversion_interval(cv.get())
    print("3")
    threshold_str = conversion_threshold(threshold_value.get())
    print("4")
    # 从视频中截取图片存入相应的文件夹
    # get_img_from_camera_local(file_path,screenshot_interval)

    # 将截图中的人数统计出来并将其输入到json文件中
    write_to_json(file_path,threshold_str)
    print("5")



ui()
print(flag)
if flag:
    function()