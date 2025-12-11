import threading
import time

def print_1():
    print("start of thread", threading.current_thread().name)
    time.sleep(2)
    print("end of thread", threading.current_thread().name)

def print_2():
    print("start of thread", threading.current_thread().name)
    time.sleep(3)
    print("end of thread", threading.current_thread().name)

a = threading.Thread(target=print_1, name="thread 1")
b = threading.Thread(target=print_2, name="thread 2")

a.start()
b.start()