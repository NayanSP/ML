from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

print('Data Validation')

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=30, title='Name of the Paitent', description= 'Provide the name in 30 character', examples=['Nitin','Ajay'])]
    age: int= Field(gt=0, lt=150)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None, description='Provide the patient is married or not')] # the optinal field should be provided with the value
    #linkedin_url: AnyUrl
    allergy: Annotated[Optional[List[str]],Field(default=None,max_length=5) ]# the allergy will be list, but the value will be string this also should be validated
    
    contact: Dict[str, str] = Field(max_length=2) #the contact will be dict and key-value in dict is also string

def insert_patient_data(patient):

    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.contact)
    print(patient.allergy)
    print('data inserted')

def updated_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.contact)
    print(patient.allergy)
    print('data updated')


patient_info = {'name':'Ravi','age':30, 'weight': 77.43, 'married':True, 'allergy':['pollen','dust'],'contact':{'mobile':'91989877882','email':'cbcb@asd.com'}}
patient_info1 = {'name':'Manoj','age':30, 'weight': 90.43, 'married':False, 'allergy':['dust'],'contact':{'mobile':'91989877882','email':'abc@yhn.com'}}
patient_info2 = {'name':'Ajay','age':43, 'weight': 80.43,  'allergy':['dust'],'contact':{'mobile':'91989877882','email':'abc@yhn.com'}}

patient1 = Patient(**patient_info)
patient2 = Patient(**patient_info1)
patient3 = Patient(**patient_info2)

insert_patient_data(patient1)
updated_patient_data(patient1)
print("================================================")
insert_patient_data(patient2)
updated_patient_data(patient2)
print("================================================")
insert_patient_data(patient3)
updated_patient_data(patient3)




