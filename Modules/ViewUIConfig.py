import tkinter
import tkinter.filedialog

import ttkbootstrap as ttk
from Modules.LogOutputAPI import Log, LL


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
            "sys_list": {
                "entry": ttk.Treeview,
                "lines": 6,
                "color": "info",
                "highs": 13,
                "table": {
                    "sys_type": 180,
                    "sys_full": 50,
                    "sys_info": 190,
                    "sys_uuid": 170,
                },
                "addon": {},
            },
            "sys_name": {
                "entry": ttk.Entry,
                "pause": True,
                "width": 20,
                "lines": 2,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                }
            },
            "sys_type": {
                "entry": ttk.Combobox,
                "width": 15,
                "lines": 2,
                "value": ["在线恢复镜像DMG", "离线恢复固件DMG"],
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "sys_info": {
                "entry": ttk.Entry,
                "pause": True,
                "width": 20,
                "lines": 2,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "sys_uuid": {
                "entry": ttk.Entry,
                "pause": True,
                "width": 17,
                "lines": 2,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "dmg_path": {
                "entry": ttk.Entry,
                "width": 30,
                "lines": 3,
                "color": "info",
                "saves": ttk.StringVar,
                "value": "./MacRecovery/",
                "addon": {
                    "btn": {
                        "entry": ttk.Button,
                        "width": 6,
                        "lines": 1,
                        "color": "info",
                        "start": None,
                    },
                    "efi": {
                        "entry": ttk.Button,
                        "width": 6,
                        "lines": 1,
                        "start": None,
                        "color": "warning.outline",
                    }
                },

            },
            "dmg_save": {
                "entry": ttk.Combobox,
                "width": 10,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "bar_deal": {
                "entry": ttk.Progressbar,
                "width": 250,
                "lines": 3,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                    "exe": {
                        "entry": ttk.Button,
                        "start": None,
                        "pause": True,
                        "width": 6,
                        "lines": 1,
                        "color": "success",
                    },
                },

            },
        },
        "usb_menu": {
            "usb_list": {
                "entry": ttk.Treeview,
                "lines": 6,
                "color": "info",
                "highs": 15,
                "table": {
                    "usb_root": 200,
                    "usb_port": 50,
                    "usb_vers": 50,
                    "usb_type": 50,
                    "usb_data": 240,
                },
                "addon": {},
            },
            "usb_root": {
                "entry": ttk.Entry,
                "width": 20,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "usb_port": {
                "entry": ttk.Entry,
                "width": 5,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "usb_vers": {
                "entry": ttk.Entry,
                "width": 5,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "usb_data": {
                "entry": ttk.Entry,
                "width": 30,
                "lines": 2,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "usb_exec": {
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "success.outline",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "usb_type": {
                "entry": ttk.Entry,
                "width": 5,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "efi_save": {
                "entry": ttk.Checkbutton,
                "width": 5,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "efi_path": {
                "label": False,
                "entry": ttk.Entry,
                "width": 20,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                    "btn": {
                        "entry": ttk.Button,
                        "width": 4,
                        "lines": 1,
                        "color": "info",
                    },
                    "efi": {
                        "entry": ttk.Button,
                        "width": 4,
                        "lines": 1,

                        "color": "secondary.outline",
                    }
                },
            },
            "usb_pull": {
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "primary.outline",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "usb_save": {
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "success",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
        },
        "gpu_menu": {},
        "pci_menu": {},
        "net_menu": {},
        "aud_menu": {},
        "add_menu": {},
        "inf_memu": {}
    }
