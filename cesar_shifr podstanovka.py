
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

flag = "y"

while flag == "y":
    forward = input("Выберете направление: s - шифрование или d - дешифрование: ")
    while forward != "s" and forward != "d":
        forward = input("Укажи верное направление: s - шифрование или d - дешифрование: ")    
    
    lang = input("Выберете язык алфавита: ru - русский или en - английский: ")
    while lang != "ru" and lang != "en":
        lang = input("Укажи правильный язык алфавита: ru - русский или en - английский: ")
    if lang == "ru":
        len = 32
    elif lang == "en":
        len = 26
    
    #step = input("Укажите шаг сдвига (со сдвигом вправо): ")
    #while step.isdigit() != True:
     #   step = input(f"Укажите шаг сдвига (со сдвигом вправо), числом от 1 до {len}: ")
    #step = int(step)

    str = input("Введите фразу для шифрования/дешифрования: ")

    for step in range (len):
        cesar = []
        if forward == "s":
            if lang == "ru":
                for i in str:
                    if i.isalpha():
                        if i.isupper():
                            cesar.append(rus_upper_alphabet[(rus_upper_alphabet.find(i) + step) % 32])
                        elif i.islower():
                            cesar.append(rus_lower_alphabet[(rus_lower_alphabet.find(i) + step) % 32])
                    else:
                        cesar.append(i)
            elif lang == "en":
                for i in str:
                    if i.isalpha():
                        if i.isupper():
                            cesar.append(eng_upper_alphabet[(eng_upper_alphabet.find(i) + step) % 26])
                        elif i.islower():
                            cesar.append(eng_lower_alphabet[(eng_lower_alphabet.find(i) + step) % 26])
                    else:
                        cesar.append(i)
        elif forward == "d":
            if lang == "ru":
                for i in str:
                    if i.isalpha():
                        if i.isupper():
                            cesar.append(rus_upper_alphabet[(rus_upper_alphabet.find(i) - step) % 32])
                        elif i.islower():
                            cesar.append(rus_lower_alphabet[(rus_lower_alphabet.find(i) - step) % 32])
                    else:
                        cesar.append(i)
            elif lang == "en":
                for i in str:
                    if i.isalpha():
                        if i.isupper():
                            cesar.append(eng_upper_alphabet[(eng_upper_alphabet.find(i) - step) % 26])
                        elif i.islower():
                            cesar.append(eng_lower_alphabet[(eng_lower_alphabet.find(i) - step) % 26])
                    else:
                        cesar.append(i)
        print(* cesar, sep = "")
    flag = input("Попробуем еще что-то расшифровать/зашифровать? (y - да/ n - нет)")


