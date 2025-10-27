announcement = "   BERGEN TECH robotics meeting TODAY!   "

def format_course_code(code):
    trimmed = code.strip()
    print(f"After strip: '{trimmed}'")
    
    uppercased = trimmed.upper()
    print(f"After upper: '{uppercased}'")
    return uppercased 

print(format_course_code("  webdev101  "))
print(format_course_code("  Python202  "))
print(format_course_code("Java303"))

def count_hashtags(post):
    words = post.split()
    count = 0
    for word in words:
        if word.startswith("#"):
            count += 1
post1 = "Great game today! #BergenTech #GoGamrz #Pride"
post2 = "Meeting tomorrow in room 205"
post3 = "#Robotics team wins #StateChampionship! #STEM #BergenTech"

print(count_hashtags(post1))
print(count_hashtags(post2))
print(count_hashtags(post3))

# .endswith()

# filename = "assignments.pdf"
# print(filename.endswith(".pdf"))
# print(filename.endswith(".docx"))