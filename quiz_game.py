"""
Simple Quiz Game
-----------------
Python च्या basics concepts वापरून बनवलेला छोटा project:
- Variables
- Lists आणि Dictionaries
- Loops (for)
- Functions
- if / else
- थोडं Exception Handling (input validation साठी)
"""

# ---------------------------------------------------------
# STEP 1: Questions ची data — प्रत्येक question एक dictionary आहे
# ---------------------------------------------------------

questions = [
    {
        "question": "Python मध्ये list सुरू करायला कोणतं symbol वापरतात?",
        "options": ["1. { }", "2. [ ]", "3. ( )", "4. < >"],
        "answer": "2"
    },
    {
        "question": "10 % 3 चं उत्तर काय येईल?",
        "options": ["1. 3", "2. 0", "3. 1", "4. 10"],
        "answer": "3"
    },
    {
        "question": "for loop चा उपयोग कशासाठी होतो?",
        "options": [
            "1. एकदाच code चालवण्यासाठी",
            "2. condition check करण्यासाठी",
            "3. ठराविक वेळा किंवा list वर iterate करण्यासाठी",
            "4. function बनवण्यासाठी",
        ],
        "answer": "3"
    },
    {
        "question": "'ValueError' कधी येते?",
        "options": [
            "1. file सापडली नाही तर",
            "2. चुकीच्या प्रकारचा data convert करायचा प्रयत्न केला तर",
            "3. list index बाहेर गेला तर",
            "4. zero ने भाग दिला तर",
        ],
        "answer": "2"
    },
    {
        "question": "Dictionary मधून value कशी मिळवतात?",
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
# STEP 2: एक question विचारायचं आणि उत्तर बरोबर आहे का ते
# check करायचं function
# ---------------------------------------------------------

def ask_question(q_number, q_data):
    print(f"\nप्रश्न {q_number}: {q_data['question']}")
    for option in q_data["options"]:
        print("  " + option)

    # ---- इथे थोडं Exception Handling ----
    # User ने काहीही टाईप केलं तरी program crash होऊ नये.
    try:
        user_answer = input("तुमचं उत्तर (1/2/3/4): ").strip()

        if user_answer not in ["1", "2", "3", "4"]:
            raise ValueError("कृपया 1, 2, 3 किंवा 4 यापैकीच एक टाका.")

    except ValueError as e:
        print(f"चुकीचा input: {e}")
        return False   # चुकीचा input दिला तर उत्तर चुकीचं मानू

    # उत्तर बरोबर आहे का ते check करा
    if user_answer == q_data["answer"]:
        print("बरोबर! ✅")
        return True
    else:
        print(f"चुकीचं. बरोबर उत्तर होतं: {q_data['answer']}")
        return False


# ---------------------------------------------------------
# STEP 3: संपूर्ण quiz चालवणारं function
# ---------------------------------------------------------

def run_quiz(questions):
    score = 0
    total = len(questions)

    print("=" * 40)
    print("   PYTHON QUIZ मध्ये स्वागत आहे!")
    print("=" * 40)

    for i in range(total):
        is_correct = ask_question(i + 1, questions[i])
        if is_correct:
            score += 1

    show_result(score, total)


# ---------------------------------------------------------
# STEP 4: शेवटी result दाखवणारं function
# ---------------------------------------------------------

def show_result(score, total):
    percentage = (score / total) * 100

    print("\n" + "=" * 40)
    print(f"तुमचा Score: {score} / {total}  ({percentage:.1f}%)")

    if percentage == 100:
        print("Perfect! एकही चूक नाही! 🎉")
    elif percentage >= 60:
        print("छान! पण अजून थोडा सराव करा. 👍")
    else:
        print("काळजी नको, परत प्रयत्न करा! 💪")
    print("=" * 40)


# ---------------------------------------------------------
# STEP 5: Program सुरू
# ---------------------------------------------------------

if __name__ == "__main__":
    run_quiz(questions)