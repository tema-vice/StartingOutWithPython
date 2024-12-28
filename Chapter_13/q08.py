# Exercise 8
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.canvas = tk.Canvas(self.main_window,
                                width=300,
                                height=300)
        self.canvas.create_rectangle(0, 0, 300, 300, fill='blue')
        self.canvas.create_rectangle(0, 200, 300, 300, fill='green')
        self.canvas.create_rectangle(75, 105, 225, 255, fill='red')
        self.canvas.create_rectangle(130, 190, 170, 255, fill='orange')
        self.canvas.create_rectangle(100, 125, 125, 175, fill='yellow')
        self.canvas.create_rectangle(175, 125, 200, 175, fill='yellow')
        self.canvas.create_arc(75, 45, 225, 165, start=0, extent=180, fill='black')
        self.canvas.pack()
        tk.mainloop()

my_gui = MyGUI()
