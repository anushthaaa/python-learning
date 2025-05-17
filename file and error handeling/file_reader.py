# reading a file

with open("guest.txt", "w") as object:
    object.write("")

name = 1
while name <= 2:
    naam = input("Enter your name: ").title()
    print("Thankyou for enteing your name.")
    why = input("Why do you like programming?: ")
       
    with open("guest.txt", "a") as object:
        object.write(naam + "\n")
        object.write("-" + why + "\n")
        

    name += 1


