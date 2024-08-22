import random
from threading import Thread

myArray = []
for i in range(1000):
    myArray.append(random.randint(1, 1000))
sumFilhos=0

def somar(inicio, posicoes):
    global sumFilhos
    for i in range(posicoes):
        sumFilhos += myArray[inicio+i]
    #for i in myArray[inicio:inicio+posicoes]:
    #    sumFilhos += i
    

threads = []
for i in range(5):
    threads.append(Thread(target=somar, args=(i*200, 200)))

for t in threads:
    t.start()
for t in threads:
    t.join()

sumPai = 0
for i in myArray:
    sumPai += i

print(sumPai, sumFilhos)