"""
Simple Quiz Game (English version)
------------------------------------
A small project using Python basics:
- Variables
- Lists and Dictionaries
- Loops (for)
- Functions
- if / else
- Basic Exception Handling (for input validation)
"""

# ---------------------------------------------------------
# STEP 1: Question data — each question is a dictionary
# ---------------------------------------------------------

questions = [
    {
        "question": "Which symbol is used to start a list in Python?",
        "options": ["1. { }", "2. [ ]", "3. ( )", "4. < >"],
        "answer": "2"
    },
    {
        "question": "What is the result of 10 % 3?",
        "options": ["1. 3", "2. 0", "3. 1", "4. 10"],
        "answer": "3"
    },
    {
        "question": "What is a for loop used for?",
        "options": [
            "1. Running code only once",
            "2. Checking a condition",
            "3. Repeating a set number of times or iterating over a list",
            "4. Creating a function",
        ],
        "answer": "3"
    },
    {
        "question": "When does a 'ValueError' occur?",
        "options": [
            "1. When a file is not found",
            "2. When converting data to the wrong type",
            "3. When a list index is out of range",
            "4. When dividing by zero",
        ],
        "answer": "2"
    },
    {
        "question": "How do you get a value from a dictionary?",
        "options": [
            "1. dictionary[index]",
            "2. dictionary.get(index)",
            "3. dictionary[key]",
            "4. dictionary.value()",
        ],
        "answer": "3"
    },
]


# ---------------------------------------------------------
# STEP 2: Function to ask one question and check the answer
# ---------------------------------------------------------

def ask_question(q_number, q_data):
    print(f"\nQuestion {q_number}: {q_data['question']}")
    for option in q_data["options"]:
        print("  " + option)

    # ---- Exception Handling here ----
    # Program should not crash no matter what the user types.
    try:
        user_answer = input("Your answer (1/2/3/4): ").strip()

        if user_answer not in ["1", "2", "3", "4"]:
            raise ValueError("Please enter only 1, 2, 3, or 4.")

    except ValueError as e:
        print(f"Invalid input: {e}")
        return False   # Treat invalid input as a wrong answer

    # Check if the answer is correct
    if user_answer == q_data["answer"]:
        print("Correct! ✅")
        return True
    else:
        print(f"Wrong. The correct answer was: {q_data['answer']}")
        return False


# ---------------------------------------------------------
# STEP 3: Function that runs the whole quiz
# ---------------------------------------------------------

def run_quiz(questions):
    score = 0
    total = len(questions)

    print("=" * 40)
    print("   WELCOME TO THE PYTHON QUIZ!")
    print("=" * 40)

    for i in range(total):
        is_correct = ask_question(i + 1, questions[i])
        if is_correct:
            score += 1

    show_result(score, total)


# ---------------------------------------------------------
# STEP 4: Function to show the final result
# ---------------------------------------------------------

def show_result(score, total):
    percentage = (score / total) * 100

    print("\n" + "=" * 40)
    print(f"Your Score: {score} / {total}  ({percentage:.1f}%)")

    if percentage == 100:
        print("Perfect! No mistakes at all! 🎉")
    elif percentage >= 60:
        print("Good job! But keep practicing. 👍")
    else:
        print("Don't worry, try again! 💪")
    print("=" * 40)


# ---------------------------------------------------------
# STEP 5: Program starts here
# ---------------------------------------------------------

if __name__ == "__main__":
    run_quiz(questions)