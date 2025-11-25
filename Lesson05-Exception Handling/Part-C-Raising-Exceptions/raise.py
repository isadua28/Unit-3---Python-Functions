# The raise syntax
# Basic Syntax

"""
Raise ExceptionType("Your message!")
Examples:
raise ValueError("Quantity must be at least 1)
raise TypeError("Expected a player object, got a potato!)
raies PermissionError("You are not a mod, nice try though!)"""
# Just returning
def open_loot_box(player, qty):
    if qty <= 0:
        return None
    # Rest of the code

# Raise exception
def open_loot_box(player, qty):
    if qty <= 0:
        raise ValueError("Bad qty!")
    # Rest of the code 