import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Game")
        self.master.geometry("500x300")  # Adjusted the window size
        self.master.config(bg="lightcyan")

        self.questions = [
            {"question": "What is the capital of india?", "options": ["Delhi", "Mumbai", "Channai", "Gandinagar"], "correct_option": "Delhi"},
            {"question": "Which planet is known as the Red Planet?", "options": ["Mars", "Venus", "Jupiter", "Saturn"], "correct_option": "Mars"},
            {"question": "What is the largest bird in the world?", "options": ["Emu", "Cassowary", "Ostrich", "Rhea"], "correct_option": "Ostrich"},
        ]

        self.current_question_index = 0
        self.score = 0

        self.label_question = tk.Label(self.master, text="", font=("Arial", 12, "bold"), bg="lightcyan", fg="#333333")  # Changed font family
        self.label_question.pack(pady=10, padx=20, anchor="w")

        self.radio_var = tk.StringVar()
        self.radio_var.set("")

        self.radio_buttons = []
        for i in range(4):
            radio_btn = tk.Radiobutton(self.master, text="", variable=self.radio_var, value="", command=self.check_enable_next, bg="lightcyan", fg="#333333", anchor="w", font=("Arial", 10))  # Changed font family
            radio_btn.pack(anchor="w", padx=20)

            self.radio_buttons.append(radio_btn)

        self.next_button = tk.Button(self.master, text="Next", command=self.next_question, bg="blue", fg="#ffffff", activebackground="#0056b3", activeforeground="darkblue", bd=0, font=("Arial", 10, "bold"), state="disabled")  # Changed font family
        self.next_button.pack(pady=10)

        self.warning_label = tk.Label(self.master, text="", fg="red", bg="lightcyan", font=("Arial", 10))  # Changed font family
        self.warning_label.pack(pady=5)

        self.load_question()

    def load_question(self):
        # Deselect all radio buttons
        self.radio_var.set("")
        self.warning_label.config(text="")
        
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            options = question_data["options"]
            random.shuffle(options)
            for i in range(4):
                self.radio_buttons[i].config(text=options[i], value=options[i])

        else:
            self.show_result()

    def check_enable_next(self):
        # Enable Next button if an option is selected
        if self.radio_var.get():
            self.next_button.config(state="normal")
        else:
            self.next_button.config(state="disabled")

    def select_option(self):
        selected_option = self.radio_var.get()
        correct_option = self.questions[self.current_question_index]["correct_option"]

        if selected_option == correct_option:
            self.score += 1

    def next_question(self): 
        if self.radio_var.get():
            self.select_option()  # Ensure option is selected before proceeding
            self.current_question_index += 1
            self.radio_var.set("")
            self.next_button.config(state="disabled")  # Disable Next button after proceeding

            if self.current_question_index < len(self.questions):
                self.load_question()
            else:
                self.show_result()
        else:
            self.warning_label.config(text="Please select an option before proceeding to the next question.")

    def show_result(self):
        messagebox.showinfo("Quiz Result", f"Your Score: {self.score}/{len(self.questions)}")
        self.master.destroy()

def main():
    root_quiz = tk.Tk()
    quiz_game = QuizGame(root_quiz)
    root_quiz.mainloop()

if __name__ == "__main__":
    main()
