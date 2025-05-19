@echo off
REM %1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
REM cd /d "%~dp0"
REM python.exe BuildPackage.py build

powershell.exe "Start-Process python.exe 'BuildPackage.py build' -verb runAs "