from fastapi import FastAPI, Path, HTTPException, Query
from pydantic import BaseModel, Field , computed_field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse
import json

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001','P002'])]
    name: Annotated[str, Field(..., description='Name of the patient', examples=['Ajay','Vinay'])]
    city: Annotated[str, Field(..., description='City name of the paitent is living')]
    age: Annotated[int, Field(gt=0, lt=130, description='age of the patient',)]
    gender: Annotated[Literal['male','female','others'], Field(...,description='gender of the patient')]
    height: Annotated[float, Field(...,gt=0,  description='Patient height in meters',)]
    weight: Annotated[float, Field(...,gt=0,  description='Patient weight in Kgs',)]

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdicr(self)->str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Obsese'
        else:
            return 'Overweight'

def load_date():
    with open('patients.json','r') as f:
        data = json.load(f)
    
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)

@app.post('/create')
def create_paitent(patient: Patient):
    data = load_date()
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient ID is already exists')
    
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)

    return JSONResponse(status_code=201, content={'message':'Patient data created successfully'})

