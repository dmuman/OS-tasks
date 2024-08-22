import sys, struct, pickle

def readPkl(filename):
    try:
        soma = 0.0

        with open(filename,"rb") as inFile:
            x = pickle.load(inFile)
            for i in x:
                soma += i

        return soma

    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)

print(readPkl("floats.pkl"))