from survey import AnonyomousSurvey

# define a question and make a survey
question = input("your first language?: ")
ans = AnonyomousSurvey(question)

# show the results and store the responses into the question
ans.show_question()
print("enter 'q' to quit anytime.\n")

while True:
    response = input("Language: ")
    if response == "q":
        break
    ans.store_response(response)

#  show survey results
print("\nThankyou to everyone who participated in the survey.")
ans.show_result()



