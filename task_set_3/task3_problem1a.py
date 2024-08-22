import os, sys
from multiprocessing import Process

n=0
def incrementar():
    global n
    for i in range(1000):
        n += 1
    print("processo, n=", n)

processos = []
for i in range(2):
    processos.append(Process(target=incrementar))

for process in processos:
    process.start()

for process in processos:
    process.join()

print("processo pai, n=", n)