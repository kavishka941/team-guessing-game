import random
number = random.randint(1, 50)
print("Guess a number between 1 and 50")
guess = int(input())

if guess < number:
    print("Too low!")
elif guess > number:
    print("Too high!")

if guess == number:
 print("You win!")
else:
 print(f"Wrong! The number was {number}")
 while True: 
    # (paste existing code here) 
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break 
