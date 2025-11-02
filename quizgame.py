questions = ("When did Kenya gain independence? ", 
             "Who was the first president of Kenya? ",
             "How many counties does Kenya have? ",
             "What is the capital city of Kenya? ",
             "Who is the governor of the capital city? ")

choices =  (("A. 1925", "B. 1960", "C. 1963", "D. 1966"), 
            ("A. Tom Mboya", "B. Jomo Kenyatta", "C. Oginga Odinga", "D. Nelson Mandela"), 
            ("A. 12", "B. 40", "C. 36", "D. 47"), 
            ("A. Mombasa", "B. Kisumu", "C. Kitale", "D. Nairobi"), 
            ("A. Jonnson Sakaja", "B. Mike Sonko", "C. Idah Odinga", "D. Willis Raburu"))

answers = ("C", "B", "D", "D", "A")

question_num = 0
score = 0
guesses = []


print("-----Quiz Time-----")
print()

for question in questions:
    print("----------------------")
    print(question)

    for choice in choices[question_num]:
        print(choice)
    print()

    guess = input("Enter: A, B, C, or D: ").upper() 

    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    elif guess != answers:
        print(f"{guess} is not a valid answer. The correct answer is {answers[question_num]}")
    elif guess == "":
        print(f"You did not choose. The correct answer is {answers[question_num]}")
    else:
        print(f"Incorrect. The correct answer is {answers[question_num]}")

    question_num += 1
quiz_num = int(len(answers))
final_score = int((score / quiz_num) * 100)
print(f"The correct answers were: {answers}")
print(f"You wrote: {guesses}")
print((f"Your score is: {final_score}%."))

print("Thanks for playing, Byee")


    