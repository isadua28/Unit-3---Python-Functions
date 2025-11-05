# Question 3

def calculate_engagement_rate(post):
#     engagement = 0
#     engagement += post["likes"] + post["comments"] + post["shares"]
#     rate = ((engagement / post["views"]) * 100)
#     rate = round(rate, 2)
#     if not "views" in post or "views" == 0:
#         return 0
#     return f"{rate}"

# post = {"views": 1000, "likes": 50, "comments": 10, "shares": 5}
# print(calculate_engagement_rate(post))

# ALT SOLUTION

    views = post.get("views", 0)
    
    if views == 0:
        return 0
    
    likes = post.get("likes", 0)
    comments = post.get("comments", 0)
    shares = post.get("shares", 0)
    
    engagement = likes + comments + shares
    rate = (engagement / views) * 100
    return f"{rate:.2f}"

    