from question_model import Question
from data import question_data

question_bank = []

for _, (question, answer) in enumerate(question_data):
    question_bank.append(Question(text=question, answer=answer))

print(question_bank[0])