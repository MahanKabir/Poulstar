from threading import Thread
import time
def timer01(t):
    counter = 0
    while counter <= 10:
        time.sleep(1)
        print("timer 1:", counter)
        counter +=1
def timer02(t):
    counter = 0
    while counter <= 10:
        time.sleep(1)
        print("timer 2:", counter)
        counter += 1
Thread(target= timer01, args=(0, )).start()
Thread(target= timer02, args=(0, )).start()