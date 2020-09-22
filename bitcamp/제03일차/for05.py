# for05.py
mystring = input('문자열 입력 : ') # python is very easy

mylist = mystring.split()
print(type(mylist)) # type 함수는 해당 데이터의 유형을 알려 주는 함수
print(mylist)

for idx in range(len(mylist)) :
    if idx % 2 == 0 :
        mylist[idx] = mylist[idx].upper()
    else :
        mylist[idx] = mylist[idx].lower()

result = '#'.join(mylist)
print(result)