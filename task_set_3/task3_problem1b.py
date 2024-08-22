import os, sys
from multiprocessing import Process, Value

n = Value("i", 0)

def incrementar():
    global n
    for i in range(1000):
        n.value += 1
    print("processo, n=", str(n.value))

processos = []
for i in range(2):
    processos.append(Process(target=incrementar))

for process in processos:
    process.start()

for process in processos:
    process.join()


print("processo pai, n=", str(n.value))