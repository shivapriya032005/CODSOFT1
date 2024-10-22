import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock-Paper-Scissors Game")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f8ff")  # Light blue background

        self.user_score = 0
        self.computer_score = 0

        # Title Label
        self.title_label = tk.Label(master, text="Rock, Paper, Scissors", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333333")
        self.title_label.pack(pady=20)

        # Instructions Label
        self.instructions_label = tk.Label(master, text="Choose Rock, Paper, or Scissors:", font=("Helvetica", 16, "bold"), bg="#f0f8ff")
        self.instructions_label.pack(pady=10)

        # Result Label
        self.result_label = tk.Label(master, text="", font=("Helvetica", 14), bg="#f0f8ff", fg="#ff5722")
        self.result_label.pack(pady=10)

        # Score Label
        self.score_label = tk.Label(master, text=f"Score - You: {self.user_score} | Computer: {self.computer_score}", font=("Helvetica", 14), bg="#f0f8ff", fg="#4caf50")
        self.score_label.pack(pady=10)

        # Buttons Frame
        self.buttons_frame = tk.Frame(master, bg="#f0f8ff")
        self.buttons_frame.pack(pady=20)

        # Button styles
        button_font = ("Helvetica", 12, "bold")
        button_width = 10
        button_height = 2

        # Rock button
        self.rock_button = tk.Button(
            self.buttons_frame, text="Rock", command=lambda: self.play("rock"),
            bg="#2196f3", fg="white", font=button_font, width=button_width, height=button_height
        )
        self.rock_button.grid(row=0, column=0, padx=10, pady=5)

        # Paper button
        self.paper_button = tk.Button(
            self.buttons_frame, text="Paper", command=lambda: self.play("paper"),
            bg="#4caf50", fg="white", font=button_font, width=button_width, height=button_height
        )
        self.paper_button.grid(row=0, column=1, padx=10, pady=5)

        # Scissors button
        self.scissors_button = tk.Button(
            self.buttons_frame, text="Scissors", command=lambda: self.play("scissors"),
            bg="#ff9800", fg="white", font=button_font, width=button_width, height=button_height
        )
        self.scissors_button.grid(row=0, column=2, padx=10, pady=5)

        # Play Again Button (initially disabled)
        self.play_again_button = tk.Button(
            master, text="Play Again", command=self.reset_game, state=tk.DISABLED,
            bg="#e0e0e0", fg="white", font=button_font, width=button_width, height=button_height
        )
        self.play_again_button.pack(pady=20)

    def play(self, user_choice):
        """Main gameplay function"""
        computer_choice = random.choice(["rock", "paper", "scissors"])
        result = ""

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        # Update the result and score labels
        self.result_label.config(
            text=f"You chose {user_choice}, Computer chose {computer_choice}. {result}",
            fg="#ff5722" if result == "You lose!" else "#4caf50"
        )
        self.score_label.config(
            text=f"Score - You: {self.user_score} | Computer: {self.computer_score}"
        )

        # Disable buttons and enable "Play Again" button
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)
        self.play_again_button.config(state=tk.NORMAL, bg="#ff5722")

    def reset_game(self):
        """Reset the game for a new round without resetting scores"""
        # Clear result label
        self.result_label.config(text="")

        # Re-enable buttons
        self.rock_button.config(state=tk.NORMAL)
        self.paper_button.config(state=tk.NORMAL)
        self.scissors_button.config(state=tk.NORMAL)
        self.play_again_button.config(state=tk.DISABLED, bg="#e0e0e0")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
