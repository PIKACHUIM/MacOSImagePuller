import tkinter
import tkinter.filedialog
import ttkbootstrap as ttk
from Modules.LogOutput import Log, LL


class Function:
    @staticmethod
    def selectFile(in_apis, in_type):
        file_path = tkinter.filedialog.askopenfilename(filetypes=in_type)

        in_apis.delete(0, tkinter.END)
        in_apis.insert(0, file_path)
        return file_path

    @staticmethod
    def selectPath(in_apis):
        file_path = tkinter.filedialog.askdirectory()
        in_apis.delete(0, tkinter.END)
        in_apis.insert(0, file_path)
        return file_path

    @staticmethod
    def splitLists(in_data, in_logs, in_name, prompts="splitLists"):
        outputs = in_data.split("\n")
        results = []
        for gpu_name in outputs:
            if len(gpu_name) > 0:
                in_logs("返回%s列表: %s" %
                        (in_name, gpu_name), prompts, LL.S_)
                results.append(gpu_name)
        return results


class UIConfig:
    line = 6  # 每个页面内允许放置的单元列数量
    page = {  # 每个页面元素详细排列内容和方式
        # 示例 *******************************
        "dmg_menu": {
            "sys_name": {
                "entry": ttk.Combobox,
                "start": None,
                "width": 17,
                "lines": 4,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                }
            },
            "sys_type": {
                "entry": ttk.Combobox,
                "start": None,
                "width": 17,
                "lines": 4,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "sys_info": {
                "entry": ttk.Entry,
                "start": None,
                "width": 18,
                "lines": 4,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "sys_uuid": {
                "entry": ttk.Entry,
                "start": None,
                "width": 18,
                "lines": 4,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "dmg_path": {
                "entry": ttk.Entry,
                "start": None,
                "width": 30,
                "lines": 5,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                    "btn_open": {
                        "entry": ttk.Button,
                        "start": None,
                        "width": 6,
                        "lines": 1,
                        "color": "info",
                    },
                    "efi_open": {
                        "entry": ttk.Button,
                        "start": None,
                        "width": 6,
                        "lines": 1,
                        "color": "warning",
                    }
                },

            },
            "bar_deal": {
                "entry": ttk.Progressbar,
                "start": None,
                "width": 300,
                "lines": 5,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                    "btn_open": {
                        "entry": ttk.Button,
                        "start": None,
                        "width": 6,
                        "lines": 1,
                        "color": "info",
                    },
                    "efi_path": {
                        "entry": ttk.Entry,
                        "start": None,
                        "width": 8,
                        "lines": 4,
                        "color": "info",
                        "saves": ttk.StringVar,
                        "addon": {
                        },
                    },
                },

            },
        },
        "usb_menu": {},
        "gpu_menu": {},
        "pci_menu": {},
        "net_menu": {},
        "add_menu": {},
        "inf_memu": {}
    }
