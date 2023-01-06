import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk

from PIL import Image, ImageTk
import cv2

class Surface(ttk.Frame):
    pic_path = ""
    viewhigh = 1000
    viewwide = 2000
    update_time = 0
    thread = None
    thread_run = False
    camera = None
    color_transform = {"green": ("绿牌", "#55FF55"), "yello": ("黄牌", "#FFFF00"), "blue": ("蓝牌", "#6666FF")}

    def __init__(self, win):
        ttk.Frame.__init__(self, win)
        frame_left = ttk.Frame(self)
        frame_right1 = ttk.Frame(self)
        frame_right2 = ttk.Frame(self)
        win.title("车牌识别")
        win.state("zoomed")
        self.pack(fill=tk.BOTH, expand=tk.YES, padx="5", pady="5")
        frame_left.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)
        frame_right1.pack(side=tk.TOP, expand=1, fill=tk.Y)
        frame_right2.pack(side=tk.RIGHT, expand=0)
        ttk.Label(frame_left, text='原图：').pack(anchor="nw")
        ttk.Label(frame_right1, text='车牌位置：').grid(column=0, row=0, sticky=tk.W)

        from_pic_ctl = ttk.Button(frame_right2, text="来自图片", width=20, command=self.from_pic)
        self.image_ctl = ttk.Label(frame_left)
        self.image_ctl.pack(anchor="nw")

        self.roi_ctl = ttk.Label(frame_right1)
        self.roi_ctl.grid(column=0, row=1, sticky=tk.W)
        ttk.Label(frame_right1, text='识别结果：').grid(column=0, row=2, sticky=tk.W)
        self.r_ctl = ttk.Label(frame_right1, text="")
        self.r_ctl.grid(column=0, row=3, sticky=tk.W)
        self.color_ctl = ttk.Label(frame_right1, text="", width="20")
        self.color_ctl.grid(column=0, row=4, sticky=tk.W)


def get_imgtk(self, img_bgr):
    img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    im = Image.fromarray(img)
    imgtk = ImageTk.PhotoImage(image=im)
    wide = imgtk.width()
    high = imgtk.height()
    if wide > self.viewwide or high > self.viewhigh:
        wide_factor = self.viewwide / wide
        high_factor = self.viewhigh / high
        factor = min(wide_factor, high_factor)

        wide = int(wide * factor)
        if wide <= 0: wide = 1
        high = int(high * factor)
        if high <= 0: high = 1
        im = im.resize((wide, high), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=im)
    return imgtk

if __name__ == '__main__':
    win = tk.Tk()

    surface = Surface(win)
    win.mainloop()