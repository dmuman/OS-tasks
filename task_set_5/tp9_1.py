import sys, struct
def writeText(n, filename):
    try:
        f = open(filename, "wt")
        f.write(str(n))
        f.close()
    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)

        
def writeBin(n, datatype, filename):
    try:
        f = open(filename, "wb")
        f.write(struct.pack(datatype, n))
        f.close()
    except IOError as e:
        print("open failed ", e.errno, '-', e.strerror, file=sys.stderr)
        sys.exit(1)


a = 15 # 0000 000F
writeText(a, 'a.txt')
writeBin(a, 'i', 'a.bin')
b = 1.5 # 0x3FC0 0000
writeText(b, 'b.txt')
writeBin(b, 'f', 'b.bin')
c = 1.5555555555 # 0x3FC7 1C72
writeText(c, 'c.txt')
writeBin(c, 'f', 'c.bin')
d = 1/3 # 0x3EAA AAAB
writeText(d, 'd.txt')
writeBin(d, 'f', 'd.bin')