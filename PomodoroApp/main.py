from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #


# reset button
def resetOnClick():
    guiWindow.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timerLabel.config(text="Timer")
    checkmark_icon.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# start button
def startOnClick():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timerLabel.config(
            text="Long Break!!",
            font=("Courier", 24, "bold"),
            foreground=RED,
            background=YELLOW,
        )
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timerLabel.config(
            text="Break!",
            font=("Courier", 24, "bold"),
            foreground=PINK,
            background=YELLOW,
        )
    else:
        count_down(work_sec)
        timerLabel.config(
            text="Work Now!",
            font=("Courier", 24, "bold"),
            foreground=GREEN,
            background=YELLOW,
        )


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# Assuming count is defined and represents the initial countdown value
reps = 0
timer = None


# Example initial countdown value
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = f"0{count_sec}"
    elif count_min < 1:
        count_min = f"0{count_min}"
    # To change the item configuration of a canvas element
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = guiWindow.after(1000, count_down, count - 1)
    else:
        startOnClick()
        mark = ""
        for x in range(math.floor(reps / 2)):
            mark += "✔"
        checkmark_icon = Label(
            text=mark, font=(24), foreground=GREEN, background=YELLOW
        )
        checkmark_icon.grid(column=1, row=3)


# ---------------------------- UI SETUP ------------------------------- #
guiWindow = Tk()
guiWindow.title("Pomodoro :)")
guiWindow.config(padx=100, pady=50, background=YELLOW)
# Executes a time delay in ms, and calls a function that we want to call
# guiWindow.after()

timerLabel = Label(
    text="Timer", font=("Courier", 24, "bold"), foreground=GREEN, background=YELLOW
)
timerLabel.grid(column=1, row=0) 

# Canvas widget - layer one on top of other
# The width and height is in pixels
# HIGHLIGHTHICKNESS REMOVES THE BORDER FROM THE IMAGE
canvas = Canvas(width=300, height=300, background=YELLOW, highlightthickness=0)
# read through a file and get hold of image at a location
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(
    150, 175, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=2)
# count_down(count)


start = Button(
    text="Start", width=30, font=("Arial", 15, "normal"), command=startOnClick
)
start.grid(column=0, row=3)

# checkmark
checkmark_icon = Label(fg=GREEN, bg=YELLOW)
checkmark_icon.grid(column=1, row=3)


start = Button(
    text="Reset", width=30, font=("Arial", 15, "normal"), command=resetOnClick
)
start.grid(column=2, row=3)
guiWindow.mainloop()
