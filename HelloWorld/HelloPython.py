import random
import sys
import os

# More like an array in C Sharp
new_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

# Like a list, but cannot change
new_tuple = (1, 2, 3)

# Pretty much like a dictionary
new_dictionary = {'Fiddler' : 'Isaac Bowin', 'Captain Cole' : 'Leonard Snart'}

print("\n..............Lists, Tuples and Dictionaries..............")
print(new_list[1])
print(new_tuple)
print(new_dictionary['Captain Cole'])

print("\n..............Conditionals..............")
age = 21
if age >= 21:
    print("You are old enough to drive a tractor trailer")
elif age >= 16:
    print("You are old enough to drive a car")
else:
    print("You are not old enough to drive")

if (age >= 1) and (age <= 18):
    print("You get a birthday")
elif (age == 21) or (age >= 65):
    print("You get a birthday")
# Not is like != in C Sharp
elif not(age == 30):
    print("You don't get a party")
else:
    print("You get a birthday party, yay!")

print("\n..............For Loops..............")
for x in range(0, 10):
    print(x, ' ', end="")

print('\n')

for y in new_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

print("\n..............While Loops..............")

random_num = random.randrange(0, 100)

while(random_num != 15):
    print(random_num)
    random_num = random.randrange(0, 100)

print('\n')

i = 0

while(i <= 20):
    if(1%2 == 0):
        print(i)
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1

print("\n..............Functions..............")

def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1, 4))

# Ctrl + Shift + / to uncomment

# print("What is your name")
#
# name = sys.stdin.readline()
#
# print("Hello", name)

print("\n..............Strings and Chars..............")

long_string = "I'll catch you if you wall - The Floor"

print(long_string)

print(long_string[0:4])

print(long_string[-5:])

print(long_string[:-5])

print(long_string[:4] + " be there")

print("%c is my %s letter and my number %d number is %.5f" % ("X", "favorite", 1, .14))

print(long_string.capitalize())

print(long_string.find("Floor"))

print(long_string.isalnum())

print(long_string.isalnum())

print(len(long_string))

print(long_string.replace("Floor", "Ground"))

print(long_string.strip())

print("\n..............File.IO..............")

# Writing to a file
test_file = open("test.txt", mode="wb")

print(test_file.mode)

print(test_file.name)

test_file.write(bytes("Write me to the file\n", "UTF-8"))

test_file.close()

# Reading and Writing to a file
test_file = open("test.txt", mode="r+")

text_in_file = test_file.read()
print(text_in_file)

# os.remove("text.txt")

print("\n..............Objects..............")

class Animal:
    __name = 0
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)


cat = Animal("Whiskers", 33, 10, "Meow")

print(cat.toString())


print("\n..............Inheritance..............")

class Dog(Animal):
    __owner = ""


    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("Dog")

    # Override
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {}. His owner is {}.".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound,
                                                                     self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 27, "Ruff", "Sean")

print(spot.multiple_sounds(3))

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(Dog)