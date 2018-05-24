import tkinter as tk

#This window has the properties of all the stuff in Tkinter
window = tk.Tk()

#This sets the name ontop of the window
window.title('My app')

#This sets the window to the size you want
window.geometry("400x400")

#label
title = tk.Label(text="Hello world. Welcome to CS50 and welcome to my app", font=("Times New Roman", 20))
title.grid()

#button
button1 = tk.Button(text = "Click me!", bg='red')
button1.grid()

#entry field
entry_field1 = tk.Entry()
entry_field1.grid()

# text field
text_field = tk.Text(master=window, height=10, width=30)
text_field.grid()

#mainloop runs everything inside the window
window.mainloop()
