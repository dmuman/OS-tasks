import os, sys
import random
from multiprocessing import Process, Array

myArray = []
for i in range(1000):
    myArray.append(random.randint(1, 1000))

resultadosFilhos = Array("i", 5)
sumFilhos=0

def somar(id, inicio, posicoes):
    global resultadosFilhos, myArray, sumFilhos
    for i in range(posicoes):
        sumFilhos += myArray[inicio+i]
    resultadosFilhos[id] = sumFilhos

 #implementar a soma e colocar o resultado em sumFilhos

# implementar a criação, execução e a finalização dos processos filhos.

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