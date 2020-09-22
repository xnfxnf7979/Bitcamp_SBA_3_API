# 외부 패키지를 사용하는 방법 1
# import 패키지경로.모듈이름
import somefolder.mymath.mathMod

su = 4
result = somefolder.mymath.mathMod.square_root(su)
print(result)

import somefolder.mymath.mathMod
su1 = 2
su2 = 3
result = somefolder.mymath.mathMod.jegob(su1, su2)
print(result)

# 외부 패키지를 사용하는 방법 2
# from 패키지경로.모듈이름 import 함수이름
from somefolder.mymath.mathMod import square_root
su = 3
result = square_root(su)
print(result)

from somefolder.mymath.mathMod import jegob
su1 = 3
su2 = 4
result = jegob(su1, su2)
print(result)

# 외부 패키지를 사용하는 방법 3
# import 패키지경로.모듈이름 as 별칭
import somefolder.mymath.mathMod as imsi
su = 9
result = imsi.square_root(su)
print(result)

import somefolder.sansu.sansuMod
su1 = 14
su2 = 5
result = somefolder.sansu.sansuMod.add(su1, su2)
print(result)

# 뺄셈
su1 = 14
su2 = 5
result = somefolder.sansu.sansuMod.sub(su1, su2)
print(result)

from somefolder.sansu.sansuMod import add
result = add(su1, su2)
print(result)

import somefolder.sansu.sansuMod as imsi2
result = imsi2.add(10, 20)
print(result)