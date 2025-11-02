import tkinter as tk
import random

class BrainBattleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🧠 Brain Battle")
        self.root.geometry("500x400")
        self.root.configure(bg="#F3F8FF")

        self.questions = [
            ("What is the capital of France?", ["Paris", "London", "Rome", "Berlin"], "Paris"),
            ("Which planet is known as the Red Planet?", ["Mars", "Earth", "Venus", "Jupiter"], "Mars"),
            ("What is 9 x 9?", ["72", "81", "64", "99"], "81"),
            ("Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Hemingway", "Poe", "Dante"], "Shakespeare"),
            ("What gas do humans need to breathe?", ["Oxygen", "Carbon", "Nitrogen", "Helium"], "Oxygen")
        ]
        random.shuffle(self.questions)
        self.index = 0
        self.score = 0

        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self.root, text="🧠 Brain Battle!", font=("Arial", 20, "bold"), bg="#F3F8FF", fg="#333")
        self.title.pack(pady=20)

        self.question_label = tk.Label(self.root, text="", wraplength=450, font=("Arial", 14), bg="#F3F8FF", fg="#222")
        self.question_label.pack(pady=20)

        self.buttons = []
        for i in range(4):
            btn = tk.Button(self.root, text="", width=30, height=2, bg="#DCE9FF", fg="#000",
                            command=lambda idx=i: self.check_answer(idx))
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, state=tk.DISABLED,
                                     bg="#82C0FF", fg="white", font=("Arial", 12, "bold"))
        self.next_button.pack(pady=10)

        self.score_label = tk.Label(self.root, text="Score: 0", bg="#F3F8FF", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.load_question()

    def load_question(self):
        q, options, _ = self.questions[self.index]
        self.question_label.config(text=q)
        for i, opt in enumerate(options):
            self.buttons[i].config(text=opt, state=tk.NORMAL, bg="#DCE9FF")
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, idx):
        correct_answer = self.questions[self.index][2]
        if self.buttons[idx].cget("text") == correct_answer:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.buttons[idx].config(bg="#A1E6A1")
        else:
            self.buttons[idx].config(bg="#FF9B9B")

        for b in self.buttons:
            b.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.index += 1
        if self.index < len(self.questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        result_text = f"🏁 Game Over!\nYour Score: {self.score}/{len(self.questions)}"
        tk.Label(self.root, text=result_text, font=("Arial", 18, "bold"), bg="#F3F8FF").pack(pady=50)

        tk.Button(self.root, text="Play Again", command=self.restart, bg="#82C0FF", fg="white",
                  font=("Arial", 12, "bold")).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, bg="#FF7070", fg="white",
                  font=("Arial", 12, "bold")).pack(pady=5)

    def restart(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.__init__(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = BrainBattleGame(root)
    root.mainloop()
