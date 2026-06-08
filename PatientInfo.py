from fastapi import FastAPI, Path, HTTPException, Query
import json

api = FastAPI()

@api.get('/')
def hello():
    return {'message':'Patient Management API'}

@api.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

def load_date():
    with open('patients.json','r') as f:
        data = json.load(f)
    
    return data

#to view whole patient data
@api.get('/view')
def view():
    data = load_date()
    return data

@api.get('/patient/{patient_id}')
def view_patient(patient_id:str = Path(..., description="ID of the Patient in DB", example='P001')):
    #load all patient
    data = load_date()

    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code=404, detail='Patient not found')

@api.get('/sort')
def sort_parameter(sort_by: str = Query(..., description='sort on basis of height, weight, or bmi'),
                   order: str = Query('asc', description='sort in asc or desc order')):
    valid_fields = ['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= "Invalid fields, select from {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=400, detail= "Invalid order, select from asc or desc")
    
    data = load_date()
    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key = lambda x:x.get(sort_by,0), reverse=sort_order)
    return sorted_data