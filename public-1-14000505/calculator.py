import tkinter as tk


def btn_click(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator) # 1 + 2


def btn_clear_display():
    global operator
    operator = ''
    text_input.set('')


def btn_equal_input():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ''

cal = tk.Tk()
cal.title("CALCULATOR")
operator = ''
text_input = tk.StringVar()

text_display = tk.Entry(
    cal, font=('arial', 20, 'bold'), textvariable=text_input,
    bd=30, insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)
# -------------------------------------
btn_clear = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='C', bg='powder blue', command=btn_clear_display).grid(column=0, row=1)

btn_m = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='M', bg='powder blue').grid(column=1, row=1)

btn_bracket1 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='(', bg='powder blue', command=lambda: btn_click('(')).grid(column=2, row=1)

btn_bracket2 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text=')', bg='powder blue', command=lambda: btn_click(')')).grid(column=3, row=1)
# ----------------------------------------------------
btn_7 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='7', bg='powder blue', command=lambda: btn_click('7')).grid(column=0, row=2)

btn_8 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='8', bg='powder blue', command=lambda: btn_click('8')).grid(column=1, row=2)

btn_9 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='9', bg='powder blue', command=lambda: btn_click('9')).grid(column=2, row=2)

btn_divide = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='/', bg='powder blue', command=lambda: btn_click('/')).grid(column=3, row=2)
# -------------------------------------------------
btn_4 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='4', bg='powder blue', command=lambda: btn_click('4')).grid(column=0, row=3)

btn_5 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='5', bg='powder blue', command=lambda: btn_click('5')).grid(column=1, row=3)

btn_6 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='6', bg='powder blue', command=lambda: btn_click('6')).grid(column=2, row=3)

btn_sub = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='-', bg='powder blue', command=lambda: btn_click('-')).grid(column=3, row=3)
# ----------------------------------------------
btn_1 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='1', bg='powder blue', command=lambda: btn_click('1')).grid(column=0, row=4)

btn_2 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='2', bg='powder blue', command=lambda: btn_click('2')).grid(column=1, row=4)

btn_3 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='3', bg='powder blue', command=lambda: btn_click('3')).grid(column=2, row=4)

btn_multy = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='*', bg='powder blue', command=lambda: btn_click('*')).grid(column=3, row=4)
# --------------------------------------
btn_0 = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='0', bg='powder blue', command=lambda: btn_click('0')).grid(column=0, row=5)

btn_dot = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='.', bg='powder blue', command=lambda: btn_click('.')).grid(column=1, row=5)

btn_equal = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='=', bg='powder blue', command=btn_equal_input).grid(column=2, row=5)

btn_add = tk.Button(
    cal, padx=16, pady=16, bd=8, fg='black', font=('arial', 20, 'bold'),
    text='+', bg='powder blue', command=lambda: btn_click('+')).grid(column=3, row=5)

cal.mainloop()