from tkinter import *

window = Tk()

window.title("M -> KM")
window.minsize(width=100, height=100)
window.config(padx=20, pady=20)


def calculate():
    miles = int(miles_field.get())
    km = round(miles * 1.609, 2)
    result_label.config(text=km)


# Label
miles_label = Label(text="Miles", font=("Arial", 12))
km_label = Label(text="KM", font=("Arial", 12))
equal_to_label = Label(text="is equal to", font=("Arial", 12))
result_label = Label(text="0", font=("Arial", 12, "bold"))

# Button
calc_button = Button(text="Calculate", command=calculate)

# Entry
miles_field = Entry(width=5)
miles_field.insert(END, string="0")

# Set grid
miles_label.grid(column=2, row=0)
km_label.grid(column=2, row=1)
equal_to_label.grid(column=0, row=1)
result_label.grid(column=1, row=1)
calc_button.grid(column=1, row=2)
miles_field.grid(column=1, row=0)

window.mainloop()
