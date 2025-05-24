#JSON is commonly used with  data APIs.here is an example of how to use JSON in Python:
import json
# Sample JSON data
data = '''
{
    "name": "John",
    "age": 30,
    "city": "New York"
}
'''
# Parse JSON data
parsed_data = json.loads(data)
# Accessing data
print(data)


car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car_json = json.dumps(car, indent=4)
# Print JSON data
print(car_json)