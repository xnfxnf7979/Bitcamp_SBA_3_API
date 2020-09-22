import sqlite3

def getAllInfo( mycursor ):
    for onetuple in mycursor :
        print( '아이디 : ' + onetuple[0], end='')
        print( ', 과목 : ' + onetuple[1], end='')
        print( ', 점수 : ' + str(onetuple[2]), end='')
        print()

conn = sqlite3.connect('sqlitedb.db')
mycursor = conn.cursor()

try:
    mycursor.execute("drop table sungjuk")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')

mycursor.execute('''create table sungjuk
            (id text, subject text, jumsu integer)''')

mycursor.execute('insert into sungjuk values ("lee","java", 10)')
mycursor.execute('insert into sungjuk values ("lee","html", 10)')
mycursor.execute('insert into sungjuk values ("lee","python", 30)')

conn.commit()

datamylist = [ ('jo', 'java', 40), ('jo', 'html', 50), ('jo', 'python', 60), \
              ('ko', 'java', 70), ('ko', 'html', 80), ('ko', 'python', 90), ]
mycursor.executemany('insert into sungjuk values(?,?,?)', datamylist)
conn.commit()

sql = "select * from sungjuk"
mycursor.execute(sql)
print('-' * 40)
getAllInfo( mycursor ) # 함수 형태로 구현

print('-' * 40)
sql = 'select * from sungjuk order by id, subject'
for row in mycursor.execute(sql ):
    print(row)
print('-' * 40)

mycursor.close()
conn.close()
print('-' * 40)
print('작업 완료^^')