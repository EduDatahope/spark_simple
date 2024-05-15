import json 
from jsonschema import validate
from jsonschema.exceptions import ValidationError

inst = {  
  "name": "jhon smit",
  "age": 25,
  "isStudent": False ,
  "favoriteProgram": "python"
}

import json

with open('data_person.json', 'r') as f:
    config = json.load(f)

print(config)

with open('sch_person.json') as f:
    schema = json.load(f)


print('------ star validation ------')

validate(instance=config,schema=schema)

validate(instance=inst,schema=schema)

print('------ succes ------')

    
