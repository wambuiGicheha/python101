import json 
with open('data/ny_times_response.json', 'r') as f: #built in open function to load the json file into a python object
    data=json.load(f)
print("this python object is a ", type(data))

print('The keys of the data dict are', data.keys()) #the output is ['status', 'copyright', 'response']
print('The values of the data dict are', data.values())

#print(data['response'])

print(type(data['response']['docs']))

docs = data['response']['docs']

print(type(docs))# replace this comment with the code to print the data type of `docs` 
print(len(docs))# replace this comment with the code to print the length
print(type(docs[0]))# replace this comment with the code to print the data type of the first element
#[{headline:' {'main': 'Front Page 7 -- No Title', 'kicker': '1', 'content_kicker': None, 'print_headline': None, 'name': None, 'seo': None, 'sub': None},'}
#{}{}{}{}{}{}{}{}]

print('the last element in docs is', docs[-1].keys() , 'and the keys in that dict are those.')
print('the last element in docs is', docs[-1].values() , 'and the values in that dict are those.')

for doc in docs:
    print(doc['headline']['main'])


