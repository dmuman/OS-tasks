#TP06 ex1a com mutex

import os, sys
from multiprocessing import Process, Lock

mutex = Lock()

n=0
def incrementar():
    global n
    for i in range(1000):
        mutex.acquire()
        n += 1
        mutex.release()
    print("processo, n=", n)

processos = []
for i in range(2):
    processos.append(Process(target=incrementar))

for process in processos:
    process.start()

for process in processos:
    process.join()

print("processo pai, n=", n)