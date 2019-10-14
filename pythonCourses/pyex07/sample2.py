# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
x=0
smnum=0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        x=x+1
        s=line[line.rstrip().find(':')+1:]
        smnum=smnum+float(s)

avg=float(smnum/x)

print('Average spam confidence: '+str(avg))
