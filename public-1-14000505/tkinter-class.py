import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk(className='test')
    # window.geometry('400x400')
    # button entry Text Frame
    # greeting = tk.Label(
    #     text='Your Name',
    #     fg='black',
    #     bg='white'
    #     )
    # greeting.pack()
    # button = tk.Button(
    #     text='injaro bezan',
    #     width=20,
    #     height=10,
    #     fg='blue',
    #     bg='red')
    # button.pack()
    # entry = tk.Entry(fg='yellow', bg='blue', width=20)
    # greeting.pack()
    # entry.pack()
    # name = entry.get()
    # entry.delete(0)
    # entry.delete(0, 5)
    # entry.delete(0, tk.END)
    # entry.insert(0, 'hello world')
    # text_box = tk.Text()
    # text_box.insert('1.0', 'hello world')
    # text_box.pack()
    # border_effects = {
    #     'flat': tk.FLAT,
    #     'sunken': tk.SUNKEN,
    #     'raised': tk.RAISED,
    #     'groove': tk.GROOVE,
    #     'ridge': tk.RIDGE
    # }
    #
    # for relief_frame, relief in border_effects.items():
    #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    #     frame.pack(side=tk.LEFT)
    #     lable = tk.Label(master=frame, text=relief_frame)
    #     lable.pack()

    # frame1 = tk.Frame(master=window, width=200, height=100, bg='red')
    # frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # frame2 = tk.Frame(master=window, width=100, height=50, bg='yellow')
    # frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    #
    # frame3 = tk.Frame(master=window, width=50, height=25, bg='blue')
    # frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    # def increase():
    #     value = int(lbl_value["text"])
    #     lbl_value["text"] = f"{value + 1}"
    #
    #
    # def decrease():
    #     value = int(lbl_value["text"])
    #     lbl_value["text"] = f"{value - 1}"
    #
    #
    # window.rowconfigure(0, minsize=50, weight=1)
    # window.columnconfigure([0, 1, 2], minsize=50, weight=1)
    #
    # btn_decrease = tk.Button(master=window, text="-", command=decrease)
    # btn_decrease.grid(row=0, column=0, sticky="nsew")
    #
    # lbl_value = tk.Label(master=window, text="0")
    # lbl_value.grid(row=0, column=1)
    #
    # btn_increase = tk.Button(master=window, text="+", command=increase)
    # btn_increase.grid(row=0, column=2, sticky="nsew")



    # window.mainloop()

    import tkinter as tk
    from tkinter.filedialog import askopenfilename, asksaveasfilename


    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")


    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")


    # window = tk.Tk()
    window.title("Simple Text Editor")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()
