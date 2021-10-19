import tkinter as tki

window = tki.Tk()
window.title("Mile to KM Converter")
window.minsize(width=100, height=100)

label1 = tki.Label(text="Miles")
label1.grid(column=3, row=1)

label2 = tki.Label(text="is equal to")
label2.grid(column=1, row=2)

label3 = tki.Label(text=" ")
label3.grid(column=2, row=2, padx=25, pady=25)

label4 = tki.Label(text="kilometers.")
label4.grid(column=3, row=2)


def convert():
    kms = float(entry.get())*1.609
    label3.config(text=str(kms))


button = tki.Button(text="Calculate", command=convert)
button.grid(column=2, row=3, padx=25, pady=25)

entry = tki.Entry(width=10)
entry.insert(tki.END, string="")
entry.grid(column=2, row=1)
window.mainloop()
