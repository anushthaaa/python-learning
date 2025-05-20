class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
       

    def describe_user(self):
        print(f"The user's name is {self.first_name} {self.last_name} with age {self.age} and lives in {self.location}.")

    def greet_user(self):
        print(f"Hi {self.first_name}!")

    

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can reset passwords"]
    
    def show_privileges(self):
        print("\nThis user has the following privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        # Initialize the parent class (User) attributes
        super().__init__(first_name, last_name, age, location)
        
        # Create a Privileges instance as an attribute
        self.privileges_manager = Privileges()


def create_user():
    """Create and return a regular user"""
    print("\n=== CREATING REGULAR USER ===")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    location = input("Enter location: ")
    
    user = User(first_name, last_name, age, location)
    user.greet_user()
    user.describe_user()
    
    return user


def create_admin():
    """Create and return an admin user"""
    print("\n=== CREATING ADMIN USER ===")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age = int(input("Enter age: "))
    location = input("Enter location: ")
    
    admin = Admin(first_name, last_name, age, location)
    admin.greet_user()
    admin.describe_user()
    admin.privileges_manager.show_privileges()
    
    return admin


# Main program
print("Welcome to the User Management System")
print("1. Enter as Regular User")
print("2. Enter as Admin")

while True:
    option = input("\nEnter your choice (1 or 2): ")
    
    if option == "1":
        current_user = create_user()
        print("\nYou are now logged in as a regular user.")
        break
    elif option == "2":
        current_user = create_admin()
        print("\nYou are now logged in as an admin.")
        break
    else:
        print("Invalid option. Please enter 1 for Regular User or 2 for Admin.")

print("\nThank you for using the User Management System!")

