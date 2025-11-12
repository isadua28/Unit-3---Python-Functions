# Question 1 - Kill Streak Tracker 
# [26]

# Question 2 - Clan Tag Extractor 
# [NEXUS

# Question 3 - MVP Calculator 
def match_mvp(players): 
    best_player = ""
    best_ratio = 0.0
    for key, value in players.items(): 
        ratio = value["kills"] / value["deaths"]
        if ratio > best_ratio: 
            best_radio = ratio
            best_player = key
        return best_player
            
players = {
    "phoenix": {"kills": 28, "deaths": 12},
    "cipher": {"kills": 35, "deaths": 15},
    "blaze": {"kills": 22, "deaths": 18},
}
print(match_mvp(players))