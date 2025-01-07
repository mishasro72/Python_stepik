lst = [2, 5, 7, 6, 5, 7, 9, 11, 2, 3, 5, 6, 9, 10]

def get_lst(lst):
    new_lst= []
    full_list = []
    for i in range(0, len(lst)):
        new_lst = [lst[i]]
        for j in range(i+1, len(lst)):
            if lst[j] > new_lst[-1]:
                new_lst.append(lst[j])
            else: 
                break
        full_list.append(new_lst)
    return full_list

def get_index(lst, max_lst):
    length = len(max_lst)
    index_start = lst.index(max_lst[0])
    flag = 1
    while flag > 0:
        if lst[index_start:index_start+length+1] == max_lst:
            flag = 0
            index_end = lst.index(max_lst[-1])
        else:
            lst = lst[index_start+1:]
            index_start = lst.index(max_lst[0])
    return index_start, index_end

max_lst = max(get_lst(lst), key=len)


print(get_index(lst, max_lst))
print(max_lst)
