# Create a program that will accept a multiple choice question, four answers, and the letter of correct answer. 
# This will be six lines, and then store the questions in the file questions.txt.
def save_questions(filename):
    with open(filename, 'w') as file:
        for _ in range(6):
            question = input("Enter the question: ")
            answers = []
            for i in range(4):
                answer = input(f"Enter answer {chr(65 + i)}: ")
                answers.append(answer)
            correct_answer = input("Enter the letter of the correct answer: ")
            file.write(f"{question}\n")
            for i in range(4):
                file.write(f"{chr(65 + i)}. {answers[i]}\n")
            file.write(f"{correct_answer}\n")
            file.write('\n')
        print("Questions saved successfully!")


save_questions("questions.txt")