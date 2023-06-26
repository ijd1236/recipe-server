# 사진을 업로드하는 API 만들기

## AWS S3

![20230626_101727](https://github.com/ijd1236/recipe-server/assets/130967884/a5cf6dff-41c3-4e36-aa03-a0ba8d735cda)
![20230626_101754](https://github.com/ijd1236/recipe-server/assets/130967884/70ede43f-81b7-4e2c-8e80-92635ebe1554)

- 먼저 AWS에서 S3에 들어가 버킷 만들기를 눌러줍니다.

  
![20230626_101951](https://github.com/ijd1236/recipe-server/assets/130967884/310ba57d-2271-45f5-92d3-04daea4e5a98)

- ( 버킷 이름은 유니크해야합니다.)
- 
![20230626_102003](https://github.com/ijd1236/recipe-server/assets/130967884/008c3b8b-7e54-408c-8ff3-c8120a3898ec)
![20230626_102015](https://github.com/ijd1236/recipe-server/assets/130967884/6016ba2c-b7c4-42e6-8ff9-ea5bad23abd5)

- 다음과 같이 ACL 활성화, 모든 퍼블릭 액세스 차단을 선택, 확인까지 선택후 버킷만들기를 눌러줍니다.

![20230626_103117](https://github.com/ijd1236/recipe-server/assets/130967884/2c2ae152-fcac-4e52-8ba8-892b20ef41f4)
![20230626_103203](https://github.com/ijd1236/recipe-server/assets/130967884/317a2d77-e2d5-4275-9cbc-462de6938450)


- 여기서 파일을 업로드할 수 있습니다.

![20230626_103419](https://github.com/ijd1236/recipe-server/assets/130967884/a832dd2c-0578-44a4-9ea1-7a555b04c21d)

![20230626_103431](https://github.com/ijd1236/recipe-server/assets/130967884/c6060114-f6ca-423e-8f76-5c05856bdb27)

- 다음 권한에서 엑세스 제어목록에 편집을 클릭합니다.

![20230626_103522](https://github.com/ijd1236/recipe-server/assets/130967884/09509fa7-4c03-4dc0-aba9-e1677fe57fb4)


- 다음과 같이 변경하고 변경사항 저장을 클릭합니다.
- 
## 서버를 만들고 파일 업로드하기

![image](https://github.com/ijd1236/recipe-server/assets/130967884/4bc4f6b2-b74c-4478-a223-e71f1dc4679f)


- 먼저 API를 테스트할 postman에 리퀘스트를 생성해줍니다

-  Key 에는 photo(File) Value 에는 사진을 업로드시켜줍니다



- severless framework에서 aws-image-openapi-test 이름의 앱을 새로 만들어 줍니다.
- 서버를 만든후 VS코드에서 배포까지 완료합니다
- vs코드에서 boto3 라이브러리를 설치해줍니다.
- boto3는 파이썬에서 AWS(Amazon Web Services)를 제어하기 위한 오픈 소스 라이브러리입니다. boto3를 사용하면 AWS의 다양한 서비스에 대한 클라이언트를 생성하고, 리소스를 관리하며, API 호출을 수행할 수 있습니다.
- 이제 사진을 올리는 class를 작성합니다

```Python

class PhotoResource(Resource):

    def post(self):

        print(request.files)

        # 사진이 필수인 경우의 코드
        if 'photo' not in request.files :
            return {'result' : 'fail', 'error' : '파일 없음'}, 400
        
        # 유저가 올린 파일을 변수로 만든다.
        file = request.files['photo']

        # 파일명을 유니크하게 만들어준다.

        current_time = datetime.now()

        print(current_time.isoformat().replace(':', '_' ).replace('.','_')+'.jpg')

        new_filename = current_time.isoformat().replace(':', '_' ).replace('.','_')+'.jpg'

        # 새로운 파일명으로, s3에 파일을 업로드합니다.

        try:
            s3 = boto3.client('s3', 
                        aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY
                        )


          # 여기서 Config 에 들어갈 내용들은 config.py에 클래스를 등록하고 꺼내서 사용합니다. 코드는 다음과 같습니다
          
                #   class Config :
            
                # AWS_ACCESS_KEY_ID = '키'
                # AWS_SECRET_ACCESS_KEY = '시크릿키'
                # S3_BUCKET = ' S3 만들때 입력한 이름'
                # S3_BASE_URL = 'https://'+S3_BUCKET+'.s3.amazonaws.com/' # URL 형식
                        
            s3.upload_fileobj(file,
                               Config.S3_BUCKET, 
                               new_filename, 
                               ExtraArgs = {'ACL':'public-read', 'ContentType':'image/jpeg'})

        except Exception as e :
            print(str(e))
            return{'result':'fail', 'error':str(e)}, 500

        # 위에서 저장한 사진의 URL 주소를
        # DB에 저장해야 한다

        # URL 주소는 = 버킷명.s3주소/우리가만든 파일명
        file_url = Config.S3_BASE_URL + new_filename


        # 첫번째 파라미터는 파일명, 두번째 파라미터는 버킷명



        # 잘 되었으면, 클라이언트에 데이터를 응답한다.

        return {'result' : 'seccess', 'file_url': file_url}
```

![image](https://github.com/ijd1236/recipe-server/assets/130967884/e42e3b06-cb17-4974-af70-f8ad5326c602)

- app.py 에 api를 작동시킬 코드를 만들고 flask run을 입력해 작동시키고 제대로 나오는지 확인합니다

![image](https://github.com/ijd1236/recipe-server/assets/130967884/e61d136f-f6ea-4543-a533-26e134afd985)

- 제대로 실행됐으면 다음과 같이 URL 주소가 뜨며

![image](https://github.com/ijd1236/recipe-server/assets/130967884/275951d4-47bf-48cd-8895-d6f1b11d37a4)

- 해당 주소로 검색하면 사진이 나옵니다.

![image](https://github.com/ijd1236/recipe-server/assets/130967884/a42d34c8-65d7-4b2d-9148-59e024cbe300)

- 그리고 버킷에도 저장됩니다.

## 사진 정보를 분석해서 보여주기
https://docs.aws.amazon.com/ko_kr/rekognition/latest/dg/labels-detect-labels-image.html

![20230626_144237](https://github.com/ijd1236/recipe-server/assets/130967884/8f007a85-7e62-49ae-8353-1f0c3625adbe)

- Amazon Rekognition의 이미지 레이블 감지를 이용합니다.

![20230626_144920](https://github.com/ijd1236/recipe-server/assets/130967884/eea716bc-53c6-4b10-b348-0d3e019a1f07)

- 먼저 IAM에서 권한을 부여해줘야합니다 AmazonRekognitonFullAccess를 권한추가해줍니다.

![20230626_144929](https://github.com/ijd1236/recipe-server/assets/130967884/3323d5a5-9774-43cd-8ae0-cc85626ce864)

- 그 후 예제 함수를 복사해 vs코드에 위에서 입력했던 사진업로드 API에 추가합니다

```Python
class PhotoResource(Resource):

    def post(self):

        print(request.files)

        # 사진이 필수인 경우의 코드
        if 'photo' not in request.files :
            return {'result' : 'fail', 'error' : '파일 없음'}, 400
        
        # 유저가 올린 파일을 변수로 만든다.
        file = request.files['photo']

        # 파일명을 유니크하게 만들어준다.

        current_time = datetime.now()

        print(current_time.isoformat().replace(':', '_' ).replace('.','_')+'.jpg')

        new_filename = current_time.isoformat().replace(':', '_' ).replace('.','_')+'.jpg'

        # 새로운 파일명으로, s3에 파일을 업로드합니다.

        try:
            s3 = boto3.client('s3', 
                        aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY
                        )
            
            s3.upload_fileobj(file,
                               Config.S3_BUCKET, 
                               new_filename, 
                               ExtraArgs = {'ACL':'public-read', 'ContentType':'image/jpeg'})

        except Exception as e :
            print(str(e))
            return{'result':'fail', 'error':str(e)}, 500

        # 위에서 저장한 사진의 URL 주소를
        # DB에 저장해야 한다

        # URL 주소는 = 버킷명.s3주소/우리가만든 파일명
        file_url = Config.S3_BASE_URL + new_filename


        # Object Detection 한다
        # Rekognition 서비스 이용

        # 첫번째 파라미터는 파일명, 두번째 파라미터는 버킷명
        
        label_list = self.detect_labels(new_filename, Config.S3_BUCKET)      # 메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 합니다.



        # 잘 되었으면, 클라이언트에 데이터를 응답한다.

        return {'result' : 'seccess', 'file_url': file_url,
                'count' : len(label_list), 
                'items' :label_list}
    def detect_labels(self, photo, bucket):  # self를 추가해야합니다.

        client = boto3.client('rekognition',
                            'us-east-1',
                            aws_access_key_id = Config.AWS_ACCESS_KEY_ID,
                            aws_secret_access_key = Config.AWS_SECRET_ACCESS_KEY)

        response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},
            MaxLabels=10)

        print('Detected labels for ' + photo) 
        print()   


        label_list = []

        for label in response['Labels']:

            label_list.append(label['Name'])
            print ("Label: " + label['Name'])
            print ("Confidence: " + str(label['Confidence']))
            print ("Instances:")
            for instance in label['Instances']:
                print ("  Bounding box")
                print ("    Top: " + str(instance['BoundingBox']['Top']))
                print ("    Left: " + str(instance['BoundingBox']['Left']))
                print ("    Width: " +  str(instance['BoundingBox']['Width']))
                print ("    Height: " +  str(instance['BoundingBox']['Height']))
                print ("  Confidence: " + str(instance['Confidence']))
                print()

            print ("Parents:")
            for parent in label['Parents']:
                print ("   " + parent['Name'])
            print ("----------")
            print ()
        return label_list

```

- 이와 같은 코드로 완성합니다.
![image](https://github.com/ijd1236/recipe-server/assets/130967884/1b6d04fa-ee68-4e90-8414-8dcd4ab048f4)

![image](https://github.com/ijd1236/recipe-server/assets/130967884/913950f8-1429-444e-8b6f-16078dba6c17)

- 성공적으로 완료했으면 vs코드와 포스트맨에 다음과 같이 출력됩니다.







