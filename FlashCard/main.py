from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOUR = "#B1DDC6"

# -----------------------------------------READ DATA----------------------------------------------#
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    data = original_data.to_dict(orient="records")
else:
    data = data.to_dict(orient="records")


def next_word():
    global word_set, flip_timer
    word_set = random.choice(data)
    window.after_cancel(flip_timer)
    random_french = word_set["French"]
    canvas.itemconfig(image_item, image=card_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(text_item, text=random_french, fill="black")
    flip_timer = window.after(3000, flip)


def flip():
    global word_set
    canvas.itemconfig(image_item, image=card_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(text_item, text=word_set["English"], fill="white")


def is_known():
    data.remove(word_set)
    to_learn = pandas.DataFrame(data)
    to_learn.to_csv("words_to_learn.csv", index=False)
    next_word()

# --------------------------------------------GUI SETUP---------------------------------------------#
window = Tk()
window.minsize(width=900, height=600)
window.title("Flashy")
window.config(bg=BACKGROUND_COLOUR, padx=50, pady=50)

flip_timer = window.after(3000, next_word)
card_front = PhotoImage(file="card_front.png")
card_back = PhotoImage(file="card_back.png")
right_image = PhotoImage(file="right.png")
wrong_image = PhotoImage(file="wrong.png")
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOUR, highlightthickness=0)

image_item = canvas.create_image(400, int(526 / 2), image=card_front)
language = canvas.create_text(400, int(526 / 4), text="Language", font=("Arial", 50, "italic"))
text_item = canvas.create_text(400, int(526 / 2), text="Word", font=("Arial", 50, "bold"))

right = Button(image=right_image, highlightthickness=0, command=is_known)
wrong = Button(image=wrong_image, highlightthickness=0, command=next_word)
canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
right.grid(row=1, column=0)
wrong.grid(row=1, column=1)
next_word()

window.mainloop()
