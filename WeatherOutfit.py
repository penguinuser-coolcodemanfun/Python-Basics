# Ask for todays temperature 
temperature = int(input("Enter todays weather in Celsius: "))


if temperature < 20:
    outfit = "jacket"
    print(" Its cold today.")
    print("Wear a", outfit)
else:
    outfit = " t-shirt "
    print(" Its warm today,")
    print(" Wear a ", outfit)

is_raining = input(" Is it raining today? ")
if is_raining == "yes":
    print("Bring an umbrella!")

wind_speed = int(input("Enter the wund soeed in km/ h "))


if wind_speed > 30:
    needs_windbreaker = "yes"
    print("It is windy today.")
    print(" Wear a windbreaker over your outfit")

else:
    needs_windbreaker = "no"
    print(" It is calm today ")
    print(" No need windbreaker over your", outfit)

has_puddles = input(" Are there puddles on the ground? (Yes/No)")

if has_puddles == "yes":
    shoes = "boots"
    print(" The ground is wet.")
    print(" Wear,", shoes)
else:
    shoes = "Sneakers"
    print(" The ground is dry.")
    print(" Wear ", shoes)

print("")
print("Weather check complete!")

print("===== WEATHER OUTFIT PICKER =====")
print("Temperature:", temperature)
print("Outfit chosen:", outfit)
print("Raining:", is_raining)
print("Windbreaker Needed:", needs_windbreaker)
print("Shoes Chosen:", shoes)
print("=================================")