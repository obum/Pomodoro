from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# --------------------------- DISABLE START BUTTON ----------------------- #
def do_nothing():
    pass


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    tracker_label.config(text="")
    timer_label.config(text="Timer")
    start_button.config(command=start_timer)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text='Break', fg='red')

    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg='pink')

    else:
        count_down(work_secs)
        timer_label.config(text='Work', fg='green')


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = count // 60
    count_secs = count % 60
    if count_mins < 10:
        count_mins = f'0{count_mins}'
    if count_secs < 10:
        count_secs = f'0{count_secs}'
    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_secs}')
    start_button.config(command=do_nothing)
    if count > 0:
        global timer
        timer = window.after(50, count_down, count - 1)
    else:
        start_timer()
        ticks = ''
        work_session = reps // 2
        for i in range(work_session):
            ticks += '🗸'
            tracker_label.config(text=ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
# window.minsize(width=300, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 20, 'bold'))
canvas.grid(row=1, column=1)

# Create Labels

timer_label = Label()
timer_label.config(text='Timer', fg=GREEN, font=(FONT_NAME, 40, 'bold'), bg=YELLOW)
timer_label.grid(row=0, column=1)

tracker_label = Label()
tracker_label.config(fg=GREEN, font=(FONT_NAME, 25, 'bold'), bg=YELLOW)
tracker_label.grid(row=3, column=1)

# Create Buttons

start_button = Button()
start_button.config(text='Start', fg=RED, font=(FONT_NAME, 10, 'bold'), bg=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button()
reset_button.config(text='Reset', fg=RED, font=(FONT_NAME, 10, 'bold'), bg=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
