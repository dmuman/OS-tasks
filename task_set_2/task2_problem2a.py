from threading import Thread

n = 0

def incrementar():
    global n
    for i in range(1000):
        n += 1
    print("thread, n=", n)

newT = Thread(target=incrementar)
newT.start()
newT.join()

print("main thread, n=", n)