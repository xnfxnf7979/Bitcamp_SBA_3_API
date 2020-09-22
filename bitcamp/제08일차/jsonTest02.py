# jsonTest02.py
# 첨부 파일 some.json을 이용하여 각 정보를 출력해보세요.
import json

filename = 'some.json'
myfile = open(filename, 'rt', encoding='utf-8')
print(type(myfile))

mystring = myfile.read()
print(type(mystring))

jsondata = json.loads(mystring)
print(jsondata)

name = jsondata['member']['name']
address = jsondata['member']['address']
phone = jsondata['member']['phone']
print(name + '/' + address + '/' + phone )


cafename = jsondata['web']['cafename']
id = jsondata['web']['id']
print(cafename + '/' + id )