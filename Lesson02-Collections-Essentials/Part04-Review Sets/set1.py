# Question 1: Viewer Peak Detection
# 2300

# Question 2: Chat Filter
# "WOW WOW LFG"

# Question 3: 

def find_top_donor(donations): 
    top_donor = ""
    top_amount = 0
    for key, value in donations.items(): 
        if value > top_amount: 
            top_amount = value
            top_donor = key 
    return top_donor 

donations = {
    "neon": 250,
    "vibe": 180,
    "lunar": 400, 
    "pixel": 150
}

print(find_top_donor(donations))