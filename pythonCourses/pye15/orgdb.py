import sqlite3
conn = sqlite3.connect('pye4db')
cur = conn.cursor()

cur.execute('Drop table if exists Counts')
cur.execute('''
Create table counts(org text, count integer)''')

fname=input("enter file name: ")
if (len(fname) < 1): fname='mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    chunk = pieces[1].split('@')
    org = chunk[1]
    cur.execute('Select count from Counts where org = ? ',(org,))
    row= cur.fetchone()
    if row is None:
        cur.execute('''Insert into Counts(org, count) Values(?,1)''',(org,))
    else:
        cur.execute('Update Counts set count = count+1 where org =?',(org,))
conn.commit()
sqlstr = 'Select org, count from Counts order by count'
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()
