def create_username(first_name, last_name): 
    username = f"{first_name.lower()}_{last_name.lower()}"
    return username
print(create_username("John", "Smith"))
print(create_username("MARY", "Jones"))
print(create_username("Alex", "TAYLOR"))

"""
def create_uesrname(first_name, last_name):
    return f"{first_name}_{last_name}".lower()
"""

def check_email(email):
    if "@" in email and email.endswith(".com") or email.endswith(".COM"):
        return True
    return False

print(check_email("test@gmail.com"))
print(check_email("user@yahoo.COM"))
print(check_email("invalid.com"))
print(check_email("test@school.edu"))

"""
def check_email(email):
    email_lower = email.lower()
    return "@" in email_lower and email_lower.endswith(".com")"""
    
def create_slug(title):
    return title.lower().strip().replace(" ", "-")

print(create_slug("My First Blog Post"))
print(create_slug("     Python Tutorial     "))
print(create_slug("Web Development 101"))