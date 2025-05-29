#array of the sample questions
questions = [
    print("Welcome to the Quiz!"),
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Berlin", "D) Madrid"],
        "answer": "A"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A) CO2", "B) H2O", "C) O2", "D) NaCl"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A) Harper Lee", "B) Mark Twain", "C) F. Scott Fitzgerald", "D) Ernest Hemingway"],
        "answer": "A"
    }]

def run_quiz():
    score = 0
    for q in questions[1:]:  # Skip the welcome message
        print(q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}.\n")
    
    print(f"You scored {score} out of {len(questions) - 1}.")

run_quiz()