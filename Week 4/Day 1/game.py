import random

class Game:

    def get_user_item(self):
        while True:
            choice = input("Choose rock, paper, or scissors: ").lower()
            if choice in ["rock", "paper", "scissors"]:
                return choice
            else:
                print("Invalid choice, try again.")

    def get_computer_item(self):
        return random.choice(["rock", "paper", "scissors"])

    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"

        if (user_item == "rock" and computer_item == "scissors") or \
           (user_item == "paper" and computer_item == "rock") or \
           (user_item == "scissors" and computer_item == "paper"):
            return "win"

        return "loss"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"Computer chose: {computer_item}")

        if result == "win":
            print("You win!")
        elif result == "loss":
            print("You lose!")
        else:
            print("It's a draw!")

        return result