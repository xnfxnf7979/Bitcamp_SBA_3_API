# touristResource.py
# 공공 기관 데이터 : 관광 자원 통계 서비스
# https://www.data.go.kr/에 로그인 해주세요.
'''
처리 순서
    1) end_point 문자열을 생성합니다.
    2) 일반 인증 키를 발급 받습니다.
    3) 요청을 하기 위한 url 변수를 만듭니다.
'''

import urllib.parse
import urllib.request
import json
import math

import datetime # 시각에 대한 정보를 출력해주는 모듈

# 인증 키
access_key = 'wsQr1RtV60YPSHZ9NJMn1eb4Gjpt7RX2s2ApX54K6kGkqPo5S2aTobobjCimSbaQ0DQB6qoXjz4yIaX9TDPSig%3D%3D'

# 해당 url 문자열을 이용하여 정보를 읽어 옵니다.
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200 : # 문제 없슴
            # print('url 정보 : [%s]' % (url))
            # print('발생 시각 : [%s]' % (datetime.datetime.now()))
            return response.read().decode('utf-8')

    except Exception as err :
        # print(err)
        # print('발생 시각 : [%s]' % (datetime.datetime.now()))
        print('오류 발생 url : [%s]' % (url))
        return None

def getTourData(yyyymm, sido, gungu, nPageNum, maxRecords):
    # end_point와 parameters를 이용하여 url을 생성합니다.
    # getRequestUrl() 함수를 호출하여 url이 반환하는 정보를 추출합니다.
    end_point = 'http://openapi.tour.go.kr/openapi/service'
    end_point += '/TourismResourceStatsService'
    end_point += '/getPchrgTrrsrtVisitorList'

    parameters = '?'
    parameters += '_type=json'  # json으로 받겠다.
    parameters += '&serviceKey=' + access_key
    parameters += '&YM=' + yyyymm
    parameters += '&SIDO=' + urllib.parse.quote(sido)
    parameters += '&GUNGU=' + urllib.parse.quote(gungu)
    parameters += '&RES_NM=' + ''
    parameters += '&pageNo=' + str(nPageNum)
    parameters += '&numOfRows=' + str(maxRecords)

    url = end_point + parameters
    # print(url)
    result = getRequestUrl(url)

    if result == None :
        return None
    else :
        return json.loads(result)
# end def getTourData

def TourPointCorrection(item, yyyymm, jsonResult):
    # 전처리 : 해당 키가 존재하지 않는 경우, 기본 값으로 대체 데이터를 만들어 주는 함수
    # item 키중에 'addrCd'이 존재하면 그대로 사용, 없으면 0으로 대체하시오.
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd']
    gungu = 0 if 'gungu' not in item.keys() else item['gungu']
    sido = 0 if 'sido' not in item.keys() else item['sido']
    resNm = 0 if 'resNm' not in item.keys() else item['resNm']
    rnum = 0 if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']

    jsonResult.append({'yyyymm':yyyymm, 'addrCd':addrCd, 'gungu':gungu, 'sido':sido, 'resNm':resNm, 'rnum':rnum, 'ForNum':ForNum, 'NatNum':NatNum})
# end def TourPointCorrection 함수 끝


def main():
    jsonResult = [] # 전체 목록을 저장할 변수
    sido = '서울특별시' # 시도
    gungu = '' # 군구
    nStartYear = 2015 # 검색 시작 년도
    nEndYear = 2019  # 검색 종료 년도
    nPageNum = 1 # 페이지 번호
    maxRecords = 100 # 조회될 행의 최대 수

    for year in range(nStartYear, nEndYear+1):
        for month in range(1, 13):
            yyyymm = '%s%s' % (str(year), str(month).zfill(2))
            # print(yyyymm)

            while(True):
                jsonData = getTourData(yyyymm, sido, gungu, nPageNum, maxRecords)
                # print(jsonData)

                # 응답 결과가 'OK'이면
                if jsonData['response']['header']['resultMsg'] == 'OK' :
                    nTotal = jsonData['response']['body']['totalCount']
                    if nTotal == 0: # 데이터가 없슴
                        break

                    dataSet = jsonData['response']['body']['items']['item']
                    if dataSet != None :
                        for item in dataSet:
                            TourPointCorrection(item, yyyymm, jsonResult)

                    nPage = math.ceil(nTotal / 100)
                    if(nPageNum == nPage):
                        break # 마지막 페이지 입니다.

                    nPageNum += 1
                else :
                    break
            # end while
            # break  # 차후에 삭제 예정
        # end inner for
        # break  # 차후에 삭제 예정
    # end outer for

    # 파일 저장하기
    # touristResource(서울특별시 2015~2019).json
    savedFilename = 'touristResource(%s %d~%d).json'

    with open(savedFilename % (sido, nStartYear, nEndYear), 'w', encoding='utf-8') as outfile :
        retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(retJson)

    print(savedFilename % (sido, nStartYear, nEndYear) + ' 파일 저장됨')

if __name__ == '__main__' :
    main()

print('-'* 30)
