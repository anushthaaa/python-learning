import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""
    
    def setUp(self):
        """Create an employee instance for use in all test methods."""
        self.employee = Employee('John', 'Doe', 60000)
    
    def test_give_default_raise(self):
        """Test that the default raise works correctly."""
        initial_salary = self.employee.annual_salary
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, initial_salary + 5000)
    
    def test_give_custom_raise(self):
        """Test that a custom raise works correctly."""
        initial_salary = self.employee.annual_salary
        custom_raise = 7500
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.annual_salary, initial_salary + custom_raise)

if __name__ == '__main__':
    unittest.main()
    