from tkinter import *
# by using the import * ability, you remove the need to continually call the tkinter module


def on_button_click():
    # Function triggered when button is clicked
    new_label_text = my_input.get()
    my_label["text"] = new_label_text


def on_other_button_click():
    # Function to save entry into text box to console
    saved_text = my_text.get("1.0", END)
    print(saved_text)


def save_spinbox():
    my_spinbox_num = my_spinbox.get()
    my_label["text"] = my_spinbox_num


def radio_button_used():
    print(radio_state.get())


# Creating the tkinter object
my_window = Tk()
my_window.title("Big GUI Experiment!")
my_window.minsize(width=500, height=500)

"""
Creating a label - Label creation is pretty simple - the important element however is to
"pack" the created label into the created screen.
"""
my_label = Label(text="This is a label!", font=("Arial", 24, "bold"))
my_label.pack()

"""
Creating a button that adjusts the label text upon clicking
The my_button object is created from the tkinter module and calls the Button class.
One of the kwargs associated with the my_button object is the command kwarg.
This is an event listener that calls the on_button_click function when the button is clicked.
The on_button_click in turn changes a kwarg of the my_label object (it changes the label text!)
"""
my_button = Button(text="Click Me!", command=on_button_click)
my_button.pack()

"""
The Entry class is used to create a blank field inviting user input.
Here the input text is set to then be applied to the on_button_click function.
"""
my_input = Entry(width=30)
my_input.insert(END, string="Random helpful words...")
my_input.pack()

""""
Similarly to the Entry class, a Text class allows greater input.
A button is attached which associates to a 2nd function to save any entry in the box to a variable.
This is then printed to the console (see functions at the top!)
"""
my_text = Text(height=10, width=30)
my_text.focus()
my_text.insert(END, "Some more random helpful text....")
my_text.pack()
my_second_button = Button(text="Click to save stuff!", command=on_other_button_click)
my_second_button.pack()

"""
"Spinbox" is the class given to a number clicker widget.
Here I have created a new function to save the number to the label when clicked via the command event listener.
"""
my_spinbox = Spinbox(from_=0, to=99, width=5, command=save_spinbox)
my_spinbox.pack()

"""
Radio buttons with the function associated to save the chosen one to the console.
On these a radio_state variable is attributed to all buttons that saves the state of them (chosen or not)
It is this which is referenced when the function is called.
"""
radio_state = IntVar()
my_first_radiobutton = Radiobutton(text="Don't press one - please!", value=1,
                                   variable=radio_state, command=radio_button_used)
my_second_radiobutton = Radiobutton(text="Don't press this either!", value=2,
                                    variable=radio_state, command=radio_button_used)
my_third_radiobutton = Radiobutton(text="God No! Not this one!", value=3,
                                   variable=radio_state, command=radio_button_used)
my_first_radiobutton.pack()
my_second_radiobutton.pack()
my_third_radiobutton.pack()

# This line of code keeps a referenced tkinter object open so the code doesn't open and close it automatically.
my_window.mainloop()
