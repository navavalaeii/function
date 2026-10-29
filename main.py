# print("what's the best CMS?") #namayesh soal karbar
# print("A:wordpress")# namayesh gozineha
# print("B:Joomla")# daryaft javab az karbar
# print("C:Drupal")#namayesh dorost o ghalat boodan
# print("B:Headless")
from rich.console import Console
console = Console()

questions=[
    ("what's the bestCMS?",["A wordpress","B:Joomla","C:Drupal","D: headless"],"A"),
    ("what's the best programming language ?",["A Python","B:JavaScript","C:Java","D:C++ "],"A"),
    ("what's the best database ?",["A:MySQL ","B:PostgreSQL","C:MonoDB","D:SQL "],"B"),

                            
]

def show_menu():
    user_input = input("do you want to start the quiz? (yes/no): ").strip().lower()
    if user_input == "yes":
        return True
    elif user_input == "no":
        print("exiting the quiz.goodbye")
        exit()
    else:
        print("invalid input, please enter 'yes' or 'no'.")


def play_quiz():
    score=0
    user_correct=0
    BONUS=10
    PENALTY=3
    for questions,option,correct_answer in questions:
        print(questions)
    for option in option:
        print(option)
    user_answer=str(input("Your choice:").strip().upper())
    if user_answer==correct_answer:
        print("Correct")
        score+=BONUS
        user_correct+=1
    else:
        print("Incorrect")
        score-=PENALTY
    return score,user_corrects


def show_results(score, user_corrects):
    print(f"Your final score is:{score}")
    print(f"Your answer{user_correct}question correctly.")
    print(f"Percentage:{user_correct/len(questions)*100}")

while True:
    if show_menu():
        break

score, user_correctst = play_quiz()
show_results(score , user_corrects)
