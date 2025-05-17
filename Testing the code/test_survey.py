import unittest
from survey import AnonyomousSurvey

class TestAnonyomousSurvey(unittest.TestCase):
    """test for class AnonyomousSurvey"""
    def setUp(self):
        """
        creating a survey and a set of responses for use in all test modules"""

        question = "first language?: "
        self.my_survey = AnonyomousSurvey(question)
        self.responses = ["eng", "nep", "chinese"]
        
    def test_store_single_response(self):
        """test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """testing that three individual responses are stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
