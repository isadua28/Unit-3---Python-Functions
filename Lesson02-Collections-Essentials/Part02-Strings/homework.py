# 1
# john.smith @gmail.com

# 2
# tqbf

# 3
def extract_domain(email):
    at_count = email.count("@")
    if at_count != 1:
        return "Invalid email"
    parts = email.split("@")[1]
    domain = parts.lower()
    return domain

print(extract_domain("john@gmail.com"))
print(extract_domain("JANE@YAHOO.COM"))
print(extract_domain("missing.at.sign.com"))
print(extract_domain("too@@many@signs.com"))
    
# 4
# 123456

# 5
# MY_DOCUMENT

# 6
# banana

# 7
def filter_numbers(text):
    new_text = ""
    for char in text:
        if not char.isdigit():
            new_text += char
    return new_text
    
print(filter_numbers("Hello123World456"))
print(filter_numbers("Test 1 2 3"))
print(filter_numbers("Price: $29.99"))
print(filter_numbers("No numbers here!"))

# 8 
# https://example.com/user/profile

# 9 
def count_character_types(text):
    letter_count = 0
    digit_count = 0
    spaces_count = 0
    
    for char in text:
        if "a" <= char <= "z" or "A" <= char <= "Z":
            letter_count += 1
        elif "0" <= char <= "9":
            digit_count += 1
        elif char == " ":
            spaces_count += 1
    return f"Letters: {letter_count}, digits: {digit_count}, spaces: {spaces_count}"
print(count_character_types("Hello 123"))
print(count_character_types("Test2024!"))