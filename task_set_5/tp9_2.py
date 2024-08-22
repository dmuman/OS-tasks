import sys, struct

def readText(filename):
    try:
        f = open(filename, "rt")
        soma = 0.0
        for i in f:
            soma += float(i)
        f.close()
        return soma
    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)

print(readText("floats.txt"))

       
def readBin(datatype, filename):
    try:
        f = open(filename, "rb")
        soma = 0.0
        for i in f.readlines(struct.pack(datatype)):
            soma += float(i)
        f.close()
        return soma
    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)

#print(readBin("f", "floats.bin"))