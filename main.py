from tkinter import *

# window
window = Tk()
window.title('Miles to Kilometer Converter')
window.minsize(width=600, height=400)
window.config(padx=20, pady=20)

# GUI functionality
CONVERSION = 1.609


def button_clicked():
    user_input = entry.get()
    convert_km = round(float(user_input) * CONVERSION, 2)
    text_0.config(text=convert_km)




# Entry
entry = Entry()
entry.grid(column=1, row=0)

# Label
miles = Label(text='m', font=('arial', 15))
miles.grid(column=2, row=0)

# text is equal to
is_equal_to = Label(text='is equal to', font=('arial', 15))
is_equal_to.grid(column=0, row=1)

# Text 0
text_0 = Label(text='0', font=('arial', 15))
text_0.grid(column=1, row=1)

# km
km = Label(text='km', font=('arial', 15))
km.grid(column=2, row=1)

# Button
button = Button(text='Calculate', font=('arial', 15), command=button_clicked)
button.grid(column=1, row=2)




window.mainloop()
