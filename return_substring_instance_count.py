#решение без доп библиотек
def solution(full_text, search_text):
    if search_text == "":
        return len(full_text) + 1
    count = 0
    while full_text.find(search_text) != -1:
        index = full_text.find(search_text)
        index_1 = index + len(search_text)
        count += 1
        full_text = full_text[index_1:]
    return count

#решение с бибилотекой re
import re 

def solution_1(full_text, search_text):
    return len(re.findall(search_text, full_text))

full_text = "aaa"
search_text = "aa"

assert solution(full_text, search_text) == 1
print(solution(full_text, search_text))
print(solution_1(full_text, search_text))
