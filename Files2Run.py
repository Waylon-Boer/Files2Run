from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Button
import os
if __name__ == "__main__":
    root = Tk()
    root.title("Files2Run")
    try:
        root.iconbitmap("files2run.ico")
    finally:
        root.resizable(width=False, height=False)
        e = Entry(root, width=40, borderwidth=14, relief=FLAT, font=("", 13), background="#eee")
        e.grid(row=0, column=0, sticky="nsew")
        f = Frame()
        f.grid(row=1, column=0, sticky="nsew")
        Button(f, text="Run", command=lambda: os.system("start " + e.get()), width=12).grid(row=0, column=0, sticky="nsew")
        Button(f, text="Browse", command=lambda: os.startfile(filedialog.askopenfilename(filetypes=[('All Files', '*.*')]), "open"), width=12).grid(row=0, column=1, sticky="nsew")
        Button(f, text="Clear", command=lambda: e.delete(0, "end"), width=12).grid(row=0, column=2, sticky="nsew")
        Button(f, text="About", command=lambda: messagebox.showinfo("About Files2Run", "(c) Waylon Boer"), width=12).grid(row=0, column=3, sticky="nsew")
        Button(f, text="Exit", command=root.destroy, width=12).grid(row=0, column=4, sticky="nsew")
        root.bind("<Return>", lambda a: os.system("start " + e.get()))
        root.bind("<Delete>", lambda a: e.delete(0, "end"))
        root.mainloop()
