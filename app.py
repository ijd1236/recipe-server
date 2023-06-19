from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource

app = Flask(__name__)

api = Api(app) # Flask 객체에 Api 객체 등록

# 경로와 API 동작코드(Resourece)를 연결한다.
api.add_resource( RecipeListResource , '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource( UserRegisterResource , '/ruser/register')

if __name__ == '__main__':
    app.run()





