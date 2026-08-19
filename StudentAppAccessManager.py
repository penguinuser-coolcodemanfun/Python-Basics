Camera = 1
Microphone = 2
Storage = 4
Location = 8 

restricted_apps = ["gaming app", "social media app", "shopping app",]
approved_Apps = [ "coding app", "math app", "science app", "reading app"]

student_name = input("Name: ").capitalize().strip()
requested_app = input("Your requested app: ").lower().strip()

print(" \n ===== IDENTITY OPERATOR CHECK =====")

if student_name is str:
    print("The name entered is a text value.")

if requested_app is not int:
    print("The requested app you entered is not a number value.")

print("\n ===== Membership Operator Check =====")

if requested_app in approved_Apps:
    print(" The app you have chosen is an Approved App.")
if requested_app not in restricted_apps:
    print(" The app you have chosen is not in restricted apps.")

print("\n ===== App Permisson Settings =====")

student_permisson = Camera | Microphone | Storage | Location

print("Permission value: ", student_permisson)

print("Permission bits: ",bin(student_permisson))

if student_permisson & Camera:
    print("Camera Permission is Enabled.")
if student_permisson & Microphone:
    print("Microphone permisson is enabled.")
if student_permisson & Storage:
    print("Storage permission is enabled.")
if student_permisson & Location:
    print("Location permission is enabled.")

next_permission = Camera << 1
print("Camera bit:", bin(Camera))
print("After left shift:", bin(next_permission))

previous_permission = Storage >> 1

print("Storage bit:", bin(Storage))
print("After right shift:", bin(previous_permission))

print("\n ===== Final Access Result =====")

if requested_app in approved_Apps and requested_app not in restricted_apps:
    print("The access is granted to", requested_app)
else:
    print("The Access is Denied to", requested_app)
