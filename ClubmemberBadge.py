# Ask the club member for their details.
name = input("Enter your real name, club member: ")
club = input("Enter your school name: ")

# Store the members details using Data types

member_number = 8
point_earned = 9.5
event_count = 6
meeting_hours = 1.5
is_active = True

# Print each detail along with data type
print("Name:", name, "--> type:", type(name))
print("Club:", club, "--> type:", type(club))
print("Member Number:", member_number, "--> type:", type(member_number))
print("Points earned:", point_earned, "--> type:", type(point_earned))
print("Event Count:", event_count, "--> type:", type(event_count))
print("Meeting hours:", meeting_hours, "--> type:", type(meeting_hours))
print("Is active:", is_active, "--> type:", type(is_active))


# Typecast numbers and true or false

member_number_text = str(member_number)
event_count_text = str(member_number)
points_text = str(point_earned)
status_text = str(is_active)


print(" Member number as text:", member_number_text, "-> type", type(member_number_text))
print("  Event count as text", event_count_text, "-> type", type(event_count_text))
print(" Points as text:", points_text, "-> type", type(points_text))
print(" Status as text:", status_text, "-> type", type(status_text))

# Slice name for a badge code

first_three = name[0:3]
last_letter = name[-1:]
badge_code = first_three + last_letter

print("First three letters of name:", first_three)
print("Last letter of name:", last_letter)
print("Badge code:", badge_code)


# Reverse the club by slicing 

reversed_club = club[::-1]
print("Reversed club name:", reversed_club)


# join everything together to build the final badge message

badge_line_1 = "CLUB MEMBER" + badge_code.upper()
badge_line_2 = "ID: " + member_number_text + " | EVENTS:  " + event_count_text
badge_line_3 = "POINTS: " + points_text + " | ACTIVE: " + status_text
badge_line_4 = " SECRET CLUB CODE: " + reversed_club.upper()

print("")
print("====== SCHOOL CLUB MEMBER BADGE ======")
print(badge_line_1)
print(badge_line_2)
print(badge_line_3)
print(badge_line_4)
print("======================================")