import json

with open('data/nyc_2001_campaign_finance.json') as f:
    data = json.load(f)
    print(type(data))

print(data.keys())# checking the dictinaries keys
# the keys are two : meta and data

#print the keys in the first key 

#print(data['meta'].values)

for v in data['meta'].values():
   # print(v)
    print(type(v))

#for keys inside the nested dictionary
print(data['meta'].keys())

#for the typeof value with that key 
print('the data type is a ', type(data['meta']['view']))

#what are the keys in that twice nested dictionary? 

print('The keys of this dict views that is inside a dict meta that is inside data',
      data['meta']['view'].keys())

# all these can be done by importing pandas, though the first one was pretty easy for me / understandable

print(len(data['data']))

print('The values in data are', data['data'][0])

print(data['meta']['view']['description'])

