# def decor_func(func):
#     def wrapped(*args):
#         print('Wrapped function!')
#         print(f'Calling function: {func.__name__}')
#         print(f'With arguments: {args}')
#         print(func(*args))
#     return wrapped

# @decor_func
# def hello(item):
#     return f'{item} was wrapped 2!'

# hello('Candy')

def div_zero(func):
    def div(x, y):
        if y == 0:
            print('На ноль делить нельзя')
            return
        else:
            return(func(x, y))
    return div

@div_zero
def delenie(x, y):
    print(x/y)

delenie(5, 2)
# list_1 = ['fd', 5, 'banan', 10, 'Alice', 15]

# new_l = list(filter(lambda x: isinstance(x, int), list_1))
# a_list = list(filter(lambda x: 'a' in x.lower(), 
#                      list(filter(lambda x: isinstance(x, str), list_1 ))))

# print(sum(new_l))
# print(a_list)


