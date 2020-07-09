from tkinter import Tk, Entry, Label, Button, StringVar

master = Tk()
Label(master, text = "Calculate :").grid(row = 0, column = 0)

sv_input = StringVar()
Entry(master, textvariable = sv_input).grid(row = 0, column = 1)

def btn_sum():
    value = sv_input.get()
    number = value.split("+")
    sum = int(number[0]) + int(number[1])
    sv_result.set(sum)

Button(master, text = "=", command = btn_sum).grid(row = 1, column = 0)
sv_result = StringVar()
Label(master, textvariable = sv_result).grid(row = 1, column = 1)

master.mainloop()

