# 教程地址
# https://www.youtube.com/watch?v=_wXmXBpCAfc&list=PLSCgthA1Anie_vHuCOt3hCXN6HIl8Ph8u
# https://www.bilibili.com/video/BV1FW411q7Js/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=063688d5c8c4383c4904f31ff18868a8
# https://wwbk.lanzouq.com/iT8yR1ll9bdc
import tkinter as tk
from tkinter import *
import os
import requests
import random
import time
#程序创作：陈浩涵
#联系方式:
#Telegram:https://t.me/IWantMoreMoneyIWillRice
#QQ:3522689565
#QQ邮箱:3522689565@qq.com
#Google邮箱:xiaochen200011@gmail.com
hh=tk.Tk()
hh.title("九五便捷操作系统")
hh.config(background="skyblue")
hh.geometry("300x600")
hh.attributes("-alpha",0.8964)
hh.attributes('-topmost','true')
hh.geometry("+1920+0")
lab=Label(hh,text="九五便捷操作系统",width=300,background="pink",font=("黑体",28))
def numaaaa():
    #姓名单位
    listone=["陈浩涵","王华特","冯嘉晨",
             "孙宏杰","赵泽安","吴冬晨",
             "李浩然","梁恩豪",""
             
             
             ]
    albab=random.choice(listone)
    l1=Label(hh,text=albab,relief="sunken",font=("黑体",20))
    l1.pack(anchor="w")
    def clearfucku():
        l1.destroy()
        but.destroy()
    but=Button(hh,text="清除",background="pink",command=clearfucku)

    but.pack()

but=Button(hh,text="点击抽查",command=numaaaa,width=300)
def intel():
    url=requests.get("https://www.baidu.com/")
    url=url.status_code
    errora=Label(hh,text="未显示即是未连接网络",width=300,background="pink",relief="sunken")
    errora.pack()
    if url==200:
        aintel=Label(hh,text="网络已连接",width=300,background="pink",relief="sunken")
        aintel.pack()
    def caaa():
        errora.destroy()

        aintel.destroy()
        buta.destroy()
    buta=Button(hh,text="清除",background="pink",command=caaa)
    buta.pack()

intel=Button(hh,text="查看网络连接",width=300,command=intel)

#封包处
lab.pack()
but.pack()
intel.pack()
time.sleep(0.8964)
mainloop()