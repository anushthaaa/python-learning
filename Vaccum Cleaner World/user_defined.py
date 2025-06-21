print("\nVacuum Cleaner World")
state = int(input("Enter state (1 to 8): "))

# given states
states = {
    1: {'location': 'A', 'A': 'Dirty', 'B': 'Dirty'},
    2: {'location': 'B', 'A': 'Dirty', 'B': 'Dirty'},
    3: {'location': 'A', 'A': 'Dirty', 'B': 'Clean'},
    4: {'location': 'B', 'A': 'Dirty', 'B': 'Clean'},
    5: {'location': 'A', 'A': 'Clean', 'B': 'Dirty'},
    6: {'location': 'B', 'A': 'Clean', 'B': 'Dirty'},
    7: {'location': 'A', 'A': 'Clean', 'B': 'Clean'},
    8: {'location': 'B', 'A': 'Clean', 'B': 'Clean'}
    }

# validity check
if state not in states:
    print("Invalid choice. Please choose 1 to 8.")
    exit()

# gettin initial values (starting point)
location = states[state]['location']
A = states[state]['A']
B = states[state]['B']

print("\n-----analyzing-----\n")


if location == 'A':
    print("Vacuum is in room A")
    if A == 'Dirty':
        print("Cleaning Room A")
        A = 'Clean'
    else:
        print("Room A already clean")

    print("Moving to Room B")
    location = 'B'

    if B == 'Dirty':
        print("Cleaning Room B")
        B = 'Clean'
    else:
        print("Room B already clean")

else: 
    print("Vacuum is in Room B")
    if B == 'Dirty':
        print("Cleaning Room B")
        B = 'Clean'
    else:
        print("Room B already clean")

    print("Moving to Room A")
    location = 'A'

    if A == 'Dirty':
        print("Cleaning Room A")
        A = 'Clean'
    else:
        print("Room A already clean")



print("\nFinally,")
print(f"Room A is {A}.")
print(f"Room B is {B}.")
print(f"Vacuum is in Room {location}.")


if A == 'Clean' and B == 'Clean':
    print("\nHence, both rooms are clean.")
    print("Mission accomplished!!!")
else:
    print("\nstill dirt remaining.")
