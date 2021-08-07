# Python Functions

# Simple function program
def print_my_name(my_name):
    print("My name is", my_name)
    return

name = "Shoriful Islam Emon"
print_my_name(name)

# Simple Calculator
def add(a, b, c):
    result = a + b + c
    return result

output = add(25, 20, 30)
print(output)

# Simple Calculator with input
def add(a, b, c):
    result = a + b + c
    print(a,'+',b,'+',c,'=', output)
    return result

output = add(int(input("Enter 1st number : ")),
         int(input("Enter 2nd number : ")),
         int(input("Enter 3rd number : ")))


# Function Arguments

# 1. Required Arguments
def add(a, b, c):
    result = a + b + c
    return result

#output = add(10, 20) # This will not work
output = add(15, 25, 35) # This will work
print(output)

# 2. Keyword Arguments
def add(a, b, c):
    result = a + b + c
    return result

output = add(b=17, c=20, a=25) # We can choose any parameters value
print(output)

# 3. Default Arguments
def add(a, b, c=0):
    result = a + b + c
    return result

output = add(25, 60)
print(output)

# 4. Variable-length Arguments
'''
Types:
(i) Keyword variable-length argument
(ii) Non-keyword variable-length argument
'''
# (i) Keyword variable-length argument
def add(**number_list):
    print(type(number_list))
    result = 0
    for key in number_list:
        result = result + number_list[key]
    return result

output = add(a=1, b=2, c=3, d=4, e=5)
print(output)

# (ii) Non-keyword variable argument
def add(*number_list):
    print(type(number_list))
    result = 0
    for number in number_list:
        result =result + number
    return result

output = add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(output)