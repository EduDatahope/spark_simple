from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["name"],
}

validate(instance={"name": "John", "age": 30}, schema=schema) 

validate(instance={"name": "John", "age": "30"}, schema=schema)

validate(instance={"name": "John"}, schema=schema)