from pydantic import BaseModel

class Patient(BaseModel):
    name: str
    age: int

def insert_patient_data(patient):

    print(patient.name)
    print(patient.age)
    print('data inserted')

def updated_patient_data(patient):
    print(patient.name)
    print(patient.age)
    print('data updated')


patient_info = {'name':'Ravi','age':30}
patient_info1 = {'name':'Manoj','age':33}

patient1 = Patient(**patient_info)
patient2 = Patient(**patient_info1)

insert_patient_data(patient1)
updated_patient_data(patient1)
insert_patient_data(patient2)
updated_patient_data(patient2)




