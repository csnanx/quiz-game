class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def get_valid_answer(self, current_question):
        while True:
            answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
            if answer.lower() in ["true", "false"]:
                return answer
            print("Invalid input. Please enter 'True' or 'False'")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = self.get_valid_answer(current_question)
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, right_answer):
        if user_answer.lower() == right_answer.lower():
            print("You are ABSOLUTELY RIGHT!")
            self.score += 1
        else:
            print("How can you be this wrong?")
        print(f"The right answer was: {right_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")