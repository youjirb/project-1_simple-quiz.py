questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Jupiter", "C. Venus", "D. Saturn"],
        "answer": "A"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Ribosome", "C. Mitochondria", "D. Chloroplast"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Gorilla"],
        "answer": "B"
    },
    {
        "question": "Which of the following is not a primary color?",
        "options": ["A. Red", "B. Yellow", "C. Green", "D. Black"],
        "answer": "D"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. J.K. Rowling", "C. Ernest Hemingway", "D. F. Scott Fitzgerald"],
        "answer": "A"
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["A. Venus", "B. Mars", "C. Mercury", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. Wo", "B. Wt", "C. H2O", "D. Wa"],
        "answer": "C"
    },
    {
        "question": "Who is known as the father of modern physics?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["A. Au", "B. Ag", "C. Gd", "D. AuBr"],
        "answer": "A"
    },
    {
        "question": "Which famous artist painted the Mona Lisa?",
        "options": ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Michelangelo"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Beijing", "B. Tokyo", "C. Seoul", "D. Bangkok"],
        "answer": "B"
    },
    {
        "question": "Which gas is most abundant in Earth's atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"],
        "answer": "B"
    },
]

def ask_question(question_dict):
    print(question_dict["question"])
    for option in question_dict["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    return user_answer

def check_answer(question_dict, user_answer):
    return user_answer == question_dict["answer"]

def main():
    print("Welcome to the Multiple Choice Quiz!")
    num_questions = len(questions)
    score = 0

    for question in questions:
        user_answer = ask_question(question)
        if check_answer(question, user_answer):
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])

    print(f"\nYou got {score} out of {num_questions} questions correct.\nYou got {(score/num_questions)*100}%a")

if __name__ == "__main__":
    main()
