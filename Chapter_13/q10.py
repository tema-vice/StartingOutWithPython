# Exercise 10
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.canvas = tk.Canvas(self.main_window,
                                width=300,
                                height=300)
        self.canvas.create_rectangle(0,0, 300,300)
        self.canvas.create_line(150, 50, 125, 110)
        self.canvas.create_line(150, 50, 175, 110)

        self.canvas.create_line(125, 110, 65, 110)
        self.canvas.create_line(175, 110, 235, 110)

        self.canvas.create_line(65, 110, 110, 150)
        self.canvas.create_line(235, 110, 190, 150)

        self.canvas.create_line(110, 150, 90, 210)
        self.canvas.create_line(190, 150, 210, 210)

        self.canvas.create_line(90, 210, 150, 170)
        self.canvas.create_line(210, 210, 150, 170)
        self.canvas.create_text(150, 140, text='Artem', anchor=tk.S)
        self.canvas.pack()
        tk.mainloop()

my_gui = MyGUI()
