import tkinter
from functools import partial
from ttkbootstrap import *
from tkinter import ttk

lab = (ttk.Entry, ttk.Combobox, ttk.Label)
wid = (ttk.Entry, ttk.Combobox, ttk.Button, ttk.Label)
txt = (ttk.Label, ttk.Checkbutton, ttk.Button)
var = (ttk.Entry, ttk.Label, ttk.Combobox)
bar = (ttk.Progressbar,)
val = (ttk.Combobox,)
top = (ttk.Treeview,)
com = (ttk.Button,)


class UIObject:
    def __init__(self,  # 组件创建 ========================
                 in_name,
                 in_item,
                 in_apis,
                 in_i18n: callable,
                 ):
        self.label = None
        self.entry = None
        self.saves = None
        self.addon = {}
        self.items = in_item
        self.names = in_name
        self.trans = in_i18n
        self.roots = in_apis
        self.create()

    def create(self):
        view_type = self.items['entry']
        self.saves = self.items['saves']() if 'saves' in self.items else None
        self.label = ttk.Label(
            self.roots, text=self.trans(self.names) + ": ") \
            if view_type in lab and ("label" not in self.items or self.items["label"]) else None
        self.entry = self.items["entry"](
            self.roots, bootstyle=self.items['color'] or "info",
            command=self.items['start'] if 'start' in self.items and view_type in com else None,
            width=self.items['width'] if 'width' in self.items and view_type in wid else None,
            length=self.items['width'] if 'width' in self.items and view_type in bar else None,
            values=self.items['value'] if 'value' in self.items and view_type in val else None,
            height=self.items['highs'] if 'highs' in self.items and view_type in top else None,
            text=self.trans(self.names) if view_type in txt else None,
            textvariable=self.saves if view_type in var else None,
            variable=self.saves if view_type is ttk.Checkbutton else None,
        )
        if "value" in self.items and self.items["entry"] == ttk.Entry:
            # if self.items["saves"] is not None:
            #     self.saves.set(self.items["value"])
            self.parser(self.items['value'])
        if "addon" in self.items and type(self.items["addon"]) is dict:
            self.addon = {
                adds_name: UIObject(
                    self.names + "_" + adds_name,
                    self.items["addon"][adds_name],
                    self.roots,
                    self.trans,
                ) for adds_name in self.items["addon"]
            }
        if "pause" in self.items and self.items["pause"]:
            self.entry.config(state="disabled")
        self.config()
        return self

    def freeze(self, in_flag):
        self.entry.config(state=tk.DISABLED \
            if in_flag else tk.NORMAL)

    # 放置组件 ============================================
    def placed(self):
        pass

    # 取消放置 ============================================
    def forget(self):
        pass

    def config(self):
        # 创建列表 ========================================
        if type(self.entry) == ttk.Combobox:
            if 'value' in self.items:
                self.entry.current(0)
                if 'index' in self.items:
                    if len(self.items['value']) > self.items['index']:
                        self.entry.current(self.items['index'])
        # 创建表格 ========================================
        if type(self.entry) == ttk.Treeview:
            self.entry.column("#0", width=25)
            self.entry.heading("#0", text="#", anchor='center')

    # 设置内容 ============================================
    def parser(self, in_data: list | str | bool):
        # 设置表格 ========================================
        if type(self.entry) == ttk.Treeview:
            count = 0
            for row in in_data:
                self.entry.insert('', count, values=row)
                count += 1
        # 设置文本 ========================================
        if type(self.entry) in (
                ttk.Entry, ttk.Button, ttk.Checkbutton,
                ttk.Button, ttk.Label):
            if self.saves is not None:
                self.saves.set(in_data)
            else:
                self.entry['text'] = in_data

    # 清空内容 ============================================
    def eraser(self):
        # 检查类型 ========================================
        if type(self.entry) != ttk.Treeview:
            return False
        # 设置表格 ========================================
        self.entry.delete(*self.entry.get_children())
        return True

    def binder(self, runner: callable, *in_args):
        # 绑定表格 ========================================
        if type(self.entry) == ttk.Treeview:
            self.entry.bind('<<TreeviewSelect>>', partial(
                runner, in_args))
