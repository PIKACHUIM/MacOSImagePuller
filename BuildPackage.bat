@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
cd /d "%~dp0"
G:\Venvs\MacRecGet\Scripts\python.exe BuildPackage.py build
xcopy DownloadList.json build/exe.win-amd64-3.11/