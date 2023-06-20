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


## 저장된 데이터 가져오기

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


# 특정 데이터 가져오기, 수정, 삭제

- 저장된 데이터중 특정한 레시피만 검색해서 보여주거나 수정, 삭제를 할 수 있습니다.

-  그러기위해 RecipeResource class 와 app.py 에서 API 엔드포인트를 새로만들어줍니다

```Python
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
```

- 다음과 같이 엔드포인트를 만들어 줍니다
- 이때 , recipes 주소 뒤에 /<int:recipe_id>를 입력하여 숫자를 입력하면 해당 숫자의 데이터를 찾아냅니다.

  
## 특정 데이터만 가져오기



```Python
class RecipeResource(Resource):
    
    # GET 메소드에서, 경로로 넘어오는 변수는 get 함수의 파라미터로사용

   

    def get(self, recipe_id):   # 모든 데이터를 찾아올때와 다르게 self 외에도 recipe_id 라는 매개변수로 특정 데이터를 찾습니다.


        # 1. 클라이언트로부터 데이터를 받아온다.
        # 위의 recipe_id 에 담겨있다.
        print(recipe_id)
        print(type(recipe_id))
        
        # 2. 데이터베이스에 레시피 아이디로 쿼리한다.
        try :

            
            connection = get_connection()

            query = '''
                    select r.*, u.username
                    from recipe r
                    join user u on r.user_id = u.id
                    where r.id = %s;'''
            record = (recipe_id, )  # 하나만 있으면 튜플이 되지 않아서 , 를 입력해줘야합니다
            cursor =connection.cursor(dictionary=True)  #dictionary=True = json 형식으로가져오게한다
            cursor.execute(query, record)
            result_list = cursor.fetchall()    #fetchall 데이터 있는거 전부 가져와라
            print(result_list)
            cursor.close()
            connection.close()

        except Error as e :
            print(e)
            return{'result': 'fail', 'error':str(e)}, 500
        # 3. 데이터가공이 필요하면, 가공한 후에
        #    클라이언트에 응답한다.
        i = 0
        for row in result_list :
            result_list[i]['created_at'] = row['created_at'].isoformat()    
            result_list[i]['updated_at'] = row['updated_at'].isoformat()   
            i = i + 1
        if len(result_list) != 1:
            return{'result' : 'success', 'item' : {}}
        else :
            return{'result' : 'success', 'item' : result_list[0]}
```

- 코드 입력후 서버 실행 포스트맨에서 확인합니다

  ![image](https://github.com/ijd1236/recipe-server/assets/130967884/de35106a-4df2-4b0e-8167-e91d09d0fcb5)

- 특정 데이터가 출력된것을 확인합니다

## 특정 데이터 수정하기

- 포스트맨에서 데이터를 수정하여 데이터베이스에 보낼 수 있습니다

-  이때는 PUT 을 사용합니다.

  

```Python
    def put(self, recipe_id) :

        # 1. 클라이언트로부터 데이터 받아온다.
        print(recipe_id)
        # body 에 있는 json 데이터를 받아온다.
        data = request.get_json()
        # 2. 데이터베이스에 update 한다.
        try : 
            connection = get_connection()
            query = '''  update recipe
                        set name = %s, description =%s, num_of_servings = %s , cook_time = %s,
                        directions = %s, is_publish = %s
                        where id = %s and user_id = %s;
                    '''
            record = ( data['name'], 
                      data['description'] , 
                      data['num_of_servings'], 
                      data['cook_time'], 
                      data['directions'], 
                      data['is_publish'],
                      recipe_id)               # query와 record 에 데이터 베이스의 내용, 포스트맨 body에 들어갈 내용을 입력합니다
            cursor = connection.cursor()
            cursor.execute(query, record)
            connection.commit()    # 데이터베이스에 적용시킬것이니 커밋해줍니다.
            cursor.close()
            connection.close()

        except Error as e :
            print(e)
            return {'result': 'fail', 'error' : str(e)}, 500
        

        return {'result' : 'success'}


![image](https://github.com/ijd1236/recipe-server/assets/130967884/bb7cca87-d612-4683-a1ff-81d378ceb261)

- 포스트맨에서 수정할 데이터의 주소 10 (recipe_id) 를 입력, 그리고 Body에 수정할 내용을 입력하고 전송 후
- Mysql 데이터베이스에서 수정됐는지 확인합니다.

## 특정 데이터 삭제하기

- 특정 데이터를 찾아 그 데이터를  삭제합니다

```Python
    def delete(self, recipe_id):
        # 1. 클라이언트로부터 데이터 받아온다
        print(recipe_id)

        # 2. DB에서 삭제한다

        
        try:
            connection = get_connection()
            query = ''' delete from recipe
                        where id = %s and user_id = %s;
                    '''
            record = (recipe_id ,)   # 튜플에 하나 넣을때는 , 를 넣어야 튜플 유지됨
            cursor = connection.cursor()
            cursor.execute(query,record)
            connection.commit()
            cursor.close()
            connection.close()
        except Error as e :
            print(e)
            return{'result' : 'success', 'error' : str(e)}



        # 3. 결과를 응답한다.

        return {'result' : 'success'}

```

- 코드를 입력후 서버를 실행, 포스트맨에서
  
![image](https://github.com/ijd1236/recipe-server/assets/130967884/df01afa9-46b5-4217-91d1-22f86a0c99d8)

- 주소를 입력후 전송, Mysql에서 해당 데이터가 삭제됐는지 확인합니다.






