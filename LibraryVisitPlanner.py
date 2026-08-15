print("===== LIBRARY VISIT PLANNER =====")

day = input("What is the day today(Monday/ Friday)").capitalize().strip()
weather = input("Whats the weather today? (Sunny / Rainy / Cloudy)").lower().strip()
book_return = input(" Do you have to return any book today? (yes / no").lower().strip()

print()
print(f"=== Your library Plan for {day} =========")
print("-" * 35)

if day in ("Saturday", "Sunday"):
    print("Its a weekend. Perfect for a library visit!")
elif day == "Monday":
    print("Its Monday! The start of the week! Check your reading list.")
elif day == "Friday":
    print("Its friday! The last school day! Remember to give your books by the weekend")
elif day in ("Tuesday", "Wednesday", "Thursday" ):
    print("Its a regular school day! Plan a short library visit.")
else:
    print("Day not regconised. Check your spelling")

if weather == "sunny" and book_return == "yes":
    print("Tip: Go return a book!")

if weather == "rainy" or weather == "cloudy":
    print("Tip: Bring an umbrella!")

if not book_return == "yes":
    print("You do not have any book to return today!")


