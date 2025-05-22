import json
import os
import shutil
import subprocess
import threading
import time

from ttkbootstrap import *
from tkinter import messagebox
import psutil

from Modules.downloadfile import PullGibMacOS
from Modules.downloadfile.MacsRecovery import action_download
from Modules.downloadfile.PullGibMacOS import gibMacOS


class ArgRecDown:
    def __init__(self,
                 action='download', outdir='com.apple.recovery.boot',
                 basename='', board_id='Mac-7BA5B2D9E42DDD94', mlb='00000000000000000',
                 code='', os_type='latest', diagnostics=False, verbose=False,
                 board_db='boards.json'
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


class PullRecovery:
    def __init__(self, in_view):

        self.flag = False
        self.main = in_view
        self.data = []
        self.part = []
        self.exec = {
            "process": 0,
            "extcute": True,
        }
        self.proc = None  # 存储下载过程的线程
        self.demo = None  # 存储更新进度的线程
        self.name = None  # 存储待下载系统版本
        self.path = None  # 存储待下载保存路径
        self.page = self.main.views['dmg_menu']

    def readJson(self):
        with open("Configs/DownloadLists.json", "r") as read_file:
            read_data = json.load(read_file)
            print()
            self.data = [(i, "✔️" if read_data[i][2] else "✖️",
                          read_data[i][0], read_data[i][1]) for i in read_data]
            self.data.reverse()
        print(self.data)

    def parseEFI(self, number=0):
        self.part = psutil.disk_partitions()
        self.part = [i.device for i in self.part]
        values = ["不写入ESP"] + self.part
        self.page['dmg_save'].entry.configure(values=values)
        self.page['dmg_save'].entry.current(0 if number == 0 else len(self.part))

    @staticmethod
    def onSelect(view_list, event):
        tree_item = view_list[0]['sys_list']
        tree_uuid = tree_item.entry.selection()
        if len(tree_uuid) > 0:
            tree_uuid = tree_uuid[0]
            tree_data = tree_item.entry.item(tree_uuid)
            tree_data = tree_data['values']
            print(tree_data)
            view_list[0]['sys_name'].parser(tree_data[0])
            view_list[0]['sys_info'].parser(tree_data[2])
            view_list[0]['sys_uuid'].parser("{:<017}".format(tree_data[3]))
            view_list[0]['bar_deal'].addon['exe'].freeze(False)

    def mountEFI(self):
        for i in ["O", "P", "Q", "R"]:
            process = subprocess.run(
                "cmd /c mountvol %s: /S" % i,
                shell=True, text=True, capture_output=True)
            results = process.stdout
            if len(results) > 1:
                continue
            tk.messagebox.showinfo("成功", "挂载EFI分区成功！")
            self.parseEFI(-1)
            return i
        messagebox.showerror("错误", "挂载EFI分区失败:\n" + results)
        return False

    def dmgFetch(self, save_path, vers_name):
        g = gibMacOS(interactive=True, download_dir=save_path)
        g.set_prods(progressbar=self.page['bar_deal'].entry)
        try:
            g.get_for_version(vers_name, dmg=True, progressbar=self.page['bar_deal'].entry)
        except (PullGibMacOS.ProgramError, Exception) as err:
            g.get_for_version(vers_name, dmg=False, progressbar=self.page['bar_deal'].entry)
        self.page['bar_deal'].addon['exe'].entry.config(state=tk.NORMAL)
        self.flag = False
        messagebox.showinfo("恭喜", "下载镜像文件成功")

    def download(self, *args):
        self.path = self.page['dmg_path'].entry.get()
        self.name = self.page['sys_name'].entry.get()
        if len(self.path) <= 0:
            messagebox.showerror("错误", "请设置保存路径")
            return False
        self.page['bar_deal'].addon['exe'].entry.config(state=tk.DISABLED)
        if self.page['sys_type'].entry.get() == "在线恢复镜像DMG":
            pid = self.page['sys_info'].entry.get()
            uid = self.page['sys_uuid'].entry.get()
            self.exec['execute'] = True
            if len(pid) <= 0 or len(uid) <= 0:
                messagebox.showerror("错误", "缺少ID，请选择系统或者手动填写")
                return False
            self.page["bar_deal"].entry['value'] = 0
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
                board_db=save_path + self.name + '/boards.json'
            )
            self.proc = threading.Thread(target=action_download, args=(args, self.exec,))
            self.proc.start()
            self.demo = threading.Thread(target=self.updateUI, args=())
            self.demo.start()
            return None
        elif self.page['sys_type'].entry.get() == "离线恢复固件DMG":
            save_path = self.path + self.name + "/"
            if self.name.find("-") > 0:
                vers_name = self.name[6:]
            else:
                vers_name = "sequoia"

            if os.path.exists(save_path):
                shutil.rmtree(save_path)
            self.proc = threading.Thread(target=self.dmgFetch, args=(save_path, vers_name,))
            self.proc.start()
            return None
        else:
            self.page['bar_deal'].addon['exe'].entry.config(state=tk.NORMAL)
            return None

    def finished(self, save_path, vers_name):
        g = gibMacOS(interactive=True, download_dir=save_path)
        g.set_prods(progressbar=self.page['bar_deal'].entry)
        try:
            g.get_for_version(vers_name, dmg=True, progressbar=self.page['bar_deal'].entry)
        except (PullGibMacOS.ProgramError, Exception) as err:
            g.get_for_version(vers_name, dmg=False, progressbar=self.page['bar_deal'].entry)
        self.page['bar_deal'].addon['exe'].entry.config(state=tk.NORMAL)
        self.flag = False
        messagebox.showinfo("恭喜", "下载镜像文件成功")

    def updateUI(self):
        try:
            while self.proc is not None and self.proc.is_alive() and self.exec['execute']:
                self.page['bar_deal'].entry["value"] = self.exec['process']
                time.sleep(0.2)
            if self.exec['execute']:
                self.proc = self.demo = None
                save_file = "/.contentDetails"
                save_path = self.path + self.name + "/com.apple.recovery.boot"
                save_file = save_path + save_file
                with open(save_file, "w") as save_data:
                    save_data.write("Install macOS " + self.name)
                if self.page['dmg_save'].entry.get() != "不写入ESP":
                    part_label = self.page['dmg_save'].entry.get()
                    if os.path.exists(part_label):
                        try:
                            part_path = part_label + "com.apple.recovery.boot"
                            if os.path.exists(part_path):
                                shutil.rmtree(part_path)
                            shutil.copytree(save_path, part_path)
                            os.system("explorer %s" % part_path.replace("/", "\\"))
                        except (PermissionError, Exception) as err:
                            messagebox.showwarning("错误", str(err))
                            return False
                    else:
                        messagebox.showwarning("错误", "所选磁盘不存在")
                else:
                    os.system("explorer %s" % self.path.replace("/", "\\"))
                messagebox.showinfo("恭喜", "下载镜像文件成功")
        except (SystemExit, Exception) as e:
            print("Force to stop at:", str(e))
        self.page['bar_deal'].addon['exe'].entry.config(state=tk.NORMAL)
        return True
