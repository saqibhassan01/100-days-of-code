import random

class Game:
    def __init__(self, hint_text, difficulty, score=0):
        self.hint_text = hint_text
        self.difficulty = difficulty
        self.score = score
        self.number = random.randint(0, 99)
        self.tries = 0
        self.guess = 0
        self.difficulty_tries = {
            "easy": 10,
            "medium": 7,
            "hard": 5
        }
    def hint(self):
        hint_number = 3
        if hint_number == 1:
            if self.number % 2 == 0:
                self.hint_text = ("The number is divisible by 2")
            elif self.number % 2 != 0:
                self.hint_text = ("The number is not divisible by 2")
        elif hint_number == 2:
            if self.number <= 20:
                self.hint_text = ("The number is less then 20")
            elif self.number > 20 and self.number < 40:
                self.hint_text = ("The number is greater then 20 and less then 40")
            elif self.number >= 40 and self.number < 60:
                self.hint_text = ("The number is greater then 40 and less then 60")
            elif self.number >= 60 and self.number < 80:
                self.hint_text = ("The number is greater then 60 and less then 80")
            else:
                self.hint_text = ("The number is greater then 80 and less then 100")
        elif hint_number == 3 and self.number >= 10:
            last_digit = self.number % 10
            self.hint_text = (f"The last digit of the number is {last_digit}")
    # Method to start the main menu of the game
    def main_menu(self):
        self.hint()
        print("Welcome to Guess the Number Game")
        while True:
            # Getting the user's choice of difficulty
            difficulty = input("Choose the difficulty\n1. Easy\n2. Medium\n3. Hard\nYour Choice: ").lower()
            # Setting the number of tries based on the chosen difficulty
            if difficulty in self.difficulty_tries:
                self.difficulty = difficulty
                self.tries = self.difficulty_tries[difficulty]  # Set the number of tries based on difficulty
                break
            else:
                print("Invalid Input") 
        # Main game loop
        while self.tries > 0:
            print(f"Score: {self.score}")
            print(f"Tries Left: {self.tries}")
            print("Need Hint? Type 'h' or 'hint'")
            guess = input("Guess the number: ")
            if guess == "h" or guess == "hint":
                self.tries +=1
                print(self.hint_text)
            else:
                guess = int(guess)
                if guess > self.number:
                    print("Too High")
                elif guess < self.number:
                    print("Too Low")
                else:
                    print(f"Congratulations! You guessed the correct number.")
                    self.score += 1  # Increasing the player's score by 1
                    print(f"Score: {self.score}")  # Displaying the updated score
                    self.tries = self.difficulty_tries[self.difficulty]  # Resetting the number of tries to the chosen difficulty
                    self.hint()

            self.tries -= 1  # Decrementing the number of tries

        # Player is out of tries
        print(f"Out of tries. The correct number was {self.number}")

# Creating an instance of the Game class to initialize the game
game = Game("Guess the number", "easy")

# Calling the main_menu method to start the game
game.main_menu()