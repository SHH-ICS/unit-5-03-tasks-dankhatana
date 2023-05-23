# Create a second program that will read the file questions.txt, formatted as described above, and pose the questions to the user. 
# The program will keep score of the number of questions answered correctly.
def load_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 7):
            question = lines[i].strip()
            answers = [lines[i + j].strip() for j in range(1, 5)]
            correct_answer = lines[i + 5].strip()
            questions.append((question, answers, correct_answer))
    return questions


def pose_questions(questions):
    score = 0
    for i, (question, answers, correct_answer) in enumerate(questions, 1):
        print(f"Question {i}:")
        print(question)
        for j, answer in enumerate(answers):
            print(f"{chr(65 + j)}. {answer}")
        user_answer = input("Your answer (enter the letter): ").upper()
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
        print()
    print(f"You scored {score}/{len(questions)}.")


questions = load_questions("questions.txt")
pose_questions(questions)
