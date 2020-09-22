# sqliteEx03.py
import sqlite3

class SqliteDB:
    def __init__(self, dbname):
        print('생성자 출력')
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()

    def __del__(self):# 소멸자(마감 처리 용도)
        print('소멸자 출력')
        self.cursor.close()
        self.conn.close()

    def getJoinData(self): # 조인 데이터
        sql = " select st.id, st.name, st.birth, sg.subject, sg.jumsu"
        sql += " from students st join sungjuk sg "
        sql += " on st.id = sg.id"

        result = self.cursor.execute(sql)
        return result

    def getSubQuery(self, name):
        sql = " select * from sungjuk "
        sql += " where id = (select id from students where name = '%s')"

        result = self.cursor.execute(sql % (name))
        return result

    # 고아라, 심형래 구현해 보세요
    def getJumsu(self, name):
        sql = " select jumsu  from sungjuk "
        sql += " where id = (select id from students where name = '%s')"

        mydata = self.cursor.execute(sql % (name))

        total = 0 # 총점
        cnt = 0 # 행 갯수

        for row in mydata :
            total += row[0]
            cnt += 1

        if cnt != 0:
            average = total / cnt
            print('총점 : ', dataset[0])
            print('평균 : ', dataset[1])
            return (total, average)
        else:
            print('존재하지 않는 회원입니다.')
            return None


dbname = 'sqlitedb.db'
mydb = SqliteDB(dbname)

dataset = mydb.getJoinData()
for row in dataset :
    print(row)
print('#'*30)

who = '이문세'
dataset = mydb.getSubQuery(who)
for (id, subject, jumsu) in dataset:
    print('아이디 :', id, end='', sep='')
    print(', 과목 :', subject, end='', sep='')
    print(', 점수 :', jumsu, end='', sep='')
    print()

print('#'*30)

who = '심형래' # '고아라'
dataset = mydb.getJumsu(who)

# if dataset != None :
#     print('총점 : ', dataset[0])
#     print('평균 : ', dataset[1])
# else :
#     print('존재하지 않는 회원입니다.')

print('#'*30)

print('finished')

