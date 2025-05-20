import ttkbootstrap as ttk
from ttkbootstrap import *

lab = (ttk.Entry, ttk.Combobox)
wid = (ttk.Entry, ttk.Combobox, ttk.Button, ttk.Label)
txt = (ttk.Label, ttk.Checkbutton, ttk.Button)
var = (ttk.Entry, ttk.Label, ttk.Combobox)
bar = (ttk.Progressbar,)
val = (ttk.Combobox,)
top = (ttk.Treeview,)


class UICreate:
    # 创建页面对象 ################################################################
    def __init__(self,
                 app_root: tk.Tk,
                 app_view: dict = None,
                 app_text: dict = None):
        self.start = ttk.Notebook(app_root)
        self.views = {}  # 存储APP对象内容
        self.pages_config = app_view or {}
        self.texts_config = app_text or {}
        self.pageCreate()
        print(self.views)

    # 获取本地翻译 ################################################################
    def i18nString(self, in_name):
        if in_name in self.texts_config:
            result = self.texts_config[in_name]
            if type(result) is list:
                return "".join(result)
            return result
        return in_name

    # 设置页面组件 ################################################################
    def pageCreate(self):
        # 处理页面 ================================================================
        print(self.pages_config)
        for page_name in self.pages_config:
            # 添加组件 ------------------------------------------------------------
            self.views[page_name] = {}
            view_list = self.pages_config[page_name]
            api = ttk.Frame(self.start)
            l = c = 0
            # 遍历组件 ============================================================
            for view_name in view_list:
                view_item = view_list[view_name]
                l, c = self.viewCreate(api, view_item, page_name, view_name, l, c)
            # 添加标签 ------------------------------------------------------------
            self.start.add(api, text=self.i18nString(page_name))
        self.start.pack(padx=10, pady=10, fill="both", expand=True)

    # 添加组合组件 ################################################################
    def viewCreate(self, page_apis, view_item, page_name, view_name, line, cols):
        # 新UI组件 ================================================================
        view_data = self.itemCreate(page_apis, view_item, view_name)
        view_type = view_data['entry']
        # 设置列表 ================================================================
        if type(view_type) == type(ttk.Combobox):
            if 'index' in view_item and 'value' in view_item:
                if len(view_item['value']) > view_item['index']:
                    view_type.current(view_item['index'])
            elif 'value' in view_item and len(view_item['value']) > 0:
                view_type.current(0)
        # 设置表格 ================================================================
        if type(view_type) == ttk.Treeview and 'table' in view_item:
            view_type["columns"] = tuple(view_item['table'].keys())
            view_type.column("#0", width=25)
            view_type.heading("#0", text="#", anchor='center')
            for set_name in view_item['table']:
                width = view_item['table'][set_name]
                view_type.column(set_name, width=width, anchor='center')
                view_text = view_name + "_" + set_name
                view_type.heading(set_name, text=self.i18nString(view_text), anchor='center')
        # 放置核心组件 =========================================================================
        if view_data["label"] is not None:
            cols += 1
            view_data["label"].grid(padx=10, row=line, column=cols)
        view_type.grid(pady=10, row=line, column=cols + 1, columnspan=view_item['lines'],
                       padx=10, sticky=NSEW if page_name == "about_us" else W)
        # 放置附属组件 =========================================================================
        for add_name in view_data['addon']:
            now_data = view_data['addon'][add_name]
            now_data.grid(column=cols + 1 + view_item['lines'], row=line, padx=10, pady=10,
                          sticky=W, columnspan=view_item['addon'][add_name]['lines'])
            cols += view_item['addon'][add_name]['lines']
        # 计算行位置 ===========================================================================
        cols += view_item['lines']
        if cols >= 6:
            cols = 0
            line += 1
        self.views[page_name][view_name] = view_data
        return line, cols

    # 添加单个组件 #############################################################################
    def itemCreate(self, page_apis, view_item, view_name):
        view_type = view_item['entry']
        view_subs = view_item['addon']
        var_save = view_item['saves']() if 'saves' in view_item else None
        var_adds = {
            add_name: view_subs[add_name]['saves']() \
                if 'saves' in view_subs[add_name] else None
            for add_name in view_subs
        }
        tmp_data = {
            # 引导标题 =============================================================================
            "label": ttk.Label(
                page_apis, text=self.i18nString(view_name) + ": ") \
                if view_type in lab and ("label" not in view_item or view_item["label"]) else None,
            # 核心组件 =============================================================================
            "saves": var_save,
            "entry": view_item["entry"](
                page_apis, bootstyle=view_item['color'] or "info",
                # command=view_item['start'] if 'start' in view_item and view_type in com else None,
                width=view_item['width'] if 'width' in view_item and view_type in wid else None,
                length=view_item['width'] if 'width' in view_item and view_type in bar else None,
                values=view_item['value'] if 'value' in view_item and view_type in val else None,
                height=view_item['highs'] if 'highs' in view_item and view_type in top else None,
                text=self.i18nString(view_name) if view_type in txt else None,
                textvariable=var_save if view_type in var else None,
                variable=var_save if view_type is ttk.Checkbutton else None,
            ),
            # 附件组件 =============================================================================
            "saved": var_adds,
            "addon": {
                add_name: view_subs[add_name]['entry'](
                    page_apis,
                    bootstyle=view_subs[add_name]['color'] \
                        if view_subs[add_name]['entry'] != tk.Text else None,
                    text=self.i18nString(view_name + "_" + add_name) \
                        if view_subs[add_name]['entry'] != tk.Text else None,
                    width=view_subs[add_name]['width'] if 'width' in view_subs[add_name] else None,
                    textvariable=var_adds[add_name] if add_name in view_subs else None,
                    height=view_item['highs'] \
                        if 'highs' in view_item and view_type == ttk.Treeview else None,
                )
                for add_name in view_subs
            },
            "place": ()
        }
        return tmp_data
