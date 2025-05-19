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
    script="PullRecovery.py",
    # base="Win32GUI",
    icon="OpencoreImage.ico",
    uac_admin=True
)

# SETUP CX FREEZE
setup(
    name="Mac OS Recovery Downloader",
    version="0.2.2024.1106",
    description="Mac OS Recovery Downloader",
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
