import tkinter as tk
data = {
    "A":"._",
    "B":"_...",
    "C":"_._.",
    "D":"_..",
    "E":".",
    "F":".._.",
    "G":"__.",
    "H":"....",
    "I":"..",
    "J":".___",
    "K":"._.",
    "L":"._..",
    "M":"__",
    "N":"_.",
    "O":"___",
    "P":".__.",
    "Q":"__._",
    "R":"._.",
    "S":"...",
    "T":"_",
    "U":".._",
    "V":"..._",
    "W":".__",
    "X":"_.._",
    "Y":"_.__",
    "Z":"__..",
    "1":".____",
    "2":"..___",
    "3":"...__",
    "4":"...._",
    "5":".....",
    "6":"_....",
    "7":"__...",
    "8":"___..",
    "9":"____.",
    "10":"_____"
}

def convert():
    morse = ""
    for alph in input_str.get():
        if alph == " ":
            morse += "/"
        else:
            morse += data[alph.upper()] + " "
    input_str.delete(first=0, last=len(input_str.get()))
    output.config(text=morse, font=("Helvetica", 10, "bold"), width=50)


window = tk.Tk()
window.title("Text To Morse")
window.minsize(width=400, height=400)
window.config(bg="red", padx=50, pady=50)

input_label = tk.Label(text="Write what you want to convert into Morse", bg="red", font=("Helvetica", 20, "bold"))
input_label.grid(row=0, column=2)
input_str = tk.Entry(width=50)
input_str.grid(row=2, column=2)
output = tk.Label(text="Your Output", bg="red")
output.grid(row=3, column=2)
button = tk.Button(text="Convert Into Morse", bg="red", font=("Helvetica", 10, "normal"), command=convert)
button.grid(row=8, column=2)


window.mainloop()
