#Quiz Game in python

Questions = ("When was Pakistan made?",
             "When did the great Indo-Pak war sparked?",
             "What's the most populated city in Pakistan?",
             "What's the most largest province by land? ",
             "When did the great Earthquake occur in Pakistan?")
Options =(("A. 1954 ","B. 1899 ","C. 1945 ","D. 1947 "),
          ("A. 2001","B. 1564","C. 1959","D. 1965"),
          ("A. Quetta","B. Islamabad","C. Karachi","D. Lahore"),
          ("A. Sindh","B. Punjab","C. Balochistan","D. KPK"),
          ("A. 2005","B. 2025 ","C. 2009 ","D. 1972 "))

Guesses = []
Answers = ("D","D","C","B","A")

Question_num = 0
score = 0

for question in Questions:
    print("--------------------------")
    print(question)
    for option in Options[Question_num]:
        print(option)
    
    guess = input("Please enter an option (A,B,C,D): ").upper()
    Guesses.append(guess)

    if guess == Answers[Question_num]:
        score += 1
        print("CORRECT !")
    else:
        print("INCORRECT !")
        print(f"{Answers[Question_num]} is the correct answer.")
    Question_num+=1

print("---------------------------")
print("          RESULTS          ")
print("---------------------------")

print("Answers: ", end = "")
for answers in Answers:
    print(answers, end = " ")
print()

print("Guesses: ", end = "")
for guess in Guesses:
    print(guess, end = " ")
print()

Percentage = (score/Question_num) * 100
print(f"Your Result is {Percentage}% ")