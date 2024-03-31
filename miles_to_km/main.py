from tkinter import *

# window and config
window = Tk()
window.title("Miles to Kilometers")
window.config(padx=20, pady=20)

# input miles
miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

# miles label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# equal to label
equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

# km value label
km_value = Label(text="0")
km_value.grid(row=1, column=1)

# km label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)


# calculate button
def calculate():
    miles_to_km = round(int(miles_input.get()) * 1.60934)
    km_value.config(text=miles_to_km)


calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(row=2, column=1)

# mainloop
window.mainloop()
