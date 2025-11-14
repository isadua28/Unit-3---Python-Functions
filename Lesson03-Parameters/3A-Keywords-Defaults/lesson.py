def create_gamer(username, level, xp ,rank, online):
    """Create a gamer profile."""
    return {
        "username": username,
        "level": level,
        "xp": xp,
        "rank": rank,
        "online": online
    }

player1 = create_gamer(username="BTStudent",
                       level = 25,
                       rank="Gold",
                       xp=1000,
                       online=True)
print(player1)

def send_message(sender, recipient, message, urgent): 
    return f"{sender} -> {recipient}: {message} (Urgent: {urgent})"

message1 = send_message(sender = "Alex",
                        recipient = "Jordan",
                        message = "Check Discord",
                        urgent = True)
print(message1)

def post_content(username, text, likes=0, retweets=0):
    return f"@{username}: {text} | ❤️ {likes} 🔁 {retweets}" 

post = post_content("techguru", "Python is amazing!")
print(post)

# *args - Accept any number of values 

def sum_scores(*scores): 
    """Sum ANY Number of scores"""
    total = 0
    for score in scores: 
        total += score
    return total
