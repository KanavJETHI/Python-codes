print("Welcome to the quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("ok! Let's start the quiz :)")
score = 0

answer = input("Who developed python programing language? ")
if answer.lower() == "Guido van Rossum":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is the correct extension for python file? ")
if answer.lower() == ".py":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("Which character in python is used to give multi line comments? ")
if answer.lower() == "#":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PIP stand for? ")
if answer.lower() == "preferred installer program":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
    
    answer = input("What arithmetic operator cannot be used with strings in python? ")
if answer.lower() == "-":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
