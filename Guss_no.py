import random

password = random.randrange(100, 999)
print("Password:", password)

tries = 10
attempts = 0

while attempts < tries:
    i = input("Guess the 3-digit number: ")
    
    if not i.isdigit() or len(i) != 3:
        print("Invalid input! Please enter a 3-digit number.\n")
        continue

    guess = int(i)
    attempts += 1

    if guess == password:
        print("Successful! You guessed it right.")
        break
    else:
        
        passwordstr = str(password)
        guessstr = str(guess)
        
        rightplace = 0
        wrongplace = 0
        
        for j in range(3):
            if guessstr[j] == passwordstr[j]:
                rightplace += 1
            elif guessstr[j] in passwordstr:
                wrongplace += 1

        print(f"Wrong guess. {tries - attempts} attempts left.")
        print(f"Hints: {rightplace} digit(s) in the right place, {wrongplace} digit(s) correct but in wrong place.\n")

if attempts == tries and guess != password:
    print("All 10 attempts used! The correct number was:", password)