from threading import Thread

n=10
def func():
    global n
    n+=1
    print ("hello, n=", n)

newT = Thread(target=func)
newT.start()
func()
newT.join()
