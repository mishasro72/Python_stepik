# numbers = {'zero': 0, 'one' : 1, 'two': 2, 'three' : 3,  'four' : 4, 'five' : 5, 
#            'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

# def number(name_of_number):
#     return (numbers[name_of_number])

# def operation(a, b, operator):
#     if operator == 'plus':
#         return(a+b)
#     elif operator == 'minus':
#         return(a-b)
#     elif operator == 'times':
#         return (a * b)
#     elif operator == 'divided_by':
#         return (a // b)
    
# culculator = input()
# string = culculator.split('(')

# print(operation(number(string[0]), number(string[2]), string[1]))

def zero(f=None): return 0 if not f else f(0) 
def one(f=None): return 1 if not f else f(1) #your code here
def two(f=None): return 2 if not f else f(2)  #your code here
def three(f=None): return 3 if not f else f(3) #your code here
def four(f=None): return 4 if not f else f(4) #your code here
def five(f=None): return 5 if not f else f(5)#your code here
def six(f=None): return 6 if not f else f(6) #your code here
def seven(f=None): return 7 if not f else f(7)#your code here
def eight(f=None): return 8 if not f else f(8) #your code here
def nine(f=None): return 9 if not f else f(9) #your code here

def plus(b): return lambda a: a + b #your code here
def minus(b): return lambda a: a - b #your code here
def times(b): return lambda a: a * b #your code here
def divided_by(b): return lambda a: a // b #your code here


print(eight(divided_by(three())))
