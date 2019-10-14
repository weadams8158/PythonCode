import sqlite3
conn = sqlite3.connect('pye4db')
cur = conn.cursor()

cur.execute('Drop table if exists Counts')
cur.execute('''
Create table counts(email text, count integer)''')

fname=input("enter file name: ")
if (len(fname) < 1): fname='mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('Select count from Counts where email = ? ',(email,))
    row= cur.fetchone()
    if row is None:
        cur.execute('''Insert into Counts(email, count) Values(?,1)''',(email,))
    else:
        cur.execute('Update Counts set count = count+1 where email =?',(email,))
conn.commit()
sqlstr = 'Select email, count from Counts order by count desc limit 10'
for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
cur.close()
