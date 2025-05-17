class Employee:
    """A simple employee class."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, amount=5000):
        """Give the employee a raise.
        
        Args:
            amount (int, optional): Amount to raise salary. Defaults to 5000.
        """
        self.annual_salary += amount