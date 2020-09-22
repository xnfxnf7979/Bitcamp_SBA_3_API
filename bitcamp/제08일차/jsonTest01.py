# jsonTest01.py
import json

# data = {'age':30, 'name':'홍길동', 'address':'강남구 역삼동', 'broadcast':{'mbc':11, 'kbs':9, 'sbs':5}}

data = {'response': {'header': {'resultCode': '0000', 'resultMsg': 'OK'}, 'body': {'items': {'item': [{'addrCd': 1111, 'csForCnt': 23453, 'csNatCnt': 49390, 'gungu': '종로구', 'resNm': '창덕궁', 'rnum': 1, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1111, 'csForCnt': 108087, 'csNatCnt': 196594, 'gungu': '종로구', 'resNm': '경복궁', 'rnum': 2, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1111, 'csForCnt': 1326, 'csNatCnt': 24256, 'gungu': '종로구', 'resNm': '창경궁', 'rnum': 3, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1111, 'csForCnt': 3112, 'csNatCnt': 9854, 'gungu': '종로구', 'resNm': '종묘', 'rnum': 4, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1117, 'csForCnt': 6513, 'csNatCnt': 339073, 'gungu': '용산구', 'resNm': '국립중앙박물관', 'rnum': 5, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1114, 'csForCnt': 8989, 'csNatCnt': 54159, 'gungu': '중구', 'resNm': '덕수궁', 'rnum': 6, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1135, 'csForCnt': 11, 'csNatCnt': 1754, 'gungu': '노원구', 'resNm': '태릉 ·  강릉 · 조선왕릉전시관', 'rnum': 7, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1141, 'csForCnt': 5355, 'csNatCnt': 23464, 'gungu': '서대문구', 'resNm': '서대문형무소역사관', 'rnum': 8, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1141, 'csForCnt': 0, 'csNatCnt': 44478, 'gungu': '서대문구', 'resNm': '서대문자연사박물관', 'rnum': 9, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1144, 'csForCnt': 30234, 'csNatCnt': 10756, 'gungu': '마포구', 'resNm': '트릭아이미술관', 'rnum': 10, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1165, 'csForCnt': 2, 'csNatCnt': 1362, 'gungu': '서초구', 'resNm': '헌릉ㆍ인릉', 'rnum': 11, 'sido': '서울특별시', 'ym': 201501}, {'addrCd': 1168, 'csForCnt': 569, 'csNatCnt': 12155, 'gungu': '강남구', 'resNm': '선릉·정릉', 'rnum': 12, 'sido': '서울특별시', 'ym': 201501}]}, 'numOfRows': 100, 'pageNo': 1, 'totalCount': 12}}}

# dumps() 함수 : 데이터를 읽어서 str 형태로 바꿔주는 함수이다.
json_str = json.dumps(data, ensure_ascii=False, indent=4, sort_keys=True)
print(json_str)

# print(type(json_str))
# print('-'*30)
#
# json_data = json.loads(json_str)
# print(json_data)
# print(type(json_data))
# print('-'*30)
#
# print(json_data['name'])
# print(json_data['age'])
# print(json_data['broadcast']['sbs'])
#
# print('-'*30)