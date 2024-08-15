import json
import os
import signal
import threading
import time
import tkinter as tk
# import tkinter as tt
import ttkbootstrap as tt
from tkinter import filedialog, messagebox
from ttkbootstrap.constants import *
from MacsRecovery import action_download


class ArgRecDown:
    def __init__(self,
                 action='download', outdir='com.apple.recovery.boot',
                 basename='', board_id='Mac-7BA5B2D9E42DDD94', mlb='00000000000000000',
                 code='', os_type='latest', diagnostics=False, verbose=False,
                 board_db='G:\\Codes\\PullRecovery\\boards.json'
                 ):
        self.action = action
        self.outdir = outdir
        self.basename = basename
        self.board_id = board_id
        self.os_type = os_type
        self.diagnostics = diagnostics
        self.verbose = verbose
        self.board_db = board_db
        self.verbose = verbose
        self.mlb = mlb
        self.code = code


class MacRecDown:
    def __init__(self):
        self.demo = None
        self.proc = None
        self.path = ""
        self.name = ""
        self.data = dict()
        self.root = tk.Tk()
        self.exec = {
            "process": 0,
            "extcute": True,
        }
        self.conf = tk.ttk.Style()
        self.conf.theme_use("default")
        self.conf.configure("TProgressbar", thickness=50)
        # 设置主窗口宽度和高度
        self.root.geometry("650x150")
        self.root.title("Mac OS 恢复镜像下载工具 (v0.1 Beta ©2024 Pikachu)")
        self.root.protocol("WM_DELETE_WINDOW", self.onClosing)
        self.tk_l_sys = tt.Label(text="选择系统：")
        self.tk_l_sys.grid(row=0, column=0, padx=10, sticky=W, pady=10)
        self.tk_c_sys = tt.Combobox(bootstyle="info", width=15)
        self.tk_c_sys.bind("<<ComboboxSelected>>", self.save_type)
        self.tk_c_sys.grid(row=0, column=1, sticky=W, pady=10)
        self.tk_l_pid = tt.Label(text="序列号：")
        self.tk_l_pid.grid(row=0, column=2, sticky=W, pady=10)
        self.tk_e_pid = tt.Entry(bootstyle="info", width=22)
        self.tk_e_pid.grid(row=0, column=3, sticky=W, pady=10)
        self.tk_l_uid = tt.Label(text="版本号：")
        self.tk_l_uid.grid(row=0, column=4, sticky=W, pady=10)
        self.tk_e_uid = tt.Entry(bootstyle="info", width=15)
        self.tk_e_uid.grid(row=0, column=5, sticky=W, pady=10)
        self.tk_l_url = tt.Label(text="保存路径：")
        self.tk_l_url.grid(row=2, column=0, padx=10, pady=10)
        self.tk_e_url = tt.Entry(bootstyle="info", width=60)
        self.tk_e_url.grid(row=2, column=1, pady=10, columnspan=4)
        self.tk_b_url = tt.Button(bootstyle="info", width=10, text="打开",
                                  command=self.open_path)
        self.tk_b_url.grid(row=2, column=5, pady=10, padx=22)
        self.tk_b_act = tt.Button(bootstyle="success", width=5, text="开始",
                                  command=self.downloads)
        self.tk_b_act.grid(row=3, column=0, padx=10, pady=10)
        self.tk_p_act = tt.Progressbar(bootstyle="success-striped", length=435,
                                       style="TProgressbar", mode='determinate')
        self.tk_p_act.grid(row=3, column=1, pady=10, columnspan=5, sticky=W)
        self.tk_l_act = tt.Label(text="0%")
        self.tk_l_act.grid(row=3, column=5, padx=10, pady=10)
        self.tk_p_act['value'] = 0
        self.read_json()
        self.root.mainloop()

    def open_path(self):
        self.path = filedialog.askdirectory().replace("\\", "/")
        self.path += "MacRecovery/"
        self.tk_e_url.delete(0, tk.END)
        self.tk_e_url.insert(0, self.path)
        self.tk_p_act['value'] = 0
        self.tk_l_act['text'] = "0%"
        print("Selected directory:", self.path)

    def save_type(self, event):
        self.name = event.widget.get()
        if self.name in self.data:
            self.tk_e_pid.delete(0, tk.END)
            self.tk_e_uid.delete(0, tk.END)
            self.tk_e_pid.insert(0, self.data[self.name][0])
            self.tk_e_uid.insert(0, self.data[self.name][1])
            self.tk_p_act['value'] = 0
            self.tk_l_act['text'] = "0%"
        print("Selected value:", self.name)

    def read_json(self):
        with open("DownloadList.json", "r") as read_file:
            read_data = json.load(read_file)
            read_name = [i for i in read_data]
            self.tk_c_sys["values"] = read_name
            self.tk_c_sys.current(len(read_name) - 1)
            self.data = read_data

    def updateFPS(self):
        try:
            while self.proc is not None and self.proc.is_alive() \
                    and self.exec['execute']:
                self.tk_p_act["value"] = self.exec['process']
                self.tk_l_act['text'] = "%d%%" % int(self.exec['process'])
                time.sleep(0.2)
            if self.exec['execute']:
                os.system("explorer %s" % self.path.replace("/", "\\"))
                self.proc = self.demo = None
                messagebox.showinfo("恭喜", "下载镜像文件成功")
        except (SystemExit, Exception) as e:
            print("Force to stop at:", str(e))
        self.tk_b_act.config(state=tt.NORMAL)

    def waitProcs(self, proc):
        if self.exec['execute']:
            self.exec['execute'] = False
        count = 3
        try:
            raise SystemExit()
            time.sleep(1)
        except (SystemExit, Exception) as e:
            while count > 0 and proc.is_alive():
                time.sleep(1)
                print("Wait program exit...")
                count -= 1

    def onClosing(self, cw=True):
        if cw:
            # 获取当前进程ID
            pid = os.getpid()
            print("Current process ID is:", pid)
            # 发送SIGTERM信号结束进程
            os.kill(pid, signal.SIGTERM)
        if self.proc is not None and self.proc.is_alive():
            self.waitProcs(self.proc)
        if self.demo is not None and self.demo.is_alive():
            self.waitProcs(self.demo)
        self.tk_b_act.config(state=tt.NORMAL)
        if cw:
            exit(0)

    def downloads(self):
        pid = self.tk_e_pid.get()
        uid = self.tk_e_uid.get()
        self.exec['execute'] = True
        self.tk_b_act.config(state=tt.DISABLED)
        self.onClosing(cw=False)
        if len(pid) <= 0 or len(uid) <= 0:
            messagebox.showerror("错误", "缺少ID，请选择系统或者手动填写")
            return False
        if len(self.path) <= 0:
            messagebox.showerror("错误", "请设置保存路径")
            return False
        self.tk_p_act['value'] = 0
        self.tk_l_act['text'] = "0%"
        save_path = self.path + self.name + '/com.apple.recovery.boot'
        print("Saving path:", save_path)
        args = ArgRecDown(
            action='download',
            outdir=save_path,
            basename='',
            board_id=pid,
            mlb=uid,
            code='',
            os_type='',
            diagnostics=False,
            verbose=False,
            board_db=self.path + self.name + '/boards.json'
        )
        self.proc = threading.Thread(target=action_download, args=(args, self.exec,))
        self.proc.start()
        self.demo = threading.Thread(target=self.updateFPS, args=())
        self.demo.start()


if __name__ == '__main__':
    exe = MacRecDown()
