# Ask for the temperature in celsius

temperature = int(input("Whats the temperature in Celsius today?"))

if temperature < 20:
    activity = "indoor reading"

    print(" Its cool today! You can do", activity)
else:
    activity = "outdoor play"

    print(" Its warm today! You can go for", activity)

is_raining = input("Is it raining? ")

if is_raining == "yes":
    print("Choose an indoor activity or get an umbrella!")

homework_time = int(input("Do you have homework time (mins)"))

if homework_time > 60:

    needs_break = "yes"

    print(" You have a lot of study time today. ")
    print(" Take a break before doing your ", activity)
else:

    needs_break = "no"

free_time = input(" Do you have any free time today? (yes/no)")

if free_time == "yes":
    final_task = "hobby time"
    print(" You have free time.")
    print(" Enjoy your ", final_task)
else:
    final_task = " planning"
    print(" You dont have much free time.")
    print(" Use some time for ", final_task)


print("")
print("===== DAILY ACTIVITY PLANNER: SUMMARY =====")
print(" Temperature: ", temperature)
print(" Chosen Activity: ", activity)
print(" Is it raining: ", is_raining)
print(" Study break status ", needs_break)
print(" Final task: ", final_task)
print(" ==========================================")
print("")