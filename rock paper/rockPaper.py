import random
def play_game():
    user=input("Enter your choice (rock, paper, scissors): ").lower()
    computer=random.choice(["rock", "paper", "scissors"])
    if user==computer:
        return "It's a tie!"
    if is_winner(user, computer):
        return "You win!"
    return "You lose!"
def is_winner(player, opponent):
    if (player == "rock" and opponent == "scissors") or \
       (player == "paper" and opponent == "rock") or \
       (player == "scissors" and opponent == "paper"):
        return True
    return False
print(play_game())