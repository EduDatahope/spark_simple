import json 
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import json

with open('data_ibm.json', 'r') as f:
    config = json.load(f)

print(config)

with open('sch_ibm.json') as f:
    schema = json.load(f)

print('------ star validation ------')

validate(instance=config,schema=schema)

print('------ succes ------')

##---

print('\n')

with open('data_ibm2.json', 'r') as f:
    config = json.load(f)

print(config)

with open('sch_ibm.json') as f:
    schema = json.load(f)

print('------ star validation ------')

validate(instance=config,schema=schema)

print('------ succes ------')