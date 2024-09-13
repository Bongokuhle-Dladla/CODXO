import random

def guessing_game():
    print(" Welcome to the Number Guessing Game!")
    print(" Think of a number between 1 and 100.")
    print(" Remember you only have 10 attempt! ")
    
    
    num_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts :
        
        guess = int(input("Enter your guess: "))
        attempts += 1
            
        if guess < num_to_guess:
            print("Too low! Try again.")
                
        elif guess > num_to_guess:
            print("Too high! Try again.")
            
        else:
            print("Congratulations! You've guessed the correct number which is", num_to_guess)
            break
            
        if attempts == max_attempts:
            print("Sorry, you've reached the maximum attempts.")
    
    play_again()

def play_again():
    while True:
        choice = input("Do you want to play again? (y/n) || (yes/no)): ")
        if choice == 'yes' or 'y':
            guessing_game()
        elif choice == 'no' or 'n':
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Please enter 'yes' or 'no'.")

guessing_game()