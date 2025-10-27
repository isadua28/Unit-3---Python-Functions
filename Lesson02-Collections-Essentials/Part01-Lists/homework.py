#1 
def remove_duplicates(items):
    new_list = []
    for item in items: 
        if item not in new_list:
            new_list.append(item)
    return new_list

print(remove_duplicates([1, 2, 2, 3, 1, 4]))
print(remove_duplicates(["a", "b", "a", "c"]))
print(remove_duplicates([5, 5, 5]))


#2 
def find_common(list1, list2):
    common_list = []
    for item in list1:
        for item2 in list2:
            if item == item2:
                common_list.append(item)
    return common_list

print(find_common([1, 2, 3], [2, 3, 4]))
print(find_common(["a", "b"], ["c", "c"]))
print(find_common([1, 1, 2], [2, 2, 3]))


#3 
def reverse_sublists(data, size):
    new_list = []
    for i in range(0, len(data), size):
        segment = data[i:i + size]
        segment.reverse()
        new_list.extend(segment)  
    return new_list      

print(reverse_sublists([1, 2, 3, 4, 5, 6], 2))
print(reverse_sublists([1, 2, 3, 4, 5], 3))
print(reverse_sublists([1, 2, 3, 4], 1))
print(reverse_sublists([1, 2, 3], 5))


#4

def rotate_list(items, positions):
    if not items: 
        return []
    
    positions = positions % len(items)
    return items[-positions:] + items[:-positions]

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], -2))
print(rotate_list([1, 2, 3], 0))
print(rotate_list([1, 2, 3], 5))