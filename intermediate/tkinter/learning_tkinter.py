from tkinter import *

window = Tk()

window.title("Cetti's Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="A Label", font=("Arial", 24))
my_label.pack()


# Button
def button_clicked():
    my_label.config(text=user_input.get())


button = Button(text="button", command=button_clicked)
button.pack()

# Single line text box
user_input = Entry()
user_input.insert(END, string="Some text here")
user_input.pack()

# Multi-line text box
text = Text(height=5, width=30)
text.focus()

text.insert(END, "Example multi-line entry")
text.pack()


# Spinbox
def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)

spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)

scale.pack()


# Checkbox
def checkbox_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Turn on",
                          variable=checked_state,
                          command=checkbox_used)
checkbutton.pack()


# Radio button
def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1",
                           value=1,
                           variable=radio_state,
                           command=radio_used)
radiobutton2 = Radiobutton(text="Option 2",
                           value=2,
                           variable=radio_state,
                           command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
