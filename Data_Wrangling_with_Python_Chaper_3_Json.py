import json

file_path = '/Users/Pippen/downloads/python/data-wrangling/data/chp3'
file_name = 'data-text.json'
file_full_path = file_path + '/' + file_name
json_data = open(file_path + '/' + file_name).read()
data = json.loads(json_data)

for row in data:
    print row

print type(open(file_full_path, 'rb'))  # expects a file
print type(open(file_full_path).read())  # expects a string