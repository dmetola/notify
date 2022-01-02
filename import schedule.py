import schedule
from threading import Thread
import time
import os
import signal


def exit_data():
    print("Exiting")

    # sys.exit()
    os.kill(os.getpid(), signal.SIGTERM)

def exit_data_thread():
    schedule.every(3).seconds.do(exit_data)
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    Thread(target=exit_data_thread).start()

    while True:
        time.sleep(1)

main()