import sqlite3
con = sqlite3.connect('users.db')
cur = con.cursor()
cur.execute('Create Table chats (name varchar(30), liked varchar(300), disliked varchar(300), muted bool, prev_channel varchar(50))')
con.commit()
cur.execute("INSERT into data values ('1841852990', '[]', '[]', 0, '')")
con.commit()
##print(cur.execute('select * from data').fetchall())
