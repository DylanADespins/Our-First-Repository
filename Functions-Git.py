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

# 4.14.5: Default Parameters Values
# Dylan Despins
# 2/19/18

def print_two_numbers(x,y=20):

    print('First number: ',x)
    print('Second number: ',y)

print_two_numbers(5)
print_two_numbers(23,28)

# 4.14.7: Print Multiple Times
# Dylan Despins
# 2/19/19

def print_multiple_times(string,times):
    for i in range(times):
        print(string)

print_multiple_times('\n''yeah',10)

# 4.14.7: Print Multiple Times
# Dylan Despins
# 2/19/19

def print_multiple_times(string,times):
    for i in range(times):
        print(string)

print_multiple_times('\n''yeah',10)

def print_multiple_times(string,times):
    for i in range(times):
        print(string)

print_multiple_times('\n''yeah',10)

# 4.16.3: Enter a Number
# Dylan Despins
# 2/20/19
try:
    my_num = int(input('Enter an integer: '))
    print('Your number is: ' + str(my_num))

except ValueError:
    print('That was not an integer')

# 4.16.6: Temperature Converter
# Dylan Despins
# 2/20/19
def celcius_to_fahrenheit(celcius):
    return (celcius *1.8 + 32)

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) / 1.8

try:
    c = float(input('Enter a temp in Celcius:'))
    print('In fahrenheit:', round(celcius_to_fahrenheit(c), 2))

    f = float(input('Enter a temp in Fahrenheit: '))
    print('In Celcius:', round(fahrenheit_to_celcius(f), 2))


except ValueError:
    print('You must enter float')