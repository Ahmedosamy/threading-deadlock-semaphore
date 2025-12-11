import threading
import time

receptionect = threading.Semaphore(5)


def enter_examinationroom(n):
    print(f"patient {n} is waiting for his turn")
    receptionect.acquire()
    print(f"patient {n} is in examination room")
    time.sleep(3)
    print(f"patient {n} is out of the examination room")
    receptionect.release()


patients = []

for i in range(10):
    patient = threading.Thread(target=enter_examinationroom, args=(i,))
    patients.append(patient)
    patient.start()