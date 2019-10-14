import re
name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_40190.txt"
handle = open(name)
Y = 0
for line in handle:
    line.rstrip();
    xlst = re.findall('[0-9]+',line)
    if len(xlst) > 0 :
        for i in xlst:
            Y = Y + int(i)
print(Y)