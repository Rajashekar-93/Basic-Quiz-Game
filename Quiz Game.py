class QuizQuestion:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer

def ask_question(quiz_question):
    print(quiz_question.question)
    for idx, option in enumerate(quiz_question.options, 1):
        print(f"{idx}. {option}")
    
    user_input = input("Select the correct option (1, 2, 3, ...): ").strip()
    
    if user_input.isdigit() and 1 <= int(user_input) <= len(quiz_question.options):
        selected_option = int(user_input) - 1
        return quiz_question.check_answer(quiz_question.options[selected_option])
    else:
        print("Invalid input! Please enter a number corresponding to the options.")
        return False

def main():
    questions = [
        QuizQuestion("What is the Capital of India?", ["New Delhi", "Mumbai", "Kolkata"], "New Delhi"),
        QuizQuestion("What is the Name of Indian Prime Minister?", ["Narendra Modi", "Rahul Gandhi", "Amit Shah"], "Narendra Modi"),
        QuizQuestion("Where was Charminar Located?", ["Delhi", "Hyderabad", "Mumbai"], "Hyderabad"),
        QuizQuestion("What is Longest River in India?", ["Ganga", "Yamuna", "Godavari"], "Ganga"),
        QuizQuestion("Who is the new World Cricket Champion in T20?", ["India", "England", "Australia"], "India"),  # Updated question
    ]

    score = 0

    for quiz_question in questions:
        if ask_question(quiz_question):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {quiz_question.correct_answer}\n")

    print(f"You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    main()
