
from tkinter import *
from random import choice
import time

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("450x525")
        self.root.configure(bg="Aqua")

        self.sentences = [
            "The quick red fox jumps over the lazy dog showcasing its agility and speed in a timeless display of nature's prowess.",
            "Pack my box with seven dozen liquor jugs, carefully arranging each item to maximize space and ensure safe transport.",
            "Six big devils from Greece quickly forgot how to fox-trot, their once-refined skill devolving into chaos and confusion."
        ]

        self.create_widgets()
        self.reset()

    def create_widgets(self):
        Label(self.root, text="Here is your Sentence:", bg="Aqua", font=("Times", 12, "bold italic")).place(x=15, y=10)

        self.text1 = Text(self.root, height=4, width=52, wrap=WORD)
        self.text1.place(x=15, y=40)
        self.text1.config(state=DISABLED)  # Make sample text readonly

        Label(self.root, text="Type the above Sentence:", bg="Aqua", font=("Times", 12, "bold italic")).place(x=15, y=120)

        self.text2 = Text(self.root, height=4, width=52, wrap=WORD)
        self.text2.place(x=15, y=150)

        Button(self.root, text="Check Result", bg="lightgreen", font=("Times", 10, "bold italic"),
               relief="raised", command=self.calculate).place(x=140, y=230)

        Label(self.root, text="Results:", bg="Aqua", font=("Times", 12, "bold italic")).place(x=25, y=260)

        self.text3 = Text(self.root, height=6, width=52, wrap=WORD)
        self.text3.place(x=15, y=285)
        self.text3.config(state=DISABLED)  # Make result text readonly

        Button(self.root, text="RESET", width=10, bg="orange", font=("Times", 10, "bold italic"),
               relief="raised", command=self.reset).place(x=160, y=390)

    def reset(self):
        """Resets the test with a new sentence."""
        self.text1.config(state=NORMAL)
        self.text1.delete("1.0", END)
        self.sample = choice(self.sentences)
        self.text1.insert(END, self.sample)
        self.text1.config(state=DISABLED)

        self.text2.delete("1.0", END)

        self.text3.config(state=NORMAL)
        self.text3.delete("1.0", END)
        self.text3.config(state=DISABLED)

        self.start_time = time.time()

    def calculate(self):
        """Calculates typing speed and accuracy."""
        end_time = time.time()
        time_taken = end_time - self.start_time

        user_text = self.text2.get("1.0", END).strip()
        typed_chars = len(user_text)
        correct_chars = sum(1 for i in range(min(len(user_text), len(self.sample))) if user_text[i] == self.sample[i])

        time_in_min = time_taken / 60
        GWPM = (typed_chars / 5) / time_in_min if time_in_min > 0 else 0
        NWPM = (correct_chars / 5) / time_in_min if time_in_min > 0 else 0
        Accuracy = (NWPM * 100 / GWPM) if GWPM > 0 else 0

        result = f"Total typed characters: {typed_chars}\n" \
                 f"Correct typed characters: {correct_chars}\n" \
                 f"Incorrect typed characters: {typed_chars - correct_chars}\n" \
                 f"Time taken: {round(time_taken, 2)} sec\n" \
                 f"Accuracy: {round(Accuracy, 2)}%\n" \
                 f"Typing speed: {round(NWPM, 2)} WPM"

        self.text3.config(state=NORMAL)
        self.text3.delete("1.0", END)
        self.text3.insert("1.0", result)
        self.text3.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    SpeedTypingTest(root)
    root.mainloop()
