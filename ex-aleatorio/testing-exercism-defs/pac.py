def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

result = eat_ghost(False,False)
print(result)