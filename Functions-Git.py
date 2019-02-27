# 4.13.3: Greeting
# Dylan Despins
# 2.6.19

name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()

# 4.13.4: Functions and Variables
# Dylan Despins
# 2.14.19


x = 43

def print_something():
    x = 8
    print(x)

print_something()
print(x)


# 4.13.5: Functions and Variables - Part 2
# Dylan Despins
# 2.14.19

my_variable = 3.1465

def something():
    print(my_variable + 10)

something()

# 4.13.6: Functions and Variables, Part Three
# Dylan Despins
# 2/18/19

def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + 'Hello World')

# 4.14.4: Name and Age
# Dylan Despins
# 2/18/19

def name_and_age(name, age):
    print('\n' 'Hi, my name is ', name, 'and I am ',str(age), ' years old. ')

name_and_age('Dylan' , 15)
