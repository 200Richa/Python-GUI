from tkinter import *
import math
from pygame import mixer

# from turtle_race import *

# ---------------------------- UI FOR THEMES------------------------------- #
theme_window = Tk()
theme_window.title("WALLPAPER")
theme_window.minsize(width=280, height=80)
theme_window.config(bg="#f6eec9")
THEME = 1


def radio_used():
    global THEME
    THEME = radio_state.get()


radio_state = IntVar()
radiobutton1 = Radiobutton(text="CLASSIC", value=1, variable=radio_state, command=radio_used, bg="#f6eec9")
radiobutton2 = Radiobutton(text="WORK", value=2, variable=radio_state, command=radio_used, bg="#f6eec9")
choice = Button(text="   OK   ", bg="blue", width=8, highlightthickness=0, command=theme_window.destroy)
radiobutton1.grid(row=1, column=1)
radiobutton2.grid(row=2, column=1, sticky="w")
choice.grid(row=3, column=2)
theme_window.mainloop()

# ---------------------------- CONSTANTS ------------------------------- #
if THEME == 1:
    SHORT_BREAK_COLOR = "#e2979c"
    LONG_BREAK_COLOR = "#e7305b"
    TIMER_COLOR = "#9bdeac"
    BACKGROUND_COLOR = "#f7f5dd"
    TIMER_TEXT_COLOR = "white"
    WINDOW_PADX = 100
    WINDOW_PADY = 50
    CANVAS_WIDTH = 200
    CANVAS_HEIGHT = 224
    BUTTON_PADX = 10
    BUTTON_PADY = 10
    FILENAME = "tomato.png"
    TEXT_Y = 130
    FONT_NAME = "Chalkboard"

else:
    SHORT_BREAK_COLOR = "#fff76a"
    LONG_BREAK_COLOR = "#ffcc29"
    TIMER_COLOR = "#c0e218"
    BACKGROUND_COLOR = "#06c49b"
    TIMER_TEXT_COLOR = "#ffc478"
    WINDOW_PADX = 30
    WINDOW_PADY = 50
    CANVAS_WIDTH = 308
    CANVAS_HEIGHT = 200
    BUTTON_PADX = 10
    BUTTON_PADY = 0
    FILENAME = "laptop3.png"
    TEXT_Y = 80
    FONT_NAME = "Noteworthy"

WORK_MIN = 0.05
SHORT_BREAK_MIN = 0.05
LONG_BREAK_MIN = 10
reps = 0
timer = None
on = True


# ------------------------------ SOUND ----------------------------------- #
def play():
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load("TF050.WAV")
    # Setting the volume
    mixer.music.set_volume(0.7)
    # Start playing the song
    mixer.music.play()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=TIMER_COLOR)
    check_marks.config(text="")
    global reps
    global on
    reps = 0
    on = True


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global on
    if on:
        on = False
        work_sec = int(WORK_MIN * 60)
        long_break_sec = int(LONG_BREAK_MIN * 60)
        short_break_sec = int(SHORT_BREAK_MIN * 60)
        global reps
        reps += 1
        if reps % 8 == 0:
            title_label.config(text="Break", fg=LONG_BREAK_COLOR)
            count_down(long_break_sec)
            # play_game.grid(column=2, row=5)


        elif reps % 2 == 1:
            # play_game.grid_remove()
            title_label.config(text="Work")
            count_down(work_sec)

        else:
            title_label.config(text="Break", fg=SHORT_BREAK_COLOR)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global on
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        on = True
        play()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=WINDOW_PADX, pady=WINDOW_PADY, bg=BACKGROUND_COLOR)
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
tomato_img = PhotoImage(file=FILENAME)
title_label = Label(text="Timer", fg=TIMER_COLOR, font=(FONT_NAME, 50, "normal"), bg=BACKGROUND_COLOR,)
check_marks = Label(fg=TIMER_COLOR, bg=BACKGROUND_COLOR)
check_marks.grid(column=2, row=4)
title_label.grid(row=1, column=2)
canvas.create_image(int(CANVAS_WIDTH / 2), int(CANVAS_HEIGHT / 2), image=tomato_img)
timer_text = canvas.create_text(int(CANVAS_WIDTH / 2), TEXT_Y, text="00:00", fill=TIMER_TEXT_COLOR,
                                font=(FONT_NAME, 30, "bold"))
canvas.grid(row=2, column=2)
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3, padx=BUTTON_PADX, pady=BUTTON_PADY)
# play_game = Button(text="Play", highlightthickness=0, command=race_game)


window.mainloop()