a = int(input("Enter a value: "))
b = int(input("Enter a value 2: "))
c = int(input("Enter a value 3: "))

avg = (a + b + c) / 3
print("Avg: ", avg)


if avg > a and avg > b and avg > c:
    print(f"{avg} is higher than {a}, {b}, and {c}.")
elif avg > a and avg > b:
    print(f"{avg} is higher than {a}, {b}, .")
elif avg > a and avg > c:
    print(f"{avg} is higher than {a}, {c}, .")
elif avg > b and avg > c:
    print(f"{avg} is higher than {b}, {c}, .")
elif avg > a:
    print(f"{avg} is higher than {a}")
elif avg > b:
    print(f"{avg} is higher than {b}")
elif avg > c:
    print(f"{avg} is higher than {c}")
else:
    print("Invalid input.")



