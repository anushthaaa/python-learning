import json

def get_username():
    """Get stored username if availabe"""
    filename = "username.json"
    try:
        with open(filename) as obj:
            username = json.load(obj)
    except FileNotFoundError:
        None
    else:
        return username

def greet_user():
        """Greets user or creates new file with username."""
        username = get_username()
        if username:
             print("Welcome back, "+ username.title())
        else:
             with open("username.json", "w") as obj:
                  username = input("Enter your username: ")
                  json.dump(username, obj)
                  print("We'll remeber you next time, "+ username)

greet_user()

        

                 
            

    


