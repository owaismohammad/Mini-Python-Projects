from question import Questions
from questionData import question_data
from quizbrain import Quiz_brain
import art

print(art.logo)
l=len(question_data)
question_bank=[]
for r in range(l):
    q1=question_data[r]["question"]
    a1=question_data[r]["correct_answer"]
    question_bank.append(Questions(q1,a1))
quiz=Quiz_brain(question_bank)

d=0
while quiz.still_has_questions()==False:
    quiz.next_question()
print()
print("You've Completed the Quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
print()
print(art.end)
