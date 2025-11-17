# Question 2: Create Card Function

def create_card(name, level=1, active=False):
    dictionary = {"name": name, "level": level, "active": active}
    return dictionary

print(create_card("Fireball"))
print(create_card("Shield", level=3, active=True))

# Question 4: 

def build_profile(username, **stats): 
    if not stats:
        return {"username": username}

    # Way 1
    # profile = {"username": username}
    # for key, value in stats.items():
    #     profile[key] = value
    # return profile 
    
    # Way 2
    # dictionary = {"username": username}
    # dictionary.update(stats)
    # return dictionary 

    # Way 3
    return {"username": username, **stats}

print(build_profile("gamer42", score=850, rank="Gold"))
print(build_profile("player1"))

