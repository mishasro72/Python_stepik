# my_list = [1, 3, 5, 'mama', 'bem', 'Anna', 'bem']

# print(*my_list[2], sep = '\n')
# for i in my_list:
    # if isinstance(i, int):
    #     print(i)
    # if isinstance(i, str) and 'a' in i.lower():
    #     print(i)
# print(sum([x for x in my_list if isinstance(x, int)]))

# my_tupl = tuple(my_list)
# print(my_tupl)
# my_set = set(my_list)
# print(my_set)

# set_1 = {1, 3, 5, 'a', 'b', 6, 7}
# set_2 = {1, 3, 5, 'a', 'b', 6, 7, 8, 10, 'h'}

# print(set_1.intersection(set_2))
# print(set_1.symmetric_difference(set_2))
# print(set_1.issubset(set_2))

# from functools import reduce as r

# my_list = [1, 5, -3, 6, -10]

# my_list_1 = list(filter(lambda x: x >= 0, my_list))
# power_list = r((lambda x,y: x * y), my_list) 
# print(my_list_1)
# print(power_list)

from time import *

# def decor_func(func):

#     def time_len(a):
#         start = perf_counter()
#         func(a)
#         end = perf_counter()
#         print (end - start)
#     return time_len

# @decor_func
# def hello(a):
#     #sleep(3)
#     print(a)

# #hello = decor_func(hello)
# hello('Hellooooooo')

def decor_func(func):

    def time_len():
        start = perf_counter()
        func()
        end = perf_counter()
        print (end - start)
    return time_len

# @decor_func
# def hello():
#     sleep(10)
#     print('Helllooooooo')

# #hello = decor_func(hello)
# hello()
from functools import *
@decor_func
def power_power():
    list_1 = [2, 2, 3, 5, 8, 13]
    print(reduce(lambda x, y: x ** y, list_1))

power_power()

