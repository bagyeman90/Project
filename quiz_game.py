print("Welcome to the Quiz Game")

first_question = input("Do youy want to play? ")
yes = "yes"
no = "no"
if first_question == yes:
    print("Enter the guess number")
    
else:
    print("This is the end of the game ")
    quit()

print("OKAY!!!")
print("Let's play")
score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memmory":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str(score) / 4 * 100 + " %.")

