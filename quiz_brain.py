class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        # instead of doing if/then you can just return the statement by itself. it will be either true or false.
        return self.question_number < len(self.question_list)


    def next_question(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {question_text} (True/False)?: ')
        self.check_answer(user_answer, question_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    # def return_final_score(self):
    #     print("You've completed the quiz")
    #     print(f"Your final score was: {self.score}/{self.question_number}")