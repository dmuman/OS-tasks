#TP06 ex2 com mutex

import os, sys
import random
from multiprocessing import Process, Array, Lock #Semaphore

mutex = Lock() #ou Semaphore(1)

myArray = []
for i in range(1000):
    myArray.append(random.randint(1, 1000))

resultadosFilhos = Array("i", 5)
sumFilhos=0

def somar(id, inicio, posicoes):
    global resultadosFilhos, myArray
    somaLocal = 0
    for i in range(posicoes):
        somaLocal += myArray[inicio+i] #não ẽ preciso implementar o sincronização aqui pq myArray é um array simples
    mutex.acquire() #sincronização é só para dados partilhados
    resultadosFilhos[id] = somaLocal #resultadosFilhos é um array da memória partilhada
    mutex.release

processos = []
for i in range(5):
    processos.append(Process(target=somar, args=(i, i*200, 200)))

for process in processos:
    process.start()

for process in processos:
    process.join()

sumPai = 0
for i in myArray:
    sumPai += i

# calcula o sumFilhos a partir das somas locais em resultadosFilhos

for i in resultadosFilhos:
    sumFilhos += i

print(sumPai, sumFilhos)