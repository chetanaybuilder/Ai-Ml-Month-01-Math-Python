"""Simple knowledge quiz with a polished terminal-style interface.

This script asks two questions, checks the answers, and displays the final score.
It is designed to be easy to read, simple to maintain, and beginner-friendly.
"""

# Importing standard library modules is not required for this script,
# but keeping the program simple ensures clarity for new learners.

# Decorative terminal banner for a more professional user experience.
def print_banner(title):
    """Display a neat banner across the terminal."""
    border = "=" * 60
    print("\n" + border)
    print(f"{title:^60}")
    print(border)


# Display the welcome banner before starting the quiz.
print_banner("PYTHON QUIZ CHALLENGE")
print("Welcome! Test your general knowledge with two quick questions.\n")

# Score starts at zero and increases with each correct answer.
score = 0

# Question 1: Prime Minister of India
answer = input("1) Who is the Prime Minister of India? ")

if answer.strip().lower() == "narendra modi":
    score += 1
    print("Correct! Great start.\n")
else:
    print("Incorrect. The correct answer is Narendra Modi.\n")

# Question 2: Richest person in the world
answer = input("2) Who is the richest person in the world? ")

if answer.strip().lower() == "elon musk":
    score += 1
    print("Correct! Excellent work.\n")
else:
    print("Incorrect. The correct answer is Elon Musk.\n")

# Final score summary after both questions are answered.
print_banner("QUIZ RESULTS")
print(f"You scored {score} out of 2.")

if score == 2:
    print("Outstanding! You answered both questions correctly.")
elif score == 1:
    print("Nice try! One answer was correct.")
else:
    print("Keep practicing - you can do better next time!")

print("\nThank you for playing!\n")
    

    