print("Enter marks obtained in 5 subjects")

markone = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())

total = markone + marktwo + markthree + markfour + markfive
avg = int(total / 5)

validRange = range(0,101)

if avg not in validRange:
    print("Invalid input")

elif avg in range(91,101):
    print("Your grade is A1")
elif avg in range(81,91):
    print("Your grade is a2")
elif avg in range(71,81):
    print("Your grade is b1")

elif avg in range(61,71):
    print("Your grade is b2")
elif avg in range(51,61):
    print("Your grade is c1")
elif avg in range(41,51):
    print("Your grade is c2")

elif avg in range(33,41):
    print("Your grade is d")
elif avg in range(21,33):
    print("Your grade is e1")
elif avg in range(0,21):
    print("Your grade is e2")



