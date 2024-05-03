import csv
#opening the olympic file with csv reader
with open("results.csv", encoding='utf-8') as f:
    reader = csv.reader(f) #READER OBJECT 
    for _ in range(6):
        print(next(reader))


#TO READ DATA AS A LIST OF DICTIONARIES RATHER THAN A LIST OF LISTS USE csv.DictReader

with open("results.csv", encoding='utf-8') as f:
    reader = csv.DictReader(f)
    olympics_data = list(reader)

#print the first 5 rows of data
for index in range(5):
    print(olympics_data[index])

#read with readlines and iteration

#writing 
#with open('written_text.txt' + "w") as file:
 #   file.write('hello')

 # append mode is "a" with read you do not need to specify the mode

