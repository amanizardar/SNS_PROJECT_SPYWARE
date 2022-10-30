import PyInstaller.__main__
import shutil
import os


filename="windowsproc.pyw"
exename="nice3.exe"
# icon="Firefox.ico"
pwd=os.getcwd()
usbdir= os.path.join(pwd, "USB")


if os.path.isfile(exename):
    os.remove(exename)
    
    
PyInstaller.__main__.run([
    "windowsproc.pyw",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename
])

shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

