# 多线程
import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = BuckysMessenger(name='Send')
y = BuckysMessenger(name="receive")
x.start()
y.start()
