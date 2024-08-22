#TP07 ex1

from multiprocessing import Process, Semaphore
import time

sem = Semaphore(0)

def primeiro():
    #sem acquire
    time.sleep(1)
    print ("Esta linha deve aparecer primeiro.")
    sem.release()


def segundo():
    sem.acquire()
    print ("Esta linha deve aparecer em ultimo!")
    #sem release

seg = Process(target=segundo)
prim = Process(target=primeiro)

seg.start()
prim.start()

prim.join()
seg.join()