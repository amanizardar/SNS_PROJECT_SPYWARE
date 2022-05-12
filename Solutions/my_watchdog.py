import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')

dir_name = r"C:\Users"
handling_event_manager = LoggingEventHandler()

observer = Observer()
observer.schedule(handling_event_manager, dir_name, recursive=True)

observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()