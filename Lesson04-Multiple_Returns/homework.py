# Question 1: User Search with Tricky Trio
def search_user_database(query):
    count = 0
    if not query or " " in query:
        return None, "No search query", False
    for letter in query:
        if not "a" <= letter <= "z":
            return False, "Invalid characters", False
        count += 1
    if query == "john":
        return 3, "Found 3 users", True
    return 0, "No users found", True


result, message, success = search_user_database("")
print(result)
print(message)
print(success)

result, message, success = search_user_database("     ")
print(result)
print(message)
print(success)

result, message, success = search_user_database("user123")
print(result)
print(message)
print(success)

result, message, success = search_user_database("user@email")
print(result)
print(message)
print(success)

result, message, success = search_user_database("admin")
print(result)
print(message)
print(success)

result, message, success = search_user_database("john")
print(result)
print(message)
print(success)

# Question 2: Book Collection Status
def analyze_book_pages(integers):
    count = 0
    pages = 0
    average = 0
    
    if not integers or " " in integers: 
        return 0, 0, 0.0, False
    count = len(integers)
    pages = sum(integers)
    average += pages / count
    for integer in integers: 
        if integer > 500: 
            return count, pages, average, True
    return count, pages, average, False

count, total, avg, has_long = analyze_book_pages([250, 180, 620, 310])
print(count)
print(total) 
print(avg) 
print(has_long) 

count, total, avg, has_long = analyze_book_pages([200, 150, 300])
print(count)
print(total) 
print(avg) 
print(has_long) 

count, total, avg, has_long = analyze_book_pages([])
print(count)
print(total) 
print(avg) 
print(has_long) 

count, total, avg, has_long = analyze_book_pages([500, 400, 300])
print(count)
print(total) 
print(avg) 
print(has_long) 

count, total, avg, has_long = analyze_book_pages([501, 400, 300])
print(count)
print(total) 
print(avg) 
print(has_long) 