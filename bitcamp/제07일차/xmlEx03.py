# xmlEx03.py
from xml.etree.ElementTree import parse

# parse : xml 문서를 파싱해주는 함수
tree = parse('xmlEx_03.xml')
myroot = tree.getroot()
print(type(myroot))
print('-' * 30)

# 해당 속성들의 키를 list 형식으로 반환
print(myroot.keys())
print('-' * 30)

# 해당 속성들의 키와 값을 튜플로 가지는 list를 반환
print(myroot.items())
print('-' * 30)

print(myroot.get('설명'))
print('-' * 30)

print(myroot.get('qwert', '없을 경우 기본 값'))
print('-' * 30)

print(myroot.findall('가족'))
print('-' * 30)

family = myroot.find('가족')
print(family)
print('-' * 30)

# childs = family.getchildren()
childs = [item for item in family]
# print(childs)
# print('-' * 30)

for onesaram in childs :
    # print(onesaram)
    # print('#' * 30)
    elem = [item for item in onesaram]
    for abc in elem :
        print(abc.text)
        if abc.text == '이순자':
            print(abc.attrib['정보'])

    print('^' * 30)

print('%'*30)

allfamily = myroot.findall('가족')
for onefamily in allfamily:
    # families = [item for item in onefamily]
    for onesaram in onefamily:
        name = onesaram.find('이름')
        if name != None :
            print(name.text)
        else :
            print(onesaram.attrib['이름'])

print('%' * 30)

print('finished')

