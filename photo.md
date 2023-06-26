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

- severless framework에서 aws-image-openapi-test 이름의 앱을 새로 만들어 줍니다.
- 서버를 만든후 VS코드에서 배포까지 완료합니다
- vs코드에서 boto3 라이브러리를 설치해줍니다
- boto3는 파이썬에서 AWS(Amazon Web Services)를 제어하기 위한 오픈 소스 라이브러리입니다. boto3를 사용하면 AWS의 다양한 서비스에 대한 클라이언트를 생성하고, 리소스를 관리하며, API 호출을 수행할 수 있습니다.
- 이제 사진을 올리는 class를 작성합니다

- 




