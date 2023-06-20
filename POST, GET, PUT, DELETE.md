# POST, GET, PUT, DELETE

- 사전작업이 끝나면 본격적인 데이터 등록, 조회, 삭제, 업데이트, 회원가입, 로그인, 로그아웃 등을 실행하도록 하겠습니다.

- POST 메서드는 새로운 리소스를 생성하거나 데이터를 서버에 제출하는 데 사용됩니다. 
- 클라이언트가 서버에 데이터를 전송할 때 사용되며, 서버는 이 데이터를 처리하고 새로운 리소스를 생성합니다.

- GET 메서드는 서버로부터 리소스를 조회하기 위해 사용됩니다.
- 클라이언트가 서버에게 특정 리소스를 요청하고, 서버는 해당 리소스를 반환하여 클라이언트에게 제공합니다. 
- GET 요청은 데이터의 조회나 검색에 주로 사용됩니다.

- PUT 메서드는 서버에 존재하는 리소스의 내용을 수정하기 위해 사용됩니다. 
- 클라이언트는 수정할 리소스의 식별자와 수정할 내용을 함께 서버에 전송하고, 서버는 해당 리소스를 업데이트합니다.

- DELETE 메서드는 서버에 존재하는 리소스를 삭제하기 위해 사용됩니다. 
- 클라이언트가 삭제할 리소스의 식별자를 서버에 전송하면, 서버는 해당 리소스를 삭제합니다.

- GET 과 DELET는 Body에 데이터를 넣지 않습니다.

## 데이터 등록하기

- 서버에서 데이터 베이스에 데이터를 등록하는 방법을 실행합니다
- 이때는 post를 사용합니다
- recipe를 등록하기 위한 코드는 다음과 같습니다.

```Python
class RecipeListResource(Resource):

    def post(self) :

        # {
        # "name": "김치찌게",
        # "description": "맛있게 끓이는 방법",
        # "num_of_servings": 4,
        # "cook_time": 30,
        # "directions": "고기 볶고 김치 넣고 물 붓고 두부 넣고",
        # "is_publish": 1
        # }
        # 해당 데이터는 포스트맨에 입력할 데이터입니다. 포스트맨은 Json을 사용할것이기 때문에 ''가 아닌 ""로 입력해야합니다.


        # 1. 클라이언트가 보낸 데이터를 받아옵니다.
        data = request.get_json()   # 클라이언트로부터 전송된 JSON 데이터를 가져오는 Flask에서 제공하는 메서드입니다. 
                                    # 이 메서드를 사용하여 POST 또는 PUT 요청의 본문에서 JSON 데이터를 추출할 수 있습니다.


        print(data) # 전송된 데이터가 어떤 데이터 인지 테이블에 보여지게 합니다


        # 2. DB에 저장한다.

       API에서 try-except 구문은 예외 상황을 처리하고 적절한 응답을 반환하는 데 사용될 수 있습니다. 
       예외가 발생하는 상황에 대한 처리를 위해 try 블록 내부에 해당 코드를 작성하고,
       예외가 발생하면 except 블록에서 예외를 처리하는 코드를 작성합니다.


      
        try : 
            # 2-1. 데이터베이스를 연결한다.
            connection = get_connection()   # 사전작업에서 만들어뒀던 mysql과 연결할 때 쓰는 함수입니다.
            # 2-2 쿼리문을 만든다
          
            ## 중요 : 컬럼과 매칭되는 데이터만 %s 로 바꿔준다.

            query = '''insert into recipe
            (name, description, num_of_servings, cook_time, directions, is_publish, user_id)
            values
            (%s, %s, %s,%s , %s, %s,%s);   # sql에서의 데이터 추가 형식입니다 values 값엔 앞으로 입력할 값이니 %s로 처리합니다.
                        
            '''
            # 2-3. 쿼리에 매칭되는 변수 처리 튜플로 처리해준다. query %s에 들어갈것들 
            record = (data['name'], data['description'], data['num_of_servings'], data['cook_time'], data['directions'], data['is_publish'])

            # 2-4. 커서를 가져온다.
            cursor = connection.cursor()

            # 2-5. 쿼리문을, 커서로 실행한다.
            cursor.execute(query,record)
            # 2-6. DB에 반영 완료하라는, commit 해줘야한다.
            connection.commit()
            # 2-7.자원해제
            cursor.close()
            connection.close()

    
        except Error as e:
            print(e)
            return {'result' : 'fail', 'error' : str(e)}, 500

        # 3. 에러가 났으면, 에러가 났다고 알려주고
        #    그렇지 않으면 잘 저장됐다고 알려준다.
        return {'result':'success'}
```

- 서버에 코드를 입력후 저장 -> 테이블에서 flask run 을 입력해 실행합니다.

![image](https://github.com/ijd1236/recipe-server/assets/130967884/0e6e62c3-a2a1-4e65-9d23-85e7aef8832d)

- 포스트맨에서 서버를 등록합니다 레시피 서버에서 리퀘스트를 생성
- POST를 선택하고 주소를 입력합니다


![image](https://github.com/ijd1236/recipe-server/assets/130967884/c7767bfc-427a-42ca-9bc3-0b0d464d61d1)



- 이후 Body에서 raw -> Json을 선택,
- 위에서 적은 데이터를 입력하고 저장을 합니다.
- 그 후 send를 눌러 실행합니다.

![image](https://github.com/ijd1236/recipe-server/assets/130967884/043dfc4d-59a9-4263-af20-ea6d32c8b20a)

- 포스트맨 화면에 위에서 성공했을 시 출력하려는 내용이 나온다면 성공한것입니다

- ![image](https://github.com/ijd1236/recipe-server/assets/130967884/aab9019e-82be-4f61-ae1a-507520f1dd3b)

- mysql 에 들어가서 데이터가 정상적으로 들어갔는지 확인합니다


## 데이터 검색하기

- 데이터베이스 내에 저장되어 있는 데이터를 검색합니다.

- 이때는 get 함수를 사용합니다.


```Python
    def get(self) :

        # 1. 클라이언트로 부터 데이터를 받아온다.
        # 2. 저장된 레시피 리스트를 DB로부터 가져온다.
        # 2-1. DB 커넥션

        try :
            connection = get_connection()

            # 2-2. 쿼리문 만든다.

            qeury = '''select r.*, u.username
                    from recipe r
                    join user u 
                    on r.user_id = u.id
                    where is_publish = 1;'''
            # 2-3 . 변수로 처리할 부분은 변수처리한다.

            # 2-4. 커서 가져온다,
            cursor = connection.cursor(dictionary= True) 포스트맨에 출력해야하기에  # dictionary = True 를 입력하여 MySQL 커서 객체를 생성할 때
            # 딕셔너리 형식으로 결과를 반환하도록 지정합니다.
            # 2-5. 쿼리문을 커서로 실행한다.
            cursor.execute(qeury)

            # 2-6.실행결과를 가져온다.
            result_list = cursor.fetchall()   # cursor.fetchall() 함수를 사용하여 실행한 쿼리의 결과를 모두 가져와서 result_list 변수에 저장합니다
            print(result_list)   # vs코드 터미널에서도 출력해서 보이게.

            cursor.close()
            connection.close()
        
        except Error as e :
            print(e)
            return {'result' : 'fail', 'error' : str(e)}, 500

    

        # 3. 데이터가공이 필요하면, 가공한 후에
        #    클라이언트에 응답한다.
        # 해당 데이터는 creat_at 과 updated_at 이 시간으로 되어있어 가공해야합니다
        
        i = 0
        for row in result_list :
            result_list[i]['created_at'] = row['created_at'].isoformat()    
            result_list[i]['updated_at'] = row['updated_at'].isoformat()    
            i = i + 1

        return {'result' : 'success', 
                'count' : len(result_list),
                'items' : result_list}
```

- 해당 코드를 입력후 flask run으로 서버 실행 후 포스트맨에서 실행하면

![image](https://github.com/ijd1236/recipe-server/assets/130967884/700fe671-e7f1-4bbe-ac35-cb0a840aa858)

- 다음과 같이 데이터베이스에 있는 데이터를 출력해서 보여줍니다



  




