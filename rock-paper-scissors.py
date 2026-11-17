
import random
import time

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
draws = 0

user_wins = 0
computer_wins = 0

game_history = []

print("=" * 40)
print("       ROCK PAPER SCISSORS")
print("=" * 40)

player_name = input("Enter your name: ").strip()

if not player_name:
    player_name = "Player"

print(f"\nWelcome, {player_name}!")

print("\nSelect Difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty = input("Choose difficulty: ").strip()

while difficulty not in ["1", "2", "3"]:
    print("Invalid difficulty!")
    difficulty = input("Choose again: ").strip()

print("\nSelect Game Mode:")
print("1. Best of 3")
print("2. Best of 5")
print("3. Best of 10")
print("4. Endless")

mode = input("Choose mode: ").strip()

while mode not in ["1", "2", "3", "4"]:
    print("Invalid mode!")
    mode = input("Choose again: ").strip()

if mode == "1":
    max_rounds = 3
elif mode == "2":
    max_rounds = 5
elif mode == "3":
    max_rounds = 10
else:
    max_rounds = None

round_number = 0

while True:

    if max_rounds is not None and round_number >= max_rounds:
        break

    round_number += 1

    print("\n" + "-" * 40)
    print(f"ROUND {round_number}")
    print("-" * 40)

    print("Your choices: rock, paper, scissors")

    user = input("Your choice (or quit): ").lower().strip()

    if user == "quit":
        print("You left the game.")
        break

    if user not in choices:
        print("Invalid choice! Try again.")
        round_number -= 1
        continue

    if difficulty == "1":
        computer = random.choice(choices)

    elif difficulty == "2":
        computer = random.choice(choices)

    else:
        if game_history:
            previous_choice = game_history[-1]["user"]

            if previous_choice == "rock":
                computer = "paper"
            elif previous_choice == "paper":
                computer = "scissors"
            else:
                computer = "rock"
        else:
            computer = random.choice(choices)

    print("\nComputer is thinking...")
    time.sleep(1)

    print("\nYour choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("It's a draw!")
        draws += 1
        result = "Draw"

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print(f"{player_name} wins this round!")
        user_score += 1
        user_wins += 1
        result = "Win"

    else:
        print("Computer wins this round!")
        computer_score += 1
        computer_wins += 1
        result = "Loss"

    game_history.append({
        "round": round_number,
        "user": user,
        "computer": computer,
        "result": result
    })

    print("\nSCOREBOARD")
    print("-" * 30)
    print(f"{player_name}: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Draws: {draws}")

    if max_rounds is not None:
        if user_score > max_rounds // 2:
            break
        if computer_score > max_rounds // 2:
            break

print("\n" + "=" * 40)
print("          FINAL RESULTS")
print("=" * 40)

print(f"Player: {player_name}")
print(f"Total rounds: {round_number}")
print(f"Your wins: {user_wins}")
print(f"Computer wins: {computer_wins}")
print(f"Draws: {draws}")

if user_score > computer_score:
    print(f"\nCongratulations {player_name}! You won the game!")

elif user_score < computer_score:
    print("\nComputer won the game!")

else:
    print("\nThe game ended in a tie!")

total_games = user_wins + computer_wins + draws

if total_games > 0:
    win_rate = (user_wins / total_games) * 100
    print(f"Your win rate: {win_rate:.2f}%")

print("\nGAME HISTORY")
print("-" * 40)

for game in game_history:
    print(
        f"Round {game['round']}: "
        f"{game['user']} vs {game['computer']} "
        f"-> {game['result']}"
    )

print("\nThanks for playing!")
