from Modules.ttkpagestart.uiobject import UIObject
from Modules.usbtoolboxui.USBToolApi.Windows import WindowsUSBMap


class USBToolStart:
    def __init__(self, in_view):
        self.apis: WindowsUSBMap = WindowsUSBMap(no_menu=True)
        self.port: dict[str, dict] = {}
        self.view: dict[str, UIObject] = in_view

    def update(self):
        self.apis.get_controllers()
        self.port = self.apis.controllers
        root_nums = -1
        for root_data in self.port:
            root_nums += 1
            root_name = root_data['name']
            if 'location_paths' in root_data['identifiers']:
                root_path = root_data['identifiers']['location_paths'][0]
            else:
                root_path = root_data['identifiers']['instance_id']
            root_vers = str(root_data['class'])
            # root_acpi = root_data['identifiers']['instance_id']
            root_uuid = ""
            if 'pci_id' in root_data['identifiers']:
                root_uuid = ",".join(root_data['identifiers']['pci_id'][:2])
            port_list = root_data['ports']
            # 插入数据 ===============================================
            i = self.view["usb_list"].entry.insert('', 'end', values=(
                root_nums, "O", root_name, root_vers, "N/A", root_path
            ), open=True)
            print(root_name, root_vers, root_uuid, root_path)
            # 处理端口 ===============================================
            for port_data in port_list:
                port_uuid = port_data['index']
                port_vers = port_data['class']  # 接口速率
                port_type = str(port_data['guessed'])  # 接口类型
                port_type = port_type.replace(" ", "")
                port_type = port_type.replace("USB", "")
                port_type = port_type.split("-")[0]
                if "Type" in port_type:
                    port_type = "Type " + port_type.split("Type")[1]
                port_name = port_path = "<N/A>"
                port_flag = False
                if port_data['status'] == 'DeviceConnected':
                    port_flag = True
                    port_name = port_data['devices'][0]['name']
                    port_path = port_data['devices'][0]['instance_id']
                    port_path = port_path.replace("USB\\", "").split("\\")[0]
                self.view["usb_list"].entry.insert(i, 'end', values=(
                    port_uuid, "✔️" if port_flag else "✖️",
                    port_name, port_vers, port_type, port_path
                ), text=port_uuid)
        print(self.apis.controllers)

    def select(self, event, *args):
        tree_uuid = self.view["usb_list"].entry.selection()
        if len(tree_uuid) > 0:
            port_uuid = tree_uuid[0]
            port_data = self.view["usb_list"].entry.item(tree_uuid)
            print(port_data)
            self.view["usb_path"].parser(port_data['values'][5])
            self.view["usb_vers"].parser(port_data['values'][3])
            self.view["usb_type"].parser(port_data['values'][4])
            self.view["usb_data"].parser(port_data['values'][2])
            self.view["usb_uuid"].parser("Port %02d" % port_data['values'][0])
            self.view["usb_exec"].parser(port_data['values'][1] == "✔️")

    def change_port(self):
        pass

    def output_kext(self):
        pass
