# SNS_PROJECT_SPYWARE
Keylogger,AudioLogger and Screenshotlogger
This is a System and network security project.
Implemented a Spyware which is capable of performing the following functions :

#### Keylogger 
One of the functionality of that spyware is keylogging. It records the key-presses of the victim and sends them over the email to the attacker.

#### AudioLogger
Another funtionality of that spyware is that it can act as an Audiologger. According to the predefined time interval by the attacker, it records the audio via the microphone of the victim's device and then send it over the email to the attacker.

#### Screenshotlogger
This spyware is also capable of capturing the screenshots of the victim's device and sending them to the attacker.  

> For Automation we have used bash scripting.  
> This attack is targeted only for windows operating system.  

To perform the attack, the attacker should send `Myscript.bat` file to the victim's device via any medium (Email, Chats, Spoofing etc) or bind it with any other software/game file so that victim would open that file.  
After victim opens the spoofed file (Myscript.bat file or script file binded with the software/game file) this script will start executing in the backgroud without victim being aware of it.  

Script will perform the following instructions inside the victim's device : 
- First of all it will download five files from the cloud named :
  1. autorun.py
  2. buildexe.py
  3. windowsproc.pyw
  4. Screenshot1.pyw
  5. audio_rec_final.pyw  
  
  > Autorun.py is the heart of the spyware and responsible of executing various commands over the victim's device.  
  > buildexe.py is responsible for creation of the executable file of the three functionalities of the spyware.  
  > windowsproc.pyw is the keylogger, Screenshot1.pyw is screenlogger and audio_rec_final.pyw is audiologger programs.  
 
- After that it will execute autorun.py  
- autorun.py will call buildexe.py that will take windowsproc.pyw, Screenshot1.pyw and audio_rec_final.pyw and build executable files of these files named nice1.exe, nice2.exe and nice3.exe  
- Along with it autorun.py add these three executable files to the windows registry so that even if victim restarts the device these executable will be automatically started at the windows bootup.  

> Now this spyware will send the victim's information to the attacker's email periodically.  

    
    

