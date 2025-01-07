my_dictionary = {"apple" : 1, "banana" : 2}
my_dictionary_2 = {"banana" : 2}
my_lst = [("kiwi", 7), ("cherry", 8)]
my_string = "banana"
my_lst_1 = [1, 4, 6, 0, 5, 9]

def add_item(dictionary, key, value):
    dictionary[key] = value

def del_item(dictionary, key):
    del dictionary[key]

def get_item(dictionary, key):
    return dictionary.get(key)

def change_value(dictionary, key, value):
    dictionary[key] = value

def check_the_key(my_dictionary, key):
    return key in my_dictionary

def combine_dictionary(dictionary_1, dictionary_2):
    dictionary_1.update(dictionary_2)

def get_keys(dictionary):
    return list(dictionary.keys())
    
def get_values(dictionary):
    return list(dictionary.values())

def get_pairs(dictionary):
    return list(dictionary.items())

def clear_dictionaryionary(dictionary):
    dictionary.clear()

def make_copy(dictionary):
    return dictionary.copy()

def cut_item(dictionary, key):
    return dictionary.pop(key)

def make_squares_dictionary(x):
    return {i : i ** 2 for i in range (1, (x + 1))}

def get_len(dictionary):
    return len(dictionary)

def get_non_exist_value(dictionary, key):
   return  dictionary.get(key, "нет")

def make_dictionary(lst):
    return dict(lst)

def count_uniq_char(string):
    return {char : string.count(char) for char in set(string)}

def change_values_to_0(dictionary):
    for key in dictionary:
        dictionary[key] = 0
    return dictionary

def get_all_key_and_values_greater_2(dictionary):
    return [key for key, value in dictionary.items() if value > 2]

def get_max_value(dictionary):
    return max(dictionary, key=dictionary.get)

def get_min_value(dictionary):
    return min(dictionary, key=dictionary.get)


add_item(my_dictionary, 'orange', 3)
del_item(my_dictionary, 'banana')
print(get_item(my_dictionary, 'orange'))
change_value(my_dictionary, 'orange', 5)
print(check_the_key(my_dictionary, 'apple'))
print(check_the_key(my_dictionary, 'banana'))
combine_dictionary(my_dictionary, my_dictionary_2)
print(get_keys(my_dictionary))
print(get_values(my_dictionary))
print(get_pairs(my_dictionary))
#clear_dictionaryionary(my_dictionary)
new_dictionary = make_copy(my_dictionary)
print(cut_item(new_dictionary, 'orange'))
print(make_squares_dictionary(5))
print(len(my_dictionary))
print(get_non_exist_value(my_dictionary, 'kiwi'))
print(make_dictionary(my_lst))
print(count_uniq_char(my_string))
change_values_to_0(new_dictionary)
print(get_all_key_and_values_greater_2(my_dictionary))

print(max(my_lst_1))
print(my_dictionary)
print(new_dictionary)
print(get_max_value(my_dictionary))
print(get_min_value(my_dictionary))
