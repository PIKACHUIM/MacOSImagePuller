import os
import json
import webbrowser
import locale
import tkinter
from functools import partial

import pyglet
import ttkbootstrap as ttk
from ttkbootstrap import *

from Modules.PullRecovery import PullRecovery
from Modules.ViewUIConfig import UIConfig, Function
from Modules.LogOutputAPI import Log
from Modules.ttkpagestart.uicreate import UICreate


class HackintoshUI:
    def __init__(self):
        # 创建窗口 ------------------------------------------------------------
        self.area = None
        self.text = None
        self.view = None
        self.readConfig()
        self.root = tk.Tk()
        self.head = ttk.Style()
        self.root.geometry("665x570")
        self.root.title(self.i18nString("app_name"))
        self.root.iconbitmap("Configs/OpencoreImage.ico")
        # 字体设置 ------------------------------------------------------------
        self.font = tkinter.font.Font(family="MapleMono SC NF", size=12)
        self.head.configure("TNotebook.Tab", font=self.font)
        self.head.configure("TFrame", font=self.font)
        self.head.configure("TLabel", font=self.font)
        # 界面配置 ============================================================
        self.main = ttk.Notebook(self.root)
        self.logs = Log("GPULoader", "").log
        # 布置组件 ============================================================
        self.config_exe()
        self.config_txt()
        # 读取数据 ============================================================
        self.view = UICreate(self.root, UIConfig.page, self.text)
        self.dmg_pull = PullRecovery(self.view)
        # 完成载入 ============================================================
        self.viewSetup()
        self.root.mainloop()

    # 读取配置文件 ################################################################
    def readConfig(self):
        self.area = locale.getdefaultlocale()[0]
        pyglet.font.add_file("Configs/MapleMonoFont.ttf")
        read_path = "Configs/Localizations/"
        read_name = read_path + "%s.json" % self.area
        if not os.path.exists(read_name):
            read_name = read_path + "en_US.json"
        with open(read_name, encoding="utf8") as read_file:
            self.text = json.loads(read_file.read())

    def viewSetup(self):
        self.dmg_pull.readJson()
        self.view.views['dmg_menu']['sys_list'].parser(self.dmg_pull.data)
        self.view.views['dmg_menu']['sys_list'].binder(
            self.dmg_pull.onSelect, self.view.views['dmg_menu'])
        self.view.views['dmg_menu']['dmg_path'].addon['efi'].entry.config(command=self.dmg_pull.mountEFI)
        self.view.views['dmg_menu']['bar_deal'].addon['exe'].entry.config(command=self.dmg_pull.download)
        self.view.views['dmg_menu']['dmg_path'].addon['btn'].entry.config(command=partial(
            Function.selectPath,self.view.views['dmg_menu']['dmg_path'].entry))
        self.dmg_pull.parseEFI()
        # 获取本地翻译 ################################################################

    def i18nString(self, in_name):
        if in_name in self.text:
            result = self.text[in_name]
            if type(result) is list:
                return "".join(result)
            return result
        return in_name

    @staticmethod
    def url_github(url=""):
        webbrowser.open(url)

    # 设置按钮绑定 ################################################################
    def config_exe(self):
        pass

    # 设置输入绑定 ################################################################
    def config_txt(self):
        pass


if __name__ == "__main__":
    app = HackintoshUI()
