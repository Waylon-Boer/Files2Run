import tkinter, tkinter.ttk, os
if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Files2Run Lite")
    try:
        root.iconbitmap("files2run.ico")
    finally:
        root.resizable(width=False, height=False)
        tkinter.Label(root, text="  ").grid(row=0, column=0)
        e = tkinter.ttk.Entry(root, width=40, font=("Segoe UI", 12))
        e.grid(row=0, column=1, ipadx=20, ipady=6, pady=12)
        tkinter.Label(root, text="  ").grid(row=0, column=2)
        f = tkinter.Frame()
        f.grid(row=1, column=1)
        tkinter.ttk.Button(f, text="OK", command=lambda: os.system("start " + e.get()), width=12).grid(row=0, column=0)
        tkinter.ttk.Button(f, text="Cancel", command=root.destroy, width=12).grid(row=0, column=1)
        tkinter.Label(f, text="", font=("", 2)).grid(row=1, column=1)
        root.bind("<Return>", lambda a: os.system("start " + e.get()))
        root.bind("<Delete>", lambda a: e.delete(0, "end"))
        root.mainloop()
