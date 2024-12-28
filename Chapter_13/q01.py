# Exercise 1
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.geometry('200x100')
        self.info_label = tk.Label(self.main_window, text='\n\n')
        self.info_label.pack(pady=10, padx=10)

        self.button_frame = tk.Frame(self.main_window)
        self.button_frame.pack()

        self.info_button = tk.Button(self.button_frame,
                                     text='Show Info',
                                     command=self.show_info)
        self.info_button.pack(side='left', padx=5, pady=5)
        self.quit_button = tk.Button(self.button_frame,
                                     text='Quit',
                                     command=self.main_window.destroy)
        self.quit_button.pack(side='left',padx=5, pady=5)
        tk.mainloop()

    def show_info(self):
        self.info_label.config(text='443096. Russia.\nSamara sity\n')

my_gui = MyGUI()
