import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingApp:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.number_to_guess:
                messagebox.showinfo("Try Again", "Too low! Try again.")
            elif guess > self.number_to_guess:
                messagebox.showinfo("Try Again", "Too high! Try again.")
            else:
                messagebox.showinfo("Success", f"Correct! You guessed it in {self.attempts} attempts.")
                self.master.quit()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberGuessingApp(root)
    root.mainloop()
