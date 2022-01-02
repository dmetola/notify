import schedule
import time as time
import signal
import os
from threading import Thread
from time import sleep
from schedule import every, repeat, run_pending
from notifypy import Notify

def main():
    Thread(target=receive_notification).start()
    while True:
        time.sleep(1)

def send_notification():
    '''Send a notification every hour, reminding me to stretch'''
    notification = Notify()
    notification.title = "Time notification"
    notification.message = "Time to stretch!"
    notification.send()

def receive_notification():
    '''How often a notification is sent, and at what time it should stop'''
    schedule.every().day.at("17:25").do(send_notification)
    schedule.every(10).seconds.do(send_notification)
    while True:
        schedule.run_pending()
        time.sleep(1)
    else:
        schedule.every(1).seconds.until("17:26").do(exit)

def exit():
    os.kill(os.getpid(), signal.SIGTERM)

main()