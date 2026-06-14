def insert_patient_data(name: str, age: int):
    if type(name)==str and type(age)==int:
        if age >0:
             print(name)
             print(age)
             print('Insert into DB')
    else:
        raise TypeError("Incorrect data error")

def update(name, age):
    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print('Insert into DB')
    else:
        raise TypeError("Incorrect data error")

insert_patient_data('anay',32)
insert_patient_data('anay','321a')
update('abc',23)
##Problem 1: no type validation happened here
## even after type hinting, the code will still run

#probelm 2: data validation 


