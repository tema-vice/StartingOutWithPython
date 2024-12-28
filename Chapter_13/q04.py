# Exercise 4
import tkinter as tk
import tkinter.messagebox as tkmbox
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.__create_info_label()
        self.__create_frame()
        self.__fill_frame()
        self.__create_button()
        tk.mainloop()

    def __create_info_label(self):
        self.info_label = tk.Label(self.main_window,
                                   text='Enter data for calculate.')
        self.info_label.pack()

    def __create_frame(self):
        self.top_frame = tk.Frame(self.main_window)
        self.top_frame.pack()

        self.bottom_frame = tk.Frame(self.main_window)
        self.bottom_frame.pack()

    def __fill_frame(self):
        self.celsius_label = tk.Label(self.top_frame,
                                      text='Celsius:')
        self.celsius_label.pack(side='left')
        self.celsius_entry = tk.Entry(self.top_frame, width=6)
        self.celsius_entry.pack(side='left')

        self.var = tk.StringVar()
        self.fahrenheit_label = tk.Label(self.bottom_frame,
                                         text='Fahrenheit:')
        self.fahrenheit_label.pack(side='left')
        self.result_fahrenheit_label = tk.Label(self.bottom_frame,
                                                textvariable=self.var)
        self.result_fahrenheit_label.pack(side='left')

    def __create_button(self):
        self.calculate_button = tk.Button(self.main_window,
                                text='Calculate',
                                command=self.calculate)
        self.calculate_button.pack(side='left', padx=(20,5), pady=(0,5))
        self.quit_button = tk.Button(self.main_window,
                                     text='Quit',
                                     command=self.main_window.destroy)
        self.quit_button.pack(side='left', padx=(5,20), pady=(0,5))

    def calculate(self):
        try:
            C = float(self.celsius_entry.get())
            if C < -273:
                tkmbox.showerror('Error',
                                 'The temperature cannot be below absolute zero (-273 C).')
            else:
                F = (9/5 * C) + 32
                self.var.set(f'{F:.2f}')
        except Exception:
            tkmbox.showerror('Error','Input error.')

my_gui = MyGUI()
