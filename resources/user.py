from flask_restful import Resource
from flask import request
from mysql_connection import get_connection
from mysql.connector import Error
import mysql.connector
from email_validator import validate_email, EmailNotValidError     

# EmailNotValidError 이메일이 정상이냐


# 클래스는 변수와 함수의 묶음

class UserRegisterResource(Resource):
    def post(self) :
        # {"username" : "홍길동",
        # "email" : "abc@naver.com",
        # "password" : "1234"}
        
        # 1. 클라이언트가 보낸 데이터를 받아준다.

        data = request.get_json()

        # 2. 이메일 주소형식이 올바른지 확인한다.
        try :
            validate_email(data['email'])
        
        


        except EmailNotValidError as e :
            print(e)
            return {'result' : 'fail', 'error' : str(e)} , 400
        
        # 3. 비밀번호 길이가 유효한지 체크
        #    만약, 비번이 4자리 이상 , 12자리 이하라고 한다면,
        if len(data['password']) < 4 or len(data['password']) > 12 :
            return {'result' : 'fail' , 'error' : '비번 길이 에러'}, 400
        
        # 4. 비밀번호를 암호화 한다.
        
        



        return
