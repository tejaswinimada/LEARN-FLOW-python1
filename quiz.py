import random

class QuizGame:
    def __init__(self, questions, answers, difficulty_levels):
        self.questions = questions
        self.answers = answers
        self.difficulty_levels = difficulty_levels
        self.score = 0

    def display_menu(self):
        print("Welcome to the Quiz Game!")
        print("1. Start Quiz")
        print("2. Quit")

    def start_game(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2): ")

            if choice == "1":
                self.play_quiz()
            elif choice == "2":
                print("Thanks for playing! Your final score is:", self.score)
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")

    def play_quiz(self):
        difficulty = self.select_difficulty()
        available_questions = [q for q, d in zip(self.questions, self.difficulty_levels) if d <= difficulty]
        random.shuffle(available_questions)

        for question in available_questions:
            print("\n" + question)
            user_answer = input("Your answer: ").strip().lower()

            if user_answer == self.answers[question].lower():
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect. The correct answer is:", self.answers[question])

        print("\nQuiz completed! Your final score is:", self.score)

    def select_difficulty(self):
        print("\nSelect Difficulty Level:")
        for i, level in enumerate(self.difficulty_levels, start=1):
            print(f"{i}. {level}")

        while True:
            try:
                choice = int(input("Enter the number corresponding to your choice: "))
                if 1 <= choice <= len(self.difficulty_levels):
                    return self.difficulty_levels[choice - 1]
                else:
                    print("Invalid choice. Please enter a number between 1 and", len(self.difficulty_levels))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

# Example usage:
questions = ["What is the capital of France?", "Who wrote Romeo and Juliet?", "What is the largest mammal?"]
answers = {"What is the capital of France?": "Paris", "Who wrote Romeo and Juliet?": "William Shakespeare", "What is the largest mammal?": "Blue Whale"}
difficulty_levels = ["Easy", "Medium", "Hard"]

quiz_game = QuizGame(questions, answers, difficulty_levels)
quiz_game.start_game()
