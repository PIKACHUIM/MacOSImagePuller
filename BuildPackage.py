import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = []

# TARGET
target = Executable(
    script="PullRecovery.py",
    # base="Win32GUI",
    icon="PullRecovery.ico"
)

# SETUP CX FREEZE
setup(
    name="Mac OS Recovery Downloader",
    version="0.1",
    description="Mac OS Recovery Downloader",
    author="Pikachu Ren",
    options={'build_exe': {'include_files': files}},
    executables=[target],
)
