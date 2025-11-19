def search_data(query): 
    if query == "":
        return None
    if query == "empty": 
        return 0
    if query == "error": 
        return False
    return len(query)

# 1 return Type - None --> "No Value"
# Meaning: Absence of value, not set, not found
# Use for: Missing data, search failures, optional parameters 
result = None
print(result is None)  # True - identity check 
print(result == None)  # True - equality check 

# 2 return Type - False = Boolean False
# Meaning: Eplicit false condition, validation failures, negative result 
# Use for: Validation result, boolean operations, success/failure status 

result = False
print(result is False) # True - identity check 
print(not result)      # True - boolean negation 
print(result == 0)     # True - falsy check 


# 3 return Zero - A Valid Number
# Zero is VALID numeric value, not absence of value! 
result = 0
print(result == 0)     # True - numeric equality 
print(not result)      # True - (falsy in boolean context)
print(result is None)  # False - different object 
print(result is False) # False - different types 

# Multiple Returns - python packs multiple returns into a tuple 
def calculate_room(length, width): 
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
result = calculate_room(10, 5)
print(result)
print(type(result))

print(type(42)) # int
print(type(42, )) # tuple for single item
no_parenthesis = 1, 2, 3
print(type(no_parenthesis))

# unpacking
area_result, perimeter_result = calculate_room(20, 6)
print(f"Area: {area_result}")
print(f"Perimeter: {perimeter_result}") 
def process_data():
    return "hello", 42, [1, 2, 3]
a, b, c = process_data()

def grade_statistics(grades): 
    average = 0
    highest = 0
    lowest = 100
    if not grades: 
        return 0, 0, 0, False
    for grade in grades: 
        average +=grade
        if grade > highest:
            highest = grade
        elif grade < lowest: 
            lowest = grade
    final_average = average/(len(grades))
    if final_average > 50:
        passed = True
    return final_average, highest, lowest, passed 

print(grade_statistics([85, 92, 78, 90]))
print(grade_statistics([]))
print(grade_statistics([80, 80, 80]))