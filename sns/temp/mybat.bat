@REM @for %%i in (python.exe) do @set py=%%~$PATH:i
@REM @echo %py%

@REM @for %%i in ( %py%) do @set py=%%~dpi
@REM @echo py's directory is %py%

@REM Start-Process “nice3.exe”

@REM powershell -Command ("Invoke-Expression -Command "nice3.exe"")

start /d "nice3.exe"
