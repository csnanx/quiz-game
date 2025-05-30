from random import shuffle
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import welcome

print(welcome)
question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

shuffle(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{len(question_bank)} ({round(quiz.score / len(question_bank) * 100, 2)}%)")