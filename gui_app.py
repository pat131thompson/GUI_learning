from tkinter import *

my_gui_window = Tk()
my_gui_window.title("Llbs to KG Converter")
my_gui_window.minsize(width=200, height=200)


def button_clicked():
    user_input = float(entry_box.get())
    result = round(user_input / 2.2, 2)
    results_label["text"] = result


# Top
entry_box = Entry(width=10)
entry_box.insert(END, string="0")
entry_box.grid(column=1, row=0)
llbs_label = Label(text="Llbs")
llbs_label.grid(column=2, row=0)
llbs_label.config(padx=20, pady=20)

# Middle
text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)
text_label.config(padx=10, pady=10)
results_label = Label(text="??")
results_label.grid(column=1, row=1)
text_label_two = Label(text="KG")
text_label_two.grid(column=2, row=1)

# Bottom
main_button = Button(text="Convert", command=button_clicked)
main_button.grid(column=1, row=2)
main_button.config(pady=10)

my_gui_window.mainloop()
