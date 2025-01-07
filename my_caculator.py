from my_calc_func import *

funcitions = {'-': minus, '+' : plus, '/' : div, '*' : pow}
expres = [x for x in input('Введите ваше выражение: ').split(' ')]
print(funcitions[expres[1]](int(expres[0]), int(expres[2])))
#print(f'')




