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
