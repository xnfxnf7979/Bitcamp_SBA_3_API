'''
variable (변하는) vs constant (변하지 않는)

그 중에서 variable은 분류가 가능함
분류기준을 두고 나누는데

크게 2분하면
cate, nominal로 나뉜다

cate 는 ordinal, numeric 으로 나뉨

결국
ordinal, numeric, nominal
변수 편집방법은 3가지 중 하나가 됨

확률통계코딩은 정답보다는 적합의 개념

1. embarked 부터
    p.138 누락된 값 처리 참고
    embarked 는 지우면 안됨. dropna를 쓰면 안된단 뜻
    => p.139 의 방식으로 처리한다.

    여기서 null 값을 무엇으로 넣을 것인가
    평균값을 넣는 방식이 책에 나와있으나

    이 예제는 str 이다. 평균 구할 수 없음
    그러므로 가장 많이 승선한 항구로 대체한다.
    통계를 왜곡할 수 있지만 그 null의 수가 적어 무시한다.
    빈 값이 있으면 그 변수를 아예 사용할 수 없기 때문에 대신 차선을 선택한 것이다

    이 예제에서는 사우스펨튼에서 승선객의 비율이 높아 s로 대체하고자 한다


@staticmethod
def sex_nominal(this) -> object:
    # male = 0. female = 1
    this.train['Sex'] = this.train['Sex'].map({'male':0,'female':1})
    this.test['Sex'] = this.test['Sex'].map({'male':0,'female':1})
    return this

코딩은 반복된 코드를 싫어함.
for(),while()이 syntax가 존재하는 이유임
그래서 위 코드에서 반복을 피하기 위해 (지도학습의 숙명인 train과 test 둘다 편집해야하는 상황)

combine = [this.train, this.test] # train과 test를 하나의 객체로 묶어 쓸 수 있다
        sex_mapping = {'male':0,'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)

        this.train = this.train # overwriting
        this.test = this.test


=======================================================================================================

data 수집
    - 방법론
    - 정형 (스키마 구조 존재, 컴퓨터가 인식함)
    - 비정형 (스키마 구조가 존재하지 않음, 컴퓨터가 인식불가)
    - 웹 -> 웹 크롤링 -> 브라우저
    - 문서 -> 텍스트 마이닝 -> RE 정규 표현식
data 정제, 정형화
modeling
learning
machine
evaluation

===============================정규 표현식=======================================

? : unique (하나만 존재)
* : all (null 허용)
+ : not null
{n} : counting

------ 위 4개는 반드시 숙지 -------





=======================================================================================================

 








