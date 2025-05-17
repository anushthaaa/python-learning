# applying the concept of inheretance

class Resturant: # class
    def __init__(self, name, cusineType):
        self.name = name #  attributes i.e properties
        self.cusineType = cusineType

    def describe_restro(self): # method
        print("The resturant name is "+ self.name + " and it has the cuisines "+ self.cusineType)

    def open_restro(self):
        print("The resturant; "+ self.name + " is opne.")

class IceCreamStand(Resturant):
    def __init__(self, name, cusineType, flavors):
        super().__init__(name, cusineType)
        self.flavors = ["strawberry", "chocolate", "blueberry"]
        
    def describe_flavors(self):
        print("The "+ self.name + " has the follwiing lists of flavors: "+ str(self.flavors))

restro1 = Resturant("Haadi Biryani", "Biryani") # instances
restro1.describe_restro()
restro1.open_restro()

icecreamrestro = IceCreamStand("Ice Cream Stand", "Icecreams", "flavors")
icecreamrestro.describe_flavors()
