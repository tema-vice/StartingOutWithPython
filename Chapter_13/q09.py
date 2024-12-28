# Exercise 9
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.canvas = tk.Canvas(self.main_window,
                                width=300,
                                height=300)
        width = 6
        angle_1 = 60
        angle_2 = 240
        step = 15
        year = 5
        for n in range(5):
            self.canvas.create_text(angle_1+16, angle_1+16, text=year)
            self.canvas.create_oval(angle_1, angle_1, angle_2, angle_2, width= width)
            year -= 1
            width -= 1
            angle_1 += step
            angle_2 -= step
        self.canvas.pack()
        tk.mainloop()

my_gui = MyGUI()
