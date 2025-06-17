# 12.	Build a Mini Quiz Game using Functions
# 	Use a function ask_question(question, correct_answer)
# 	Ask 3–5 questions and return score at the end


def question(question, correct_answer):
    answer = input(question + " ")
    if answer.strip().lower() == correct_answer.lower():
        print(" Correct!\n")
        return 1
    else:
        print(f" Wrong! The correct answer is: {correct_answer}\n")
        return 0

def game():
    print(" Welcome to the Mini Quiz Game! \n ")
    score = 0

    score += question("1. What is the capital of India?", "New Delhi")
    score += question("2. What is 5 + 7?", "12")
    score += question("3. What color do you get when you mix red and white?", "Pink")
    score += question("4. Who wrote 'Harry Potter'?", "J.K. Rowling")
    score += question("5. What is the boiling point of water (in Celsius)?", "100")

    print(f" Quiz Over! Your final score: {score} / 5")


game()
