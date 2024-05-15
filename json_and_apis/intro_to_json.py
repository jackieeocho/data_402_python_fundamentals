import json

car_data = {
    "name": "tesla",
    "engine": "electric"
}

print(type(car_data))

#json.dumps() --> turns python dict to a str
car_data_json_string = json.dumps(car_data)#json.dumps converts dict into str
print(type(car_data_json_string))

#json.dump()--> Converts a dict to a str AND put it in a new file, also needs two arguments in brackets 'with open( ) as jsonfile'
with open("new_json_file.json","w") as jsonfile:
    json.dump(car_data, jsonfile)
