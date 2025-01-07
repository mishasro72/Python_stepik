string = "747ndvbdhvb3.4fjekfje"
numbers = ""
numbers_final = []

for char in string:
    if char.isdigit() or char == ".":
        numbers += char
print(numbers)

i = 0 
if numbers[-2] == ".":
    while i < (len(numbers)-1):
        if numbers[i+1] == ".":
            numbers_final.append(float(numbers[i:i+3]))
            i += 3
        else:
            numbers_final.append(float(numbers[i]))
            i += 1 
else:
    while i < (len(numbers)-1):
        if numbers[i+1] == ".":
            numbers_final.append(float(numbers[i:i+3]))
            i += 3
        else:
            numbers_final.append(float(numbers[i]))
            i += 1 
    numbers_final.append(float(numbers[-1]))

print(sum(numbers_final))


