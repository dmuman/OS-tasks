#TP07 ex2

from multiprocessing import Process, Array, Semaphore
import random, time

MAX_SIZE = 1
buffer = Array("i", MAX_SIZE)

empty = Semaphore(MAX_SIZE) #Inicialmente, MAX_SIZE posicoes livres
full = Semaphore(0) #Inicialmente, 0 posicoes ocupadas

def produtor():
    while True:
        nextProduced = random.randint(1,100)
        empty.acquire() #Ha’ posicoes livres?
        buffer[0] = nextProduced
        full.release() #Informo que há nova posicao ocupada
        print ("+++Produzi ", str(nextProduced))
        time.sleep(random.randint(0,3)) #descanso um pouco

def consumidor():
    while True:
        full.acquire()
        nextConsumed = buffer[0]
        empty.release()
        print ("---Consumi ", str(nextConsumed))
        time.sleep(random.randint(0,3)) #descanso um pouco

prod = Process(target=produtor)
cons = Process(target=consumidor)

prod.start()
cons.start()

prod.join()
cons.join()