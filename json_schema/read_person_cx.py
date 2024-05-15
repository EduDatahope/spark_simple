import json 
from jsonschema import validate
from jsonschema.exceptions import ValidationError


with open('data_person_cx.json', 'r') as f:
    config = json.load(f)

print(config)

print('\n')
print('------ star validation ------')

with open('sch_person_cx.json') as f:
    schema = json.load(f)

print('------ succes ------')    




    
