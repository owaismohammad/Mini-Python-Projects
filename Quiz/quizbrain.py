
class Quiz_brain:
    def __init__(self,list):
        self.question_number=0
        self.question_list=list
        self.score=0

    def check_ans(self, correctans, userans,):
        if correctans.lower()==userans.lower():
            self.score+=1
            print("You got it right!")
            print(f"The correct answer was: {correctans}")
            print(f"Your current score is{self.score}/{self.question_number}")
            print()
        else:

            
            print("You got it Wrong!")
            print(f"The correct answer was: {correctans}")
            print(f"Your current score is{self.score}/{self.question_number}")
            print()


    def next_question(self,):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        score=self.question_number
        user_ans=input(f"Q{self.question_number}. {current_question.text} (True/False): ")
        correct_ans=current_question.answer
        self.check_ans(correct_ans,user_ans)


    def still_has_questions(self):
        if self.question_number==len(self.question_list):
            return True
        else:
            return False
        

