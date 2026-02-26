import random
import os

HIGH_SCORE_FILE = "high_score.txt"


def load_high_score():
    """Load high score from file."""
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, "r") as file:
            return int(file.read())
    return None


def save_high_score(score):
    """Save new high score to file."""
    with open(HIGH_SCORE_FILE, "w") as file:
        file.write(str(score))


def choose_difficulty():
    """Allow user to choose difficulty level."""
    print("\nChoose Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")

    while True:
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def play_game():
    """Main game logic."""
    max_number, attempts_left = choose_difficulty()
    secret_number = random.randint(1, max_number)
    attempts_used = 0

    print(f"\nI'm thinking of a number between 1 and {max_number}.")

    while attempts_left > 0:
        try:
            guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts_used += 1
        attempts_left -= 1

        if guess < secret_number:
            print("Too low! 📉")
        elif guess > secret_number:
            print("Too high! 📈")
        else:
            print(f"\n🎉 Congratulations! You guessed it in {attempts_used} attempts!")
            return attempts_used

    print(f"\n💥 Game Over! The number was {secret_number}.")
    return None


def main():
    """Run the game and handle high score."""
    print("=== Welcome to the Number Guessing Game ===")

    high_score = load_high_score()
    if high_score:
        print(f"🏆 Current High Score: {high_score} attempts")

    result = play_game()

    if result:
        if high_score is None or result < high_score:
            print("🔥 New High Score!")
            save_high_score(result)

    print("\nThanks for playing!")


if __name__ == "__main__":
    main()
