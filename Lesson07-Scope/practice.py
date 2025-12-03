# Question 15

# Error: No condition for when there is an empty list

def calculate_average(numbers): 
    if not numbers: 
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average 

grades = []
result= calculate_average(grades)
print(f"Average: {result}")

# Question 16

# C

# Question 17

# strip, upper, split, len

# Question 18

def validate_password(password): 
    if len(password) < 8: 
        return False, "Too short"
    elif not password: 
        return False, "Empty password"
    else: 
        return True, "Valid"
    
# Question 19

def create_inventory(item_name, *quantities, location="Warehouse"): 
    total = sum(quantities)
    return {
        "name": item_name,
        "total": total,
        "location": location
        }
print(create_inventory("Widget", 10, 20, 15))

# Question 20

def safe_list_access(items, index):
    try:
        if items[index]: 
            return items[index], True
    except IndexError: 
        return None, False
    
print(safe_list_access([10, 20, 30], 1))
print(safe_list_access([10, 20, 30], 10))