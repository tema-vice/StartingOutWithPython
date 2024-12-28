# Exercise 12
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.canvas = tk.Canvas(self.main_window,
                                width=500,
                                height=500)
        self.canvas.create_oval(230, 230, 270, 270, fill='yellow')
        self.canvas.create_oval(215, 215, 285, 285)
        self.canvas.create_oval(222, 222, 228, 228, fill='gray')
        self.canvas.create_oval(200, 200, 300, 300)
        self.canvas.create_oval(200, 230, 208, 238, fill='orange')
        self.canvas.create_oval(180, 180, 320, 320)
        self.canvas.create_oval(200, 192, 209, 201, fill='blue')
        self.canvas.create_oval(155, 155, 345, 345)
        self.canvas.create_oval(332, 211, 342, 221, fill='red')
        self.canvas.create_oval(135, 135, 365, 365)
        self.canvas.create_oval(328, 326, 340, 338, fill='gold')
        self.canvas.create_oval(110, 110, 390, 390)
        self.canvas.create_oval(260, 380, 277, 397, fill='brown')
        self.canvas.create_oval(80, 80, 420, 420)
        self.canvas.create_oval(78, 280, 91, 293, fill='aqua')
        self.canvas.create_oval(50, 50, 450, 450)
        self.canvas.create_oval(280, 49, 291, 60, fill='royalblue')
        self.canvas.create_oval(10, 10, 490, 490)
        self.canvas.create_oval(82, 420, 86, 425, fill='black')
        self.canvas.pack()
        tk.mainloop()

my_gui = MyGUI()