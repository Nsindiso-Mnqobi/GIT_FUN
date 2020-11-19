import json 

with open("JSON.json") as data:
    json_data = data.read()

json_dict = json.loads(json_data)

print(json_dict['People'][0]['Id'])

json_dict['People'][0]['Id'] = 5

with open("JSON.json", "w") as fh:
    json.dump(json_dict, fh, indent=4)
