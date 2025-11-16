# Question 1

def combine_values(*numbers): 
    if not numbers: 
        return 1
    product = 1
    for number in numbers: 
        product *= number
    return product

print(combine_values(2, 3, 4))
print(combine_values(5))
print(combine_values())

# Question 2

def merge_details(label, **details): 
    dictionary = {"label": label}
    dictionary.update(details)
    return dictionary 

print(merge_details("ItemA", size="Large", cost=12.50))
print(merge_details("UserX"))

# Question 3
"""
1. 8
2. 10
3. 0
"""

# Question 4
"""
1. {"name": "Alpha", "x": 1, "y": 2, "count": 2} 
2. {"name": "Beta", "count": 0}
"""