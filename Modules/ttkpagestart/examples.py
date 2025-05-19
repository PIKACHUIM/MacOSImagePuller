import tkinter
import ttkbootstrap as ttk
from ttkbootstrap import *

from Modules.ttkpagestart.uiconfig import UIConfig
from Modules.ttkpagestart.uicreate import UICreate


class Examples:
    def __init__(self):
        self.root = tk.Tk()
        self.head = ttk.Style()
        self.root.geometry("665x570")
        self.root.title("Example Application")
        # 界面配置 ============================================================
        self.main = ttk.Notebook(self.root)
        # 布置组件 ============================================================
        self.view = UICreate(self.root, UIConfig.page)
        # 完成载入 ============================================================
        self.root.mainloop()

if __name__ == "__main__":
    app = Examples()