# Part 1: Ask the agent for their details

name = input("Enter your real name, Agent:")
gadget = input("Enter your favorite gadget:")


# Agent Details

agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True


# Print details with Data type

print("Name:", name, "--> type: ", type(name))
print("Gadget:", gadget, "--> type: ", type(gadget))
print("Agent Number: ", agent_number, "--> type", type(agent_number))
print("Speed rating:", speed_rating, "-- type: ", type(speed_rating))
print("misson count:", mission_count, "-- type: ", type(mission_count))
print("height(M) ", height_m, "-- type: ", type(height_m))
print("is active: ", is_active, "-- type: ", type(is_active))

# Typecasting

agent_number_text =  str(agent_number)
misson_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("Agent Number as Text", agent_number_text, "--> type", type(agent_number_text))
print("Speed rating:", speed_rating_text, "-- type: ", type(speed_rating_text))
print("misson count:", misson_count_text, "-- type: ", type(misson_count_text))

# Slicing

first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter