# Question 5: Code Tracing 
"""
18.0
15.0
"""

# Question 6: Code Writing

def make_notification(user, *messages, urgent=False): 
    notifs = ", ".join(messages)
    if urgent==False: 
        return f"{user} - {notifs}"
    return f"URGENT: {user} - {notifs}"

print(make_notification("admin", "Server down!", urgent=True))
print(make_notification("user", "Welcome", "Check inbox"))

# Question 7: Code Tracing
"""
SELECT name, email FROM users LIMIT 10
SELECT * FROM logs WHERE "level='error'" LIMIT 5
"""

# Question 8: Code Writing

def log_action(actor, *actions, timestamp=None, **context): 
    action = ", ".join(actions)
    info = ""
    for key in context: 
        info += f"{key}={context[key]}, "
    info = info.rstrip(", ")
    return f"{actor}: {action} | {info}"

print(log_action("bot", "login", "scan", source="API", ip="1.2.3.4"))