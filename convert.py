import itertools
import json

with open('food.yml', 'r') as f:
   lines = f.readlines()
patterns, responses = lines[::2], lines[1::2]
patterns=map(str.strip, patterns)
responses=map(str.strip, responses)
tag= 'food'
record={}
record['tag']=tag
record['patterns']=patterns
record['responses']= responses
json_data = json.dumps(record)
with open('formatted.json', 'w') as f_out:
        f_out.write(json_data)
