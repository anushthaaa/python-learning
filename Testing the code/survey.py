class AnonyomousSurvey:
    """Collect anonyomous answers to a survey question."""

    def __init__(self,question):
        """Store a question and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_result(self):
        """show all the responses that have been given"""
        print("survey result:")
        for response in self.responses:
            print("-" + response.title())





