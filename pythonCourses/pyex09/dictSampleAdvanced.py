import string 
fname = input(' Enter the file name: ') 
try:
    fhandle = open(name)
except:
    print(' File cannot be opened:', fname) 
    exit()

counts = dict()
for line in fhandle:
    line = line.rsplit()
    line = line.translate( line.maketrans('', '', string.punctuation)) 
    line = line.lower() 
    words = line.split()   
    for word in words:
        counts[word] = counts.get(word,0) + 1
print counts

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount :
        bigword = word
        bigcount = count

print(bigword, bigcount)
