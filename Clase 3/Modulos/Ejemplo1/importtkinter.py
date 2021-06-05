import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
btn = tk.Button(root, text="Apretame", command=lambda : tk.messagebox.showinfo(message="¡Hola Curso!"))
btn.pack(side=tk.TOP)
root.mainloop()