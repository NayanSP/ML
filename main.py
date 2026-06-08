from fastapi import FastAPI

api = FastAPI()
 
@api.get('/')
def hello():
    return {'message':'Hello WOrld!'}

@api.get('/about')
def about():
    return {'messgae':'My first code in FastAPI'}