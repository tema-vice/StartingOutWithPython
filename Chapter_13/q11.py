# Exercise 11
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.canvas = tk.Canvas(self.main_window,
                                width=300,
                                height=300)
        self.canvas.create_polygon(75, 165, 225, 165,
                                   250, 125, 225, 135,
                                   75, 135, 50, 120)
        self.canvas.create_text(150, 50, text='boat :)')
        self.canvas.pack()
        tk.mainloop()

my_gui = MyGUI()
