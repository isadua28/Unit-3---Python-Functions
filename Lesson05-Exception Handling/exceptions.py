# 1-Common Errors
# 1 - Divison by zero
# print(10/0)

# 2-ValueError
# print(int("abc"))

# 3-KeyError
# grades = {"Bob": 90}
# print(grades["Bill"])

# 4-Index Error
# numbers = [1, 2, 3]
# print(numbers[5])

# 5-NameError
# print(total)
# total = 10

# 6-TypeError
# print("hello" + 5)

# 7-SyntaxError
# for i in range(5):
# print(i)

def safe_divide(a, b): 
    try: 
        result = a / b
        return result
    # except: 
    #     print("Can not divide by zero!")
    #     return None
    except ZeroDivisionError:
        print("Can not divide by zero!")
        return None 
    except TypeError: 
        print("That's not a valid number!")
        return None 
    except: 
        print("An error occured!")

print(safe_divide(10, 2)) # 5.0
print(safe_divide(10, 0)) # Can not divide by zero 
print(safe_divide(10, "hello"))

def safe_operations(a, b, lst, key, d): 
    try: 
        print(f"Division result: {a/b}")
        print("Access list element:", lst[2])
        print("Access Dictionary Key:", d[key])
        print(f"Add numbers: {a + b}")
    # except ZeroDivisionError: 
    #     print("Can not divide by zero!")
    # except IndexError: 
    #     print("List index out of range!")
    # except KeyError: 
    #     print(f"Key {key} not found in dictionary!")
    # except TypeError: 
    #     print("Invalid types for operation!")
    except Exception as e: 
        print("Some other error occured", e)

print(safe_operations(10, 2, [1, 2], "tom", {"John":15}))

# Question 1: Price Per Item Calculator 
def calculate_price_per_item(cost, count): 
    try:
        price = cost / count
        return round(price, 2)
    except ZeroDivisionError: 
        print("Can not divide by zero!")
    except Exception as e: 
        print("An error occured!")
        
print(calculate_price_per_item(100, 4))
print(calculate_price_per_item(50, 0))
print(calculate_price_per_item(25, 50, 3))

# Question 2: Parse Age from String

def parse_age(age_string): 
    try: 
        