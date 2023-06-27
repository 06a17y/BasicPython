"""
W3schools python tutorials practice
Function
"""
# Arguments
def practice(name):
    print(name + 'OK')

practice('John')
practice('Mary')

# Arbitrary Arguments, *args
# If you don't know how many arguments that will be passed into your function, add* before the parameter name
def func(*name):
    print("My name is " + name[2])
func('Amy','Lulu',' Sherry')

# Arbitrary Keyword Arguments, **kwargs
# do not know how many keyword arguments that will be passed into your function
def func1(**name):
    print("My name is " + name['mname'])
func1(fname ='Amy', mname = 'Lulu', lname = ' Sherry')

# Default Parameter Value
def func2(country = 'Taiwan'):
    print('I am from ' + country)
func2('Japan')
func2()
func2('America')

# return values
def func3(x):
    return x * 3
print(func3(5))

# Recursion
def func4(x):
    if x > 0:
        result = x + func4(x - 1)
        print(result)
    else:
        result = 0
    return result
func4(6)

# Lambda
# lambda arguments : expression
x = lambda x : x + 10
print(x(5))

x = lambda a,b : a * b
print(x(3,4))

def func5(n):
    return lambda a : a * n
double = func5(2)
print(double(12))