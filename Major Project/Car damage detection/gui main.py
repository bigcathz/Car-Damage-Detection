

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo


root=tk.Tk()

root.title("Car Damage Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

# bg = Image.open(r"C:/Users\HP/Downloads/road_pathole (1)/road_pathole/y9.jpg")
# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
# bg_img = ImageTk.PhotoImage(bg)
# bg_lbl = tk.Label(root,image=bg_img)
# bg_lbl.place(x=0,y=93)
# #, relwidth=1, relheight=1)

video_label =tk.Label(root)
video_label.pack()
# read video to display on label
player = tkvideo("vehicle.mp4", video_label,loop = 1, size = (w, h))
player.play()

w = tk.Label(root, text="Car Damage Detection",width=70,background="#800517",foreground="white",height=1,font=("Times new roman",15,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


wlcm=tk.Label(root,text="......Welcome to Car damage Detection System ......",width=100,height=3,background="#800517",foreground="white",font=("Times new roman",19,"bold"))
wlcm.place(x=0,y=520)




d2=tk.Button(root,text="Login",command=Login,width=15,height=1,bd=0,background="#800517",foreground="white",font=("times new roman",15,"bold"))
d2.place(x=1000,y=0)


d3=tk.Button(root,text="Register",command=Register,width=15,height=1,bd=0,background="#800517",foreground="white",font=("times new roman",15,"bold"))
d3.place(x=1200,y=0)



root.mainloop()
