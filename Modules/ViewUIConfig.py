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
                "width": 16,
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
                "width": 18,
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
                "highs": 13,
                "table": {
                    "usb_uuid": 25,
                    "usb_flag": 25,
                    "usb_name": 210,
                    "usb_vers": 70,
                    "usb_type": 80,
                    "usb_path": 185,
                },
                "addon": {},
            },
            # 下方按钮 ================================
            "act_pull": {  # 刷新列表------------------
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "act_used": {  # 智能选择------------------
                "entry": ttk.Button,
                "width": 17,
                "lines": 1,
                "color": "info.outline",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "act_help": {  # 智能选择------------------
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "dark",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "act_full": {  # 全选列表------------------
                "entry": ttk.Button,
                "width": 5,
                "lines": 1,
                "color": "success.outline",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "act_none": {  # 清空列表------------------
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "warning.outline",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "act_exec": {  # 执行定制------------------
                "entry": ttk.Button,
                "width": 4,
                "lines": 1,
                "color": "success",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            # 详细信息 ================================
            "usb_path": {
                "entry": ttk.Label,
                "pause": True,
                "width": 18,
                "lines": 1,
                "color": "default",
                "value": "",
                "addon": {
                },
            },
            "usb_uuid": {
                "entry": ttk.Label,
                "pause": True,
                "width": 8,
                "lines": 1,
                "color": "default",
                "value": "",
                "addon": {
                },
            },
            "usb_vers": {
                "entry": ttk.Label,
                "pause": True,
                "width": 8,
                "lines": 1,
                "color": "default",
                "value": "",
                "addon": {
                },
            },
            "usb_data": {
                "entry": ttk.Label,
                "width": 28,
                "lines": 2,
                "color": "default",
                "value": "",
                "addon": {
                },
            },
            "usb_exec": {
                "entry": ttk.Checkbutton,
                "width": 4,
                "lines": 1,
                "color": "info.Roundtoggle.Toolbutton",
                "saves": ttk.BooleanVar,
                "addon": {
                },
            },
            "usb_type": {
                "entry": ttk.Label,
                "pause": True,
                "width": 8,
                "lines": 1,
                "color": "default",
                "value": "",
                "addon": {
                },
            },
            "efi_save": {
                "entry": ttk.Checkbutton,
                "width": 5,
                "lines": 1,
                "color": "info.Roundtoggle.Toolbutton",
                "saves": ttk.StringVar,
                "addon": {
                },
            },
            "efi_path": {
                "label": False,
                "entry": ttk.Entry,
                "pause": True,
                "width": 28,
                "lines": 2,
                "color": "gray",
                "saves": ttk.StringVar,
                "addon": {
                    "btn": {
                        "entry": ttk.Button,
                        "width": 5,
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
        # GPU定制 ###################################################
        "gpu_menu": {
            "txt_none": {
                "entry": ttk.Label,
                "width": 20,
                "lines": 1,
                "color": "info",
                "addon": {
                },
            },
        },
        # PCI定制 ###################################################
        "pci_menu": {
            "txt_none": {
                "entry": ttk.Label,
                "width": 20,
                "lines": 1,
                "color": "info",
                "addon": {
                },
            },
        },
        # NET定制 ###################################################
        "net_menu": {
            "txt_none": {
                "entry": ttk.Label,
                "width": 20,
                "lines": 1,
                "color": "info",
                "addon": {
                },
            },
        },
        # AUD定制 ###################################################
        "aud_menu": {
            "txt_none": {
                "entry": ttk.Label,
                "width": 20,
                "lines": 1,
                "color": "info",
                "addon": {
                },
            },
        },
        # AUD定制 ###################################################
        "add_menu": {
            "txt_none": {
                "entry": ttk.Label,
                "width": 20,
                "lines": 1,
                "color": "info",
                "addon": {
                },
            },
        },
        # AUD定制 ###################################################
        "inf_memu": {
            "txt_none": {
                "entry": ttk.Label,
                "width": 20,
                "lines": 1,
                "color": "info",
                "addon": {
                },
            },
        }
    }
