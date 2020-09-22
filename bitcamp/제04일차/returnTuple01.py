# returnTuple01.py
# 튜플을 사용하여 반환되는 데이터를 여러개 만들기
def myfunc(su1, su2):
    if su2 == 0:
        temp = su1
    else :
        temp = su1 // su2

    return su1+su2, su1-su2, su1*su2, temp

su1 = 14
su2 = 5
result = myfunc(su1, su2)
print(result)
print('-'*20)


# 리스트의 모든 요소의 절대값을 구하고,
# 최대(max), 최소(min), 총합(sum), 평균을 튜플로 반환하세요.
def myfunc2(mylist):
    newlist = [abs(item) for item in mylist]
    mymax = max(newlist)
    mymin = min(newlist)
    mysum = sum(newlist)
    myavg = mysum / len(newlist)
    return mymax, mymin, mysum, myavg

mylist = [10, -20, 30, -50, 40]

result = myfunc2(mylist)
print(type(result))
print(result)
print('-'*20)

# 출력 결과 : (50, 10, 150, 30)








