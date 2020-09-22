# makeDict02.py
fruits = [('바나나', 10), ('수박', 20), ('오렌지', 30)]

mydict = dict() # empty dict

for key, value in fruits :
    mydict[key] = value

print(mydict)
print('-'*30)

mydict.clear()

fruits = [('바나나', 10), ('수박', 20), ('오렌지', 30), ('바나나', 50)]

for key, value in fruits :
    if not(key in mydict) : # 들어 있지 않으면
        mydict[key] = value
    else :
        imsi = mydict[key]
        mydict[key] = imsi + value

print(mydict)
print('-'*30)