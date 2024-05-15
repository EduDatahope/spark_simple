import json 
from jsonschema import validate
from jsonschema.exceptions import ValidationError

import json

with open('data_order_detail.json', 'r') as f:
    config = json.load(f)

print( json.dumps(config, indent=2) )

with open('sch_order_detail.json') as f:
    schema = json.load(f)

print('------ star validation ------')

validate(instance=config,schema=schema)

print('------ succes ------')