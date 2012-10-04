import json
from pprint import pprint
json_data=open('user_tag_activity.json')

data = json.load(json_data)
print(data)
json_data.close()
