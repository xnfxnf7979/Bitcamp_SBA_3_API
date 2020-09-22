# variantArgs02.py

# minval : 튜플 요소에서 가장 큰 수와 가장 작은 수를 반환하는 함수 만들기
# def minval(*args):
#     mymin = min(args)
#     mymax = max(args)
#     return mymin, mymax

def minval(*args):
    mylist = [item for item in args]
    mylist.sort()
    return mylist[0], mylist[-1]

print(minval(3, 5, 8, 2)) # (2, 8)