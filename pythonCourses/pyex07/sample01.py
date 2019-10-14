fname = input('Enter the filename: ')
fhand = open(fname)
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From: ')
        continue
    print(line)
