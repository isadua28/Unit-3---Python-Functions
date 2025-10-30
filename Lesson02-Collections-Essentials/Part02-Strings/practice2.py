def format_phone_number(phone):
    formatted = phone.remove(" ", "").remove("-", "").remove("(", "").remove(")", "")
    
    if len(formatted) != 10 or not formatted.isdigit():
        return "Invalid phone number"
    
    area = formatted[:3]
    prefix = formatted[3:6]
    line = formatted[6:]
    
    return f"({area}) {prefix}-{line}"