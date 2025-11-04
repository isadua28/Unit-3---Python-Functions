# Q1 
# {"key_a": "value1", "key_b": 150, "key_d": 50} 
# "key_c" = False

# Q2
# 120
# 60

# Q3

# def get_user_bio(user): 
#     for key, value in user.items():
#         if key == "bio":
#             return value
#     return "No bio available"
# print(get_user_bio({"username": "coder", "bio": "Python enthusiast"}))
# print(get_user_bio({"username": "newbie"}))

# Q4
# {"id": 2, "score": 60}
# {"id": 3, "score": 160}

# Q5
# 1

# Q6

def get_total_engagement(post):
    sum = 0
    if not "likes" in post:
        post["likes"] = 0
    if not "comments" in post:
        post["comments"] = 0
    if not "shares" in post:
        post["shares"] = 0
    
    sum += post["likes"] + post["comments"] + post["shares"]
    return sum

print(get_total_engagement({"likes": 100, "comments": 20, "shares": 10}))
print(get_total_engagement({"likes": 50, "comments": 5}))
print(get_total_engagement({"views": 1000}))

# Q7
# {"alpha": 3}
# 3

# Q8
# {"key1": "value1", "key2": 200, "key3": 50}
# {"key1": "value1", "key2": 100, "key4": True}

# Q9

def find_most_followed(users):
    max_followers = 0
    if users:
        for user in users:
            if user["followers"] > max_followers:
                max_followers = user["followers"]
        return max_followers
    return None

users = [
    {"username": "alex", "followers": 1000},
    {"username": "sam", "followers": 5000},
    {"username": "jordan", "followers": 3000}
]

print(find_most_followed(users))