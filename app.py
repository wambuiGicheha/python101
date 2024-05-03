print ("Hello World!")

a = 11
b = 1.1
c = 1j

x = float(a)
y = int(b)
z = complex(a)

print (x)
print (y)
print (z)

#variavle assignment
x = 5
y = 3
print (x)
print (x + y)

print ("I am a string")
print ('Me too!')

"hello"
print ("hello".upper())

print ("HELLO".lower())
print ("hello".capitalize())
print ("hello" + " world")
print  ("hello " * 3)

g = list()
print (g)

list_abc = ['a', 'b', 'c']
list_abc[0]

#dictionary
{"key1" : "value1", "key2":"value2", "key3":"value3"}


#introduction to variables:strings 27.03.2024
type ("Homer Simpson")


#intoductin to control flows
val3 = 4
val4 = 4

output = val3 + val4
print (output)

# initiliaze variable 
vacation_day = 0

#
vacation_day = vacation_day + 1
vacation_day = vacation_day + 1

print(vacation_day)


#holiday = 0
#holiday += 3
#holiday += 4
#print(holiday)

#if goals ==2
#then
#holiday += 3
#else nothing

holiday = 0
goals = False
if goals :
    holiday += 3
    print ("Your holiday days are :",  holiday )
    print ("we have incremented the days")
else:
    print ("Your holiday days are :",  holiday )
    print ("we have not incremented the days")


#number_50 = 50
#my_number = 70
#if number_50 > 100:
         # if number_50 is greater than 100, assign the `my_number` variable to the number 100
    #elif number_50 > 50:
        # if number_50 is greater than 50, assign the `my_number` variable to the number 50
    #else:
       # else assign the `my_number` variable to 0
   # my_number = 0
    
List1 = ['student1', 'student', 'student3', 'student4', 'student5']

print (List1[0])
top_student = List1[0]
print (top_student)

type(List1)
print (type(List1))

#ADDING TO A LIST USE APPEND METHOD

List1.append('New Student')
print (List1)

#append is destructive as it changed the elements in the list
#add another append 
List1.append('New Student')
print (List1)

#use the pop method to remeove the last element int the list
List1.pop()
print  (List1)

#changing an eement in a lsit
List1[4] = 'Wambui'
print (List1)

List1.append('student1')
print(List1)
 
unique_list1 = set(List1)
print (unique_list1)

print(type(unique_list1))

unique_list1 =list(unique_list1)

#DICTIONARIES
#friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons':10 }


friends = {'name': 'Friends', 'genre': 'sitcom', 'no_of_seasons': 10}
print (friends["genre"])
print (friends)

friends ['no_of_episodes'] = 236
friends ['starring'] = 'Jeniffer Aniston', 'Courtney Cox', 'Lisa Kudrow', 'Matt Leblanc', 'Matthew Perry', 'David Schwimmer'
print (friends)

#you can add any value in a dictionary
friends [14] = 'something nonsensicle'
print (friends[14])

#deleting from a dictionary
del friends[14]
print (friends)

# Add a dot (.) after 'friends' and press tab to see all of the available methods

#lists in dictionaries
starring2 = ['Jeniffer Aniston', 'Courtney Cox', 'Lisa Kudrow', 'Matt Lebranc', 'Kez G']
friends['starring2'] = ['Jeniffer Aniston', 'Courtney Cox', 'Lisa Kudrow', 'Matt Lebranc', 'Kez G']
#friends ['starring'] = 'Jeniffer Aniston', 'Courtney Cox', 'Lisa Kudrow', 'Matt Leblanc', 'Matthew Perry', 'David Schwimmer'

print (friends)

friends['creators'] = ['David Crane', 'Marta Kauffman']
print (friends)

print(friends['creators'])
print(friends['no_of_seasons'])

david = friends['creators'][0]
print (david)

#create a dictionary about seinfeld with all its attributes and what not
seinfeld = {'name' : 'Seinfeld','Genre' : 'Sitcom', 'created_by' : ['Larry David', 'Jerry Seinfeld']}
print (seinfeld)

#a list of two tv shows 
tv_shows = [friends, seinfeld]
tv_shows
print (tv_shows)

#nested dictionary
print (tv_shows[1])
print (tv_shows[1]['created_by'])
print (tv_shows[1]['created_by'][1])

#relearn how to make the lists and dictionaries and how to read them 

#for loops
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l']

for letter in alphabet:
    print (letter)

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers_count = 0
for all_numbers_we_want in numbers:
    numbers_count += 1
    print ("This is iteration:", numbers_count)
    print (all_numbers_we_want)
print("The for loop is finished now! I am not in the for loop block, which is why I only printed once!")
 

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for all_numbers_we_want in numbers:
    print (all_numbers_we_want)
#what code could we use to print out the numbers until 100?
    
countries = ['Croatia', 'USA', 'Argentina', 'France', 'Brazil', 'Japan', 'Vietnam']
print (countries)
print (type(countries))

#using list elements as indices
for where_country_is_indexed in [0,1,2,3,4,5,6]: #dont quite understand the logic behind this
    print(where_country_is_indexed)
    print (countries[where_country_is_indexed])

countries = ['Croatia', 'USA', 'Argentina', 'France', 'Brazil', 'Japan', 'Vietnam']
cities = ['Zagreb', 'District of Columbia', 'Buenos Aires', 'Paris', 'Rio de Janeiro', 'Tokyo', 'Hanoi']

for place_index in [0,1,2,3,4,5,6]: #for the new valraible called place index and uisnf the matching index place
    print(cities[place_index]+",",countries[place_index]) #take the position of the city and position of the country

#always check the length of the list 
print(len(countries))
print(len(cities))
#creating a range
range(0, len(countries))
print(range(0, len(countries)))
list((range(0, len(countries))))
print(list((range(0, len(countries)))))

for already_fig_indexed_list in list((range(0, len(countries)))):
    print(cities[already_fig_indexed_list]+",",countries[already_fig_indexed_list])

#TO GO OVER THE LABS AND REPEAT THEM 

##FOR WHILE LOOPS  WITH BREAK AND CONTINUE
    
number_to_stop = 20
while number_to_stop > 0:
    print (number_to_stop)
    number_to_stop = number_to_stop - 1 #what does this mean why is it stopping at 19
print ("The stop number reached", number_to_stop, "so the while loop's condition became False and stopped execution")




numbers30 = list(range(1, 30))
print (numbers30)
new_list = []
for num in numbers:
    if len(new_list) > 4:
        print (f'We have enough even numbers in new_list ({len(new_list)}). break will stop the for loop now')
        break
    elif num % 2 != 0:
        new_list.append(num)
    elif num % 2 != 0:
        continue
        print('i never get executed')
    print(num, 'is even.')
    print('this does not print for odd numbers\nbecause the continue statement skips\nthe code that follows in the for loop\nand goes straight back to the next element in the for loop')
    
#dir(list) checks what method that can be be used a claa
#what are classes and what are methods? 
#methods are functions that allow you to run operations on the classes
#mutating methods and non mutating   i.e you have to create a new variable mutate the original variable

name = "Keziah"
print (name)
upper_case_name = name.upper() #did not change to uppercase
print (upper_case_name)

my_list = [2, 5, 7, 7, 9, 10]
my_list.sort()
print (my_list)
print (my_list[3])

#to access a value in a list, use square brackets and the index of an element to access it 
#nested arrays - arrays with arrays inside it

#modifying an array, adding an element to an array 
my_list.append(100)
print(my_list)


#functions - code of block that you want to re use - defining reusable code
#a = 3
#b = 4

def add(a , b):#define your function - add parameters/variables
    return a + b #return output of the operation - to be semantically correct     
add(4, 7) #calling your function
print(add(4,7))

#key_list = my_dict.keys() functions on getting  all keys


z = 'YE'[-1]

print (z)

x = "Hello, World!"[-1]
print (x)
x = [19, 18, 21, 16, 15, 17, 20, 18]
print (sum(x))

printline = print("This is just a trial for git")








