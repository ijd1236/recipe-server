# 환경 설정

## MySQL 사전작업

![image](https://github.com/ijd1236/recipe-server/assets/130967884/ed564cb5-a486-4373-a453-5377092081e9)

- 기존 MySQL Connection에서 서버가 DB에 접속할 수 있도록 계정을 생성한후
- garnat all로 권한을 부여합니다.

![image](https://github.com/ijd1236/recipe-server/assets/130967884/5338191c-29ea-49bb-a3b0-5a98f80f0565)

- 그 후 recipe 데이터베이스를 만들고 테이블을 만들어줍니다.


![image](https://github.com/ijd1236/recipe-server/assets/130967884/7d160729-90ba-49fa-84a0-44291d4ed9bf)

- 위에서 생성한 계정을 토대로 새로운 MySQL Connection 을 만듭니다.

![image](https://github.com/ijd1236/recipe-server/assets/130967884/00077f62-9a1b-467e-b0b4-67d1d3b69e4d)

- 그럼 기존 MySQL Connection에서 recipe_db 데이터베이스가 새로 만든 '레시피 디비' 생성된걸 확인할 수 있습니다.

## git허브, vs코드 설정


- 먼저 git허브에서 새로운  repository를 생성한 후 클론해주고 vs 코드로 실행합니다
- 
- ![image](https://github.com/ijd1236/recipe-server/assets/130967884/071bcda3-4a4f-49d9-926f-31491d989765)

- vs코드에서 파이썬 3.10 버젼으로 lambda_app 가상환경을 만듭니다.

- 가상환경 터미널에서 pip install flask-restful을 입력하여 설치합니다/
- Flask-RESTful는 Flask 웹 프레임워크를 기반으로 한 RESTful API 개발을 위한 확장(Extension)입니다.
-  RESTful API는 Representational State Transfer의 약자로,
-   웹 서비스의 자원을 URI(Uniform Resource Identifier)로 표현하고, HTTP 메서드(GET, POST, PUT, DELETE 등)를 사용하여 자원을 조작하는 스타일을 의미합니다.
- Flask-RESTful는 Flask를 기반으로 RESTful API를 쉽게 개발할 수 있도록 도와주는 도구입니다.
- Flask-RESTful은 간편한 라우팅, 요청 파싱, 데이터 직렬화, 에러 처리 등의 기능을 제공하여 개발자가 API 개발에 집중할 수 있도록 도와줍니다.

- 설치가 완료되면
```Python
from flask import Flask
from flask_restful import Api  

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.

api = Api(app) # Flask 객체에 Api 객체 등록
```
- 다음과 같은 코드를 입력 후

-   터미널에 flask run 을 입력하여 웹 애플리케이션을 실행합니다.
![image](https://github.com/ijd1236/recipe-server/assets/130967884/a485b4ca-fe23-420c-9980-a0117953c3d7)

- 실행하면 다음과 같이 url 주소가 뜨게됩니다.

## Post man

- 서버를 개발하기 위해서 우선 포스트맨(Post man) 앱을 설치합니다
- 포스트맨은 HTTP 요청을 작성하기 위한 앱으로 
- Postman 컬렉션을 사용하면 관련 API 요청을 구성하고 그룹화할 수 있고
- API에 대한 OpenAPI 정의가 아직 없는 경우 컬렉션을 사용하면 사용자 지정 커넥터 개발을 더 빠르고 쉽게 만들 수 있습니다.
![image](https://github.com/ijd1236/recipe-server/assets/130967884/d102fdfc-182d-4a51-a8a8-531df1baa0c3)

![20230616_151232](https://github.com/ijd1236/recipe-server/assets/130967884/a501a12c-b7b0-4402-8867-8ad691682534)

- 설치가 완료되면 다음과 같이 커넥션을 생성합니다.

- 이로써 기본적인 환경설정은 완료했습니다


##  POST, GET, PUT, DELETE
- POST, GET, PUT, DELETE는 HTTP 프로토콜에서 사용되는 주요한 메서드(Methods)입니다. 
- 이들 메서드는 웹 애플리케이션에서 클라이언트와 서버 간의 통신을 위해 사용됩니다.

### 사전작업

- 먼저 경로와 API 동작코드(Resource)를 연결하기 위해 add_resource() 함수를 사용해야합니다
- add_resource()는 API 엔드포인트와 해당 엔드포인트에 대한 동작을 정의하는 데 사용됩니다.
- 첫번째 API 엔드포인트에 대한 동작을 구현한 리소스 클래스를 지정합니다. 리소스 클래스는 Flask-RESTful의 Resource 클래스를 상속받아야 합니다.
- class 란 비슷한 데이터끼리 모아놓은 것(테이블 생각)
- 클래스는 변수와 함수로 구성된 묶음
- 테이블과 다른점 : 함수가 있다는 점 


- 두번째론 '/endpoint': 클라이언트가 요청을 보낼 수 있는 엔드포인트의 URL 경로를 지정합니다. 이 경로는 사용자가 지정합니다.
- 첫번째 resource를 상속받는 클래스를 설정하기 위해 vs코드에 폴더를 생성하고 , 파일을 생성하여 작성하겠습니다.
- resource라는 새로운 폴더를 생성하고 그 안에 recipe.py라는 파일을 생성하였습니다.
![image](https://github.com/ijd1236/recipe-server/assets/130967884/5847dd27-e9c8-478b-a173-8fe1b6b6f7f6)

- recipe.py 파일에 
```Python
class RecipeResourve(Resource):
    pass
```
- 다음과 같이 Rescource 함수를 상속하는 





파이썬 MySQL Connector 라이브러리 (설치방법)
Python 에서 MySQL 커넥하는법 (전용 DB 유저 생성 포함)
Python 에서 MySQL 에 데이터 인서트 하는 방법
Python MySQL Connector 셀렉트 하는 방법과 코드
