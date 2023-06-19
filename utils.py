from passlib.hash import pbkdf2_sha256

from config import Config      
# pbkdf2_sha256 = 암호화방식

# 1. 원문 비밀번호를, 단방향으로 암호화 하는 함수.

def hash_password(original_password) :
    password = pbkdf2_sha256.hash(original_password + Config.SALT)  #암호화 문자열을 붙여서 다른 사람이 알 수 없게힌다 중요한정보니 config에 저장
    return password