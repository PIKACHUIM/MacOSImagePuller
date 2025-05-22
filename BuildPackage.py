import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
add_files = [
    ("DownloadLists.json", ""),
    ("OpencoreImage.ico", ""),
    ("Etchers", "Etchers/"),
    ("Scripts", "Scripts/"),
    ("Scripts", "./lib/Scripts/"),
]

# TARGET
target = Executable(
    script="HackintoshUI.py",
    # base="Win32GUI",
    icon="Configs/OpencoreImage.ico",
    uac_admin=True
)

# SETUP CX FREEZE
setup(
    name="Hackintosh Toolbox",
    version="0.1.2025.0520",
    description="Hackintosh Toolbox for Windows",
    author="Pikachu Ren",
    options={
        'build_exe': {
            'include_files': add_files,
            "packages": [
                "ttkbootstrap.utility",
                "ttkbootstrap",
            ],
        },
    },
    executables=[target],
)
