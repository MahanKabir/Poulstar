from tkinter import Tk, Entry, Label, Button, StringVar

master = Tk()

Label(master, text = "Name :").grid(row = 0, column = 0)

sv_input = StringVar()
Entry(master, textvariable = sv_input).grid(row = 0, column = 1)
sv_result = StringVar()
Label(master, textvariable = sv_result).grid(row = 1, column = 1 )

def press():
    value = sv_input.get()
    sv_result.set(value)
Button(master, text = "Click Me!", command = press).grid(row = 1, column = 0)


master.mainloop()