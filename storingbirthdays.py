# Get the module for Keywords

import keyword


# Variables and Input for: Persons name,  Goal,  And target month

person_name = input("Enter Name:")
person_goal = input("Enter Goal:")
target_month = input("Enter Target Month:")
daily_mins = 30

# Prints multiple Values


print("Your name:", person_name)
print("Your goal:", person_goal)
print("Your Target Month:", target_month)
print("Daily Practice Time:", daily_mins, "mins")

# Start a new line using \n 

print("\n My personal Goal plan \n ")

# Change how print status ends

print("Goal status:", end=" ")
print("Not Started")

print("Progress Reminder:", end=" - ")
print("Practice every day!")

# Print the summary

print("Summary: \n ")

print("\n", person_name, "plans to work on", person_goal, "for", daily_mins, " mins Every day!")


# Prints all the keywords

print("\n Python keywords are \n")
print(keyword.kwlist)