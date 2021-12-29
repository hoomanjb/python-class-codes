import random
import tkinter as tk

window = tk.Tk()

window.geometry('400x300')

window.title('Rock Paper Scissors Game')

user_score = 0
ai_score = 0
gl_user_choice = ''
gl_ai_choice = ''


def choice_to_number(choice):
    my_dict = {'rock': 0, 'paper': 1, 'scissor': 2}
    return my_dict[choice]


def number_to_choice(number):
    my_dict = {0: 'rock', 1: 'paper', 2: 'scissor'}
    return my_dict[number]


def ai_choosing():
    return random.choice(['rock', 'paper', 'scissor'])


def show_result(user_choice, ai_choice):
    global user_score
    global ai_score
    user = choice_to_number(user_choice)
    ai = choice_to_number(ai_choice)
    if user == ai:
        print('Mosavi!!!')
    elif user > ai:
        print('You WIN...')
        user_score += 1
    else:
        print('AI Wins...')
        ai_score += 1
    text_area = tk.Text(master=window, height=15, width=35)
    text_area.grid(column=0, row=4)
    result_text = f"""
    Your choice is {user_choice} and ai choice is {ai_choice},
    your score is {user_score} and ai score is {ai_score}"""
    text_area.insert(tk.END, result_text)

def rock():
    global gl_user_choice
    global gl_ai_choice
    gl_user_choice = 'rock'
    gl_ai_choice = ai_choosing()
    show_result(gl_user_choice, gl_ai_choice)

def paper():
    global gl_user_choice
    global gl_ai_choice
    gl_user_choice = 'paper'
    gl_ai_choice = ai_choosing()
    show_result(gl_user_choice, gl_ai_choice)

def scissor():
    global gl_user_choice
    global gl_ai_choice
    gl_user_choice = 'scissor'
    gl_ai_choice = ai_choosing()
    show_result(gl_user_choice, gl_ai_choice)


rock_button = tk.Button(text="   ROCK   ", bg='skyblue', width=10, command=rock).grid(column=0, row=1)
paper_button = tk.Button(text="   PAPER   ", bg='pink', width=10, command=paper).grid(column=0, row=2)
scissor_button = tk.Button(text="   SCISSOR   ", bg='lightgreen', width=10, command=scissor).grid(column=0, row=3)


window.mainloop()

