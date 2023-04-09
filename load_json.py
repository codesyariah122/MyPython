import json

with open('./db.json') as json_file:
    file_contents = json_file.read()
parsed_json = json.loads(file_contents)

print(parsed_json)

print(file_contents.strip())
