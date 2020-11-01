import tkinter
from tkinter import ttk
# from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory


file_path_str="D:/python_work/identify/image"


# 选择存储的文件夹

def selectPath(path_file):
    path_=askdirectory()
    # path_ = path_.replace("/", "\\\\")
    path_file.set(path_)
    file_path_str=path_file.get()
    print(path_file.get())
    # return file_path_str


def ui():
    # 主界面
    win=tkinter.Tk()
    win.title("人流量检测设置页面")
    win.geometry("700x500+250+100")
    # 禁止窗口拉伸
    win.resizable(width=False,height=False)

    # 阈值标签
    frame_threshold=tkinter.Frame(win)
    frame_threshold.pack(side=tkinter.TOP)

    label_threshold=tkinter.Label(frame_threshold,text="阈值").grid(row=0,column=0)
    entry_threshold=tkinter.Entry(frame_threshold).grid(row=0,column=1)


    # 上传时间间隔标签
    frame_interval=tkinter.Frame(win)
    frame_interval.pack(side=tkinter.TOP)

    label_interval=tkinter.Label(frame_interval,text="上传时间间隔").grid(row=0,column=0)

    # 下拉列表，选择时间间隔
    com=ttk.Combobox(frame_interval)
    com.grid(row=0,column=1)
    # 设置下拉数据
    com["value"]=("10秒","30秒","1分钟","3分钟","5分钟","10分钟","30分钟","1小时","3小时","5小时")
    # 设置默认值
    com.current(5)
    com.bind("<<ComboboxSelected>>")


    button=tkinter.Button(win,text="确认",width=10,height=1,command=win.quit)
    button.pack(side=tkinter.BOTTOM,pady=20)
    # button.place(x=300,y=450)




    # 选中的文件夹变量
    path_file=tkinter.StringVar()

    frame_file=tkinter.Frame(win)
    frame_file.pack(side=tkinter.BOTTOM,pady=40)
    label_file=tkinter.Label(frame_file,text="目标路径:").grid(row = 0, column = 0)
    entry_file=tkinter.Entry(frame_file,textvariable=path_file).grid(row = 0, column = 1)
    button_file=tkinter.Button(frame_file,text="路径选择",command=lambda :selectPath(path_file)).grid(row = 0, column = 2)


    # 上传地址
    path_upload=tkinter.StringVar()

    frame_upload_address=tkinter.Frame(win)
    frame_upload_address.pack(side=tkinter.TOP)
    label_upload_address=tkinter.Label(frame_upload_address,text="上传地址").grid(row=0,column=0)
    entry_upload_address=tkinter.Entry(frame_upload_address,textvariable=path_upload).grid(row=0,column=1)


    win.mainloop()


# # 调用图形界面程序
# ui()