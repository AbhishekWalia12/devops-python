from tkinter import *

window = Tk()
window.title("First")
window.minsize(width=500,height=500)

my_label = Label(text="It's a label")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New Text")


def button_clicked():
    print("Button got clicked")
    my_label.config(text="Button got clicked")


button = Button(text="Click Here", command=button_clicked)
button.pack()


window.mainloop()