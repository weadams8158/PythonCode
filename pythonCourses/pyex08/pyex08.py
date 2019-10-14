fname = input("Enter file name: ")
fh = open(fname)
lst = list()
ln = list()
for line in fh:
    a=line.rstrip()
    lst=a.split()
    for x in lst:
        if x not in ln:
            ln.append(x)
ln.sort()
print(ln[:])
