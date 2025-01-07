
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cesar = [x for x in input("Введите текст, который нужно зашифровать: ").split(' ')]
cesar_word = []
for i in cesar:
    count = 0
    str = i
    for y in str:
        if y.isalpha():
            count += 1
    for a in str:
        if a.isalpha():
            if a.isupper():
                cesar_word.append(eng_upper_alphabet[(eng_upper_alphabet.find(a) + count) % 26])
            elif a.islower():
                cesar_word.append(eng_lower_alphabet[(eng_lower_alphabet.find(a) + count) % 26])
        else:
            cesar_word.append(a)
    cesar_word.append("_")

print(* cesar_word[:-1], sep = "")
    


    
    
