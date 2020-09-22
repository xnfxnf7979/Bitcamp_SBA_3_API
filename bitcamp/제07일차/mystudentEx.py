# mystudentEx.py
# mystudent.xml 파일을 읽어서 students.csv 파일을 만들기
# students.db 파일에 students 테이블을 생성하고, 데이터를 추가하세요.
# pandas.DataFrame, sqlite, xml 패키지
# 추가 사항 : csv 파일과 테이블에 총점과 평균도 같이 넣어 줘보기
import sqlite3

from xml.etree.ElementTree import parse
from pandas import DataFrame

tree = parse('mystudent.xml')
myroot = tree.getroot()
# print(type(myroot))

allstudents = myroot.findall('student')

totallist = []  #
for onesaram in allstudents:
    #     print(onesaram)
    childs = onesaram.getchildren()
    sublist = []
    for onedata in childs:
        sublist.append(onedata.text)

    total = float(sublist[1]) + float(sublist[2]) + float(sublist[3])
    sublist.append(total)

    average = float(total) / 3.0
    sublist.append(average)

    totallist.append(sublist)

# print( totallist )

mycolumn = ['이름', '국어', '영어', '수학', '총점', '평균']
myframe = DataFrame(totallist, columns=mycolumn)
# print(myframe)

myframe.to_csv('students.csv', encoding='utf-8')

conn = sqlite3.connect('student.db')
mycursor = conn.cursor()

try:
    mycursor.execute('drop table students')
except Exception as err:
    print('table not exists...')

mycursor.execute('''
    create table students(name text primary key, 
    kor number, eng number, math number, 
    total number, average number)
''')

for idx in range(len(myframe)):
    onerow = myframe.loc[idx]
    print(type(onerow))
    name = onerow['이름']
    kor = onerow['국어']
    eng = onerow['영어']
    math = onerow['수학']
    total = onerow['총점']
    average = onerow['평균']

    sql = "insert into students "
    sql += "values( '"
    sql += name + "', "
    sql += kor + ", "
    sql += eng + ", "
    sql += math + ", "
    sql += str(total) + ", "
    sql += str(average) + " "
    sql += " )"
    # print( sql )
    mycursor.execute(sql)

mycursor.close()
conn.commit()
conn.close()

print('finished')