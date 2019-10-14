name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict();
for line in handle:
    if line.startswith("From ") :
       line = line.split(':')
       line = line[0].split()
       if line[5] not in counts :
         counts[line[5]] = 1
       else :
         counts[line[5]] = counts[line[5]] + 1
for hr,cnt in sorted(counts.items()) :
   print(hr,counts[hr])