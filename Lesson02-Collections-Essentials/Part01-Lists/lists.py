"""
JavaScript Arrays vs Python Lists

Create - [1, 2, 3]
Add - .append(val)
Remove end - .pop()
Insert - .insert(index, val)
Length - len(list)
Slice - [start: end]
Index - [0]
Maximum - max(engagement)
Minimum - min(engagement)
total = sum(engagement)
"""

# creating lists
daily_likes = [500, 600, 750, 400]
usernames = ["@nasa", "@tswift", "@user123", "@netflix"]
mixed_data = [500, "likes", "@user123", True]
# accessing elements 
first_day = daily_likes[0]
last_day = daily_likes[-1]
third_day = daily_likes[2]
# slicing 
first_three = daily_likes[0:3]
last_two = daily_likes[-2:]

# code along - post analyzer
def analyze_post(likes_list):
    if likes_list:
        total = sum(likes_list)
        average = total / len(likes_list)
        best_day = max(likes_list)
        return (average, best_day)
    return "The list is empty!"

def format_usernames(handles):
    formatted = []
    for username in handles:
        formatted.append("@" + username)
    return formatted
result = format_usernames(["nasa", "tswift", "netflix"])
print(result)

def filter_trending_posts(likes_list):
    trending_posts = []
    for likes in likes_list:
        if likes > 1000:
            trending_posts.append(likes)
    return trending_posts
result = filter_trending_posts([500, 1200, 800, 1500, 600])
print(result)