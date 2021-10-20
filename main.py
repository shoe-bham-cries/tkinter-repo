import tkinter as tki

#----------- Creating a new window and configurations---------#
window = tki.Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#----------- Labels---------#
label = tki.Label(text="This is old text")
label.config(text="This is new text")
label.pack()


#----------- Buttons ---------#
def action():
    print("Do something")


# calls action() when pressed
button = tki.Button(text="Click Me", command=action)
button.pack()

#-----------  Entries---------#
entry = tki.Entry(width=30)
# Add some text to begin with
entry.insert(tki.END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.pack()

#----------- Text ---------#
text = tki.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tki.END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", tki.END))
text.pack()


#----------- Spinbox ---------#
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = tki.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


#----------- Scale ---------#
# Called with current scale value.
def scale_used(value):
    print(value)


scale = tki.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#----------- Checkbutton ---------#
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tki.IntVar()
checkbutton = tki.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


#----------- Radiobutton ---------#
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tki.IntVar()
radiobutton1 = tki.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tki.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#----------- Listbox ---------#
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tki.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
#----------- Canvas ---------#
my_img = tki.PhotoImage(file='filepath')
canvas = tki.Canvas(width=210, height=213, highlightthickness=0)
canvas.create_image(xcoor, ycoor, my_img)
canvas.create_text(xcoor, ycoor, text='PlaceHolder')

# Widget inside Canvas
b = ttk.Button(canvas, text='Implode!') 
canvas.create_image(xcoor, ycoor)
