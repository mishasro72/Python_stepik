from random import *

def generate_password(chars, len_pass):
    return(sample(chars, len_pass))

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"
simb_out = "il1Lo0O"
chars= ""

count_pass = int(input("Укажаите количество паролей для генерации: "))
len_pass = int(input("Укажите длину пароля: "))
digit_on = input("Включать ли цифры 0123456789 (y - да/ n - нет)")
alpha_up_on = input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ (y - да/ n - нет)")
alpha_low_on = input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz (y - да /n - нет)")
simb_on = input("Включать ли символы !#$%&*+-=?@^_ (y - да/ n - нет)")
simb_off = input("Исключать ли неоднозначные символы il1Lo0O (y - да/ n - нет)")

if digit_on == "y":
    chars += digits
if alpha_up_on == "y":
    chars += uppercase_letters
if alpha_low_on == "y":
    chars += lowercase_letters
if simb_on == "y":
    chars += punctuation
if simb_off == "y":
    for i in simb_out:
        chars.replace(i, '')
#print(chars)
print(f"Сгенерированы следующие {count_pass} паролей:")
for i in range(count_pass):
    print(* generate_password(chars, len_pass), sep = "")
        
    



