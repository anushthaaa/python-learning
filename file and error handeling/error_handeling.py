

while True:
    try:
        a = input("enter a: ")
        b = input("enter b: ")
        a = int(a)
        b = int(b)
        sum = a + b
        print(f"The sum is {sum}")
    except TypeError:
        print("You must enter two integrer numbers.")
    except ValueError:
        print("Must ener two integers.")
