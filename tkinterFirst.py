import tkinter

window =tkinter.Tk()
window.title("First")
window.minsize(width=500,height=500)

my_label = tkinter.Label(text="It's a label")
my_label.pack()

window.mainloop()