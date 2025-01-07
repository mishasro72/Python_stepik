timur = input('Что выбирает игрок Тимур: камень, ножницы, бумага, ящерица или спок? ')
ruslan = input('Что выбиравет игрок Руножницыслан: камень, ножницы, бумага, ящерица или спок? ')

if timur == "ножницы":
    if ruslan == "бумага" or ruslan == "ящерица":
        print("Тимур")
    elif ruslan == "ножницы":
        print("ничья")
    else:
        print("Руслан")
elif timur == "бумага":
    if ruslan == "ножницы" or ruslan == "ящерица":
        print("Руслан")
    elif ruslan == "бумага":
        print("ничья")
    else:
        print("Тимур")
elif timur == "камень":
    if ruslan == "ножницы" or ruslan == "ящерица":
        print("Тимур")
    elif ruslan == "камень":
        print("ничья")
    else:
        print("Руслан")
elif timur == "ящерица":
    if ruslan == "бумага" or ruslan == "Спок":
        print("Тимур")
    elif ruslan == "ящерица":
        print("ничья")
    else:
        print("Руслан")
else:
    if ruslan == "камень" or ruslan == "ножницы":
        print("Тимур")
    elif ruslan == "Спок":
        print("ничья")
    else:
        print("Руслан")
