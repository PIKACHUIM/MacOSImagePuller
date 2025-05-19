import ttkbootstrap as ttk


class UIConfig:  # ============================
    page = {  # 每个页面元素详细排列内容和方式
        # 示例 *******************************
        "now_menu": {
            "sys_name": {  #
                "entry": ttk.Combobox,
                "start": None,
                "width": 17,
                "lines": 4,
                "color": "info",
                "saves": ttk.StringVar,
                "addon": {
                }
            },
        },
        "inf_memu": {}
    }   # ====================================
    exec = {  # 所有页面都可以使用的共享的函数
        # 示例 *******************************
        "get_sums": lambda: (
            print(1), print(1)
        ),
    }
