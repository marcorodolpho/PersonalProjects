#This is the first project to learn new habilities

import tkinter

app = tkinter.Tk()

app.title = ("My calculator")

entry1 = tkinter.Entry(app)
entry1.pack()

entry2 = tkinter.Entry()
entry2.pack()

_sum_button = tkinter.Button(app, text="Soma")
_sum_button.pack()

sub_button = tkinter.Button(app, text="Sub")
sub_button.pack()

mult_button = tkinter.Button(app, text="Mult")
mult_button.pack()

divd_button = tkinter.Button(app, text="Divd")
divd_button.pack()

result_button = tkinter.Button(app, text="Igual")
result_button.pack()

app.mainloop()