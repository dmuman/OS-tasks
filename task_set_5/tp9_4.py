import sys, struct, pickle

#a)
def readTextSaveList(filename):
    try:
        f = open(filename, "rt")
        lista = []
        for i in f:
            lista.append(float(i))
        f.close()
        return lista
    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)

print(readTextSaveList("floats.txt"))

#b)
def pickling(filename):
    try:
        
        with open("floats.pkl","wb") as outFile:
            pickle.dump(readTextSaveList(filename), outFile)

    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)

pickling("floats.txt")