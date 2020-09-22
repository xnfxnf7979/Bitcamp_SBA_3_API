클래스 하나가 단위 unit이 된다
확장해보자
객체지향에서는 디자인패턴이라는 개념이 존재한다
1994년 GoF 4인방 개발자 에릭 감마 . . . 
==>vscode 개발자

패턴조합을 통해 큰 개념의 패턴 => MVC 패턴이라고 한다
model, view, controller 이렇게 조합한다. -> Java, C 언어에서 주로 사용하는 개념

model : 데이터 처리 => API 서버 => Python => Tensorflow
view : 화면 UI 처리 => UI 서버 => Reactjs
controller : model + view 를 연결 ==> 네트워크 처리 => flask (app.py) => RESTful 방식

이 지점에서 팀내에서 나의 역할을 고민해야 한다
곧 취업시 자신을 어필할 수 있는 혹은 자신있는 카테고리 결정하기
Backend Tier (API 서버 구축 담당 : Java, C, Python, )
Frontend Tier (UI 서버 구축 담당 : JavaScript, HTML, Reactjs)

모델을 제작하고 뷰를 만들어서 컨트롤러로 연결한다. <= 이 컨셉을 이해하기
프로토 타입 만들기
독자적으로 움직인다 => 모듈
5명 팀원이므로 5개의 모듈을 만들고, 이 모듈들을 조합했을 때 작동이 잘 된다면 1단계 성공

케글...가입하기

titanic 폴더에
dataset (test.csv, train.csv) 이 존재하고
entity(속성) + service(기능) = 객체(object)

def __init__(self, ...) => 속성
def abc() => 기능
결국 class 는 객체를 정의하는 것이다

class 가 여러개(entity, service) 다시 큰 개념의 객체를 이룬다. 이것을 클래스라 하지 않고 model 이라고 한다

패키지는 컨셉을 공유하는 클래스의 집합 ... 모듈 =(진화=)> 모델이 됨
모델에 AI 개념이 없으면 web에서 말하는 모델이고
AI 개념이 존재하면 인공지능 모델이 된다.


여기서 AI 개념이라고 하면 머신러닝 코딩의 유무
dataset 을 추가하면 이를 지도학습
dataset 이 없으면 비지도 학습 이라 한다
지금 타이타닉은 dataset을 모델에 넣었으므로 지도학습을 하겠단 뜻이 된다



