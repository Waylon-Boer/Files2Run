from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import *
import os
if __name__ == "__main__":
    root = Tk()
    root.title("Files2Run")
    try:
        root.iconbitmap("files2run.ico")
    finally:
        root.resizable(width=False, height=False)
        f = Frame()
        f.grid(row=0, column=0)
        Label(f, text="", font=("", 2)).grid(row=0, column=2)
        Button(f, text="OK", command=lambda: os.system("start " + e.get()), width=10).grid(row=1, column=0)
        Button(f, text="Cancel", command=root.destroy, width=10).grid(row=1, column=1)
        Button(f, text="Delete", command=lambda: e.delete(0, "end"), width=10).grid(row=1, column=2)
        Button(f, text="Browse", command=lambda: os.startfile(filedialog.askopenfilename(), "open"), width=10).grid(row=1, column=3)
        Button(f, text="About", command=lambda: messagebox.showinfo("About Files2Run", "Files2Run: A run prompt\nCopyright (C) 2022 and later: Waylon Boer\n\nMIT License\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."), width=10).grid(row=1, column=4)
        e = Entry(root, width=35, font=("Segoe UI", 12))
        e.grid(row=1, column=0, ipadx=20, ipady=5, padx=12, pady=12)
        root.bind("<Return>", lambda a: os.system("start " + e.get()))
        root.mainloop()
