from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# it is expected for the objects to appear in the list as their location in memory.
# access attribute using the number of the list item and the name of the attribute.
# e.g. question_bank[0].text, which is the text attribute of the object stored in the list at 0
# print(question_bank)
# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

# quiz.return_final_score()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")