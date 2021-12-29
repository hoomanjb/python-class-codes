import tkinter as tk
import random

colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Brown', 'Purple']
score = 0
time_left = 30


def start_game(event):
    if time_left == 30:
        count_down()
    ask_color()

def count_down():
    global time_left
    if time_left > 1:
        time_left -= 1
        time_lable.config(text=f'Time left: {time_left}')
        time_lable.after(1000, count_down)

def ask_color():
    global score
    global time_left
    if time_left > 1:
        user_input.focus_set()
        if user_input.get().lower() == colors[1].lower():
            score += 1
        user_input.delete(0, tk.END)
        random.shuffle(colors)
        lable.config(text=str(colors[0]), fg=str(colors[1]))
        score_lable.config(text = f'Score: {score}')

window = tk.Tk()
window.title('COLOR GAME')
window.geometry('450x220')
quide = tk.Label(window, text='Insert color in the box not word text...', font=('arial', 15))
quide.pack()

score_lable = tk.Label(window, text='press enter to start', font=('arial', 15))
score_lable.pack()

time_lable = tk.Label(window, text=f'time left: {time_left}', font=('arial', 15))
time_lable.pack()

lable = tk.Label(window, font=('arial', 15))
lable.pack()

user_input = tk.Entry(window)
window.bind('<Return>', start_game)
user_input.pack()
user_input.focus_set()
window.mainloop()
