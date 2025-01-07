from random import *
#from math import *

def is_valid(str):
    if str.isdigit() and 0 < int(str) <= n:
        return True
    return False

retry = "y"
while retry == "y":   
    print("Добро пожаловать в числовую угадайку")
    n = int(input("Укажите максимальное число, которое может быть загадано: "))
    num = randint(1, n)
#print(num)
    count = 0
    answer = input(f"Угадайте число от 1 до {n}. Введите ваш ответ: ")
    while True:
        if is_valid(answer):
            answer = int(answer)
            if answer == num:
                print(f"Вы угадали, загаданное число {num}. Число ваших попыток {count}")
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                break
            elif answer > num :
                print("Слишком много, попробуйте еще раз")
                answer = input("Введите ваш ответ:")
                count += 1
            elif answer < num:
                print("Слишком мало, попробуйте еще раз")
                answer = input("Введите ваш ответ:")
                count += 1
        else:
            print(f'А может быть все-таки введем целое число от 1 до {n}?')
            answer = input("Введите корректное число: ")
            continue
    print("Сыграем еще раз? (y - да, n - no)")
    retry = input()
    
    
#print(int(log2(100)))


        
