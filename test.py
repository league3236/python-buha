import threading
import time

def f():
    while 1:
        pass

for i in range(10):
    t = threading.Thread(target=f)
    t.setDaemon(True)
    t.start()

time.sleep(60)

