from random import *

word_list_en = ['sun', 'moon', 'fun', 'gun', 'good', 'weather', 'mother', 'hart', 'table', 'plate' ]
word_list_ru = ['дорога', 'корпоратив', 'дерево', 'сила', 'алкоголь', 'праздник']

def get_word(word_list):
    return(choice(word_list))

def display_hangman(tries):
    if tries == 6:
        print("--------")
        print("|      |")
        for i in range(4):
            print("|")
        print("_")
    elif tries == 5:
        print("--------")
        print("|      |")
        print("|      0")
        for i in range(3):
            print("|")
        print("_")
    elif tries == 4:
        print("--------")
        print("|      |")
        print("|      0")
        print("|      |")
        print("|      |")
        print("|")
        print("_")
    elif tries == 3:
        print("--------")
        print("|      |")
        print("|      0")
        print("|     \\|")
        print("|      |")
        print("|")
        print("_")
    elif tries == 2:
        print("--------")
        print("|      |")
        print("|      0")
        print("|     \\|/")
        print("|      |")
        print("|")
        print("_")
    elif tries == 1:
        print("--------")
        print("|      |")
        print("|      0")
        print("|     \\|/")
        print("|      |")
        print("|     /")
        print("_")
    elif tries == 0:
        print("--------")
        print("|      |")
        print("|      0")
        print("|     \\|/")
        print("|      |")
        print("|     / \\")
        print("_")
        print("Sorry, you lose!")

def fool_check_l(letter):
    if letter.isalpha():
        return False
    else:
        return True

def fool_check_w(word):
    if word.isalpha():
        return False
    return True

def fool_check_way(way):
    if way == "l" or way == "w":
        return False
    return True

def fool_check_way_ru(way):
    if way == "с" or way == "б":
        return False
    return True

def play_en(word):
    print("Let's play The Hangman Game")
    tries = 6
    check_letters = []
    display_hangman(tries)
    word_complection = "_" * len(word)
    print(f"Secret word: {word_complection}")
    while tries != 0:
        way = input("Do you want to name the letter or whole word? (press l - for letter or w - for word): ")
        while fool_check_way(way):
            way = input("You must press noly l - for letter or w - for word: ")
        if way == "l":
            print("Letters that you already named are:", end = " ")
            print(* check_letters)
            letter = input("Enter the letter: ")
            while fool_check_l(letter):
                letter = input("You must enter the letter, not other symbol: ")
            check_letters.append(letter)
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        word_complection = word_complection[:i] + letter + word_complection[(i + 1):]
                print(f"You are right! There is {letter} in this secret word")
                print(word_complection)
            else:
                tries -= 1
                print("Sorry, you answer is wrong. There is no such letter in this word")
                display_hangman(tries)
        elif way == "w":
            word_answer = input("Enter the word: ")
            while fool_check_w(word_answer):
                word_answer = input("You must enter the word contein only letters, not other symbols: ")
            if word_answer == word:
                print(f"You are right. The secret word is {word.upper()}. Congratulations!")
                break
            else:
                tries -= 1
                print("Sorry, you answer is wrong. You didn't guess the word")
                display_hangman(tries)
        if word == word_complection:
            print(f"You are right. The secret word is {word.upper()}. Congratulations!")
            break

def play_ru(word):
    print("Давайте сыграем в игру Виселица")
    tries = 6
    check_letters = []
    display_hangman(tries)
    word_complection = "_" * len(word)
    print(f"Загаданное слово: {word_complection}")
    while tries != 0:
        way = input("Ты хочешь нзвать букву или слово целиком? (нажми б - для буквы or с - для слова): ")
        while fool_check_way_ru(way):
            way = input("Тебе нужно указать только б - для буквы/ с - для слова: ")
        if way == "б":
            print("БУквы, которые ты уже назвал:", end = " ")
            print(* check_letters)
            letter = input("Введи букву: ")
            while fool_check_l(letter):
                letter = input("Ты должен ввести букву: ")
            check_letters.append(letter)
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        word_complection = word_complection[:i] + letter + word_complection[(i + 1):]
                print(f"Ты угадал! В загадонном слове есть буква {letter}")
                print(word_complection)
            else:
                tries -= 1
                print("Извините, вы ошиблись.В загаданном слове нет такой буквы")
                display_hangman(tries)
        elif way == "с":
            word_answer = input("Введите слово: ")
            while fool_check_w(word_answer):
                word_answer = input("Вам нужно ввести слово, состоящее только из букв: ")
            if word_answer == word:
                print(f"Ты угадал. Загаданное слово {word.upper()}. ПОЗДРАВЛЯЕМ!")
                break
            else:
                tries -= 1
                print("Извините, ваш ответ не верный. Ты не угадал слово")
                display_hangman(tries)
        if word == word_complection:
            print(f"Ты угадал. Загаданное слово {word.upper()}. ПОЗДРАВЛЯЕМ!")
            break


retry = "y"
while retry == "y":
    lang = input("Choose language (en - for english/ ru - for russian): ")
    if lang == "en":
        word = get_word(word_list_en)
        print(word)
        play_en(word)
    else:
        word = get_word(word_list_ru)
        print(word)
        play_ru(word)
    retry = input("Let's play again? (y - yes/ any other letter - no): ")

                
 
        
#display_hangman(int(input("Введи количесто ошибок: ")))
