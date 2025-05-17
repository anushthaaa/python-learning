import unittest
from city_function import get_city

class TestCity(unittest.TestCase):

    def test_city_country(self):
        details = get_city("kathmandu", "nepal", "population")
        self.assertEqual(details, "Kathmandu, Nepal - Population")

unittest.main()

    

