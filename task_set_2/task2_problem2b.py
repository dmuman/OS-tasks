from threading import Thread

n = 0
def incrementar():
    global n
    for i in range(50000000):
        n += 1
    print("thread, n=", n)

threads = []
for i in range(2):
    threads.append(Thread(target=incrementar))

for t in threads:
    t.start()

for t in threads:
    t.join()

print("main thread, n=", n)