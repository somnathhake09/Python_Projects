# Step 1: Knowledge base - Python related questions
questions = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Which data type is used to store multiple items in a single variable and is ordered and changeable?",
        "options": ["A. Tuple", "B. Set", "C. List", "D. Dictionary"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(type(5))",
        "options": ["A. <class 'str'>", "B. <class 'int'>", "C. <class 'float'>", "D. <class 'bool'>"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "Which loop is used when you don't know the number of iterations in advance?",
        "options": ["A. for", "B. while", "C. do-while", "D. repeat"],
        "answer": "B"
    }
]

# Step 2: Function to ask a single question
def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()
    
    if user_answer == question_data["answer"]:
        print("Correct!")
        return True
    else:
        print(f"Wrong! Correct answer was: {question_data['answer']}")
        return False

# Step 3: Function to run the full quiz
def run_quiz(question_list):
    score = 0
    total = len(question_list)
    
    for question_data in question_list:
        result = ask_question(question_data)
        if result:
            score += 1
        print("-" * 30)   # ek line taaki questions alag dikhein
    
    print(f"Quiz over! Your score: {score}/{total}")

run_quiz(questions)