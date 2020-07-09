from tkinter import Tk, Entry, Label, StringVar, Button


master = Tk()
master.geometry("320x240")

#input1
Label(master, text = "Number 1:").grid(row = 0, column = 0)
sv_numbere01 = StringVar()
Entry(master, textvariable = sv_numbere01).grid(row = 0, column = 1)

#input2
Label(master, text = "Number 2:").grid(row = 1, column = 0)
sv_numbere02 = StringVar()
Entry(master, textvariable = sv_numbere02).grid(row = 1, column = 1)

#output
sv_result = StringVar()
Label(master, textvariable = sv_result).grid(row = 2, column = 1)


#event
def press():
    number1 = int(sv_numbere01.get())
    number2 = int(sv_numbere02.get())
    sum = number1 + number2
    sv_result.set(sum)
Button(master, text = "Compute", command = press).grid(row = 2, column = 0)

master.mainloop()