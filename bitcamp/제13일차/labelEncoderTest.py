from sklearn.preprocessing import LabelEncoder

data = ['갑', '을', '병', '정', '을', '갑']

le = LabelEncoder() # 객체 생성
le.fit(data) # 피팅

result = le.transform(data)

print(result)