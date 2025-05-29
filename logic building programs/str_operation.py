# program to check whether the string is 
# pallindrome or nor, or to reverse the string

def isPallindrome():
    string = input("Enter a string: ").lower().strip()

    for i in range(len(string) // 2):
        if string[i] != string[-i-1]:
            print("Not Pallindrome..!!")
            return
        
    print("Pallondrome...!!")
        
def rev_string():
    string = input("Enter a string: ").lower().strip()
    rev_string = ""

    for ch in string:
        rev_string = ch + rev_string

    print("Reversed string: ", rev_string)


while(True):
    print("Enter your choice:\n1. To check pallindrome or not.\n2. To reverse the string.\n3. Exit")
    try:
        choice = int(input("Enter your choice(1-3): "))
    except ValueError:
        print("Invalid input, please enter your choice between 1-3.")
        continue

    if choice == 1:
        isPallindrome()
    elif choice == 2:
        rev_string()
    elif choice == 3:
        print("Goodbyee.")
        break

    input("Press Enter to continue...") 


            




    

    
    