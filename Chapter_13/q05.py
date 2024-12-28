# Exercise 5
import tkinter as tk
import tkinter.messagebox as tkmbox
TAX_PERCENTAGE = 0.6
TAX = 0.75
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.__create_frame()
        self.__fill_top_frame()
        self.__fill_middle_frame()
        self.__fill_bottom_frame()
        self.__create_button()
        tk.mainloop()

    def __create_frame(self):
        self.top_frame = tk.Frame(self.main_window)
        self.top_frame.pack()
        self.middle_frame = tk.Frame(self.main_window)
        self.middle_frame.pack()
        self.bottom_frame = tk.Frame(self.main_window)
        self.bottom_frame.pack()

    def __fill_top_frame(self):
        self.top_label = tk.Label(self.top_frame,
                                  text="Actual value of real estate")
        self.top_label.pack(side='left')

        self.top_entry = tk.Entry(self.top_frame,
                                  width=10)
        self.top_entry.pack(side='left')

    def __fill_middle_frame(self):
        self.middle_label = tk.Label(self.middle_frame,
                                    text='Estimated value ($):')
        self.middle_label.pack(side='left')

        self.middle_result = tk.StringVar()
        self.result_middle_label = tk.Label(self.middle_frame,
                                            textvariable=self.middle_result)
        self.result_middle_label.pack(side='left')

    def __fill_bottom_frame(self):
        self.bottom_label = tk.Label(self.bottom_frame,
                                     text='Tax ($):')
        self.bottom_label.pack(side='left')

        self.bottom_result = tk.StringVar()
        self.result_bottom_label = tk.Label(self.bottom_frame,
                                            textvariable=self.bottom_result)
        self.result_bottom_label.pack(side='left')

    def __create_button(self):
        self.calculate_button = tk.Button(self.main_window,
                                          text='Calculate',
                                          command=self.calculate)
        self.calculate_button.pack(side='left', padx=(50, 5), pady=(0, 5))
        self.quit_button = tk.Button(self.main_window,
                                     text='Quit',
                                     command=self.main_window.destroy)
        self.quit_button.pack(side='left', padx=(5, 50), pady=(0, 5))

    def calculate(self):
        try:
            price = float(self.top_entry.get())
            if price <= 0:
                tkmbox.showerror("Error", "Cannot be a negative value.")
            else:
                estimate = price * TAX_PERCENTAGE
                tax = (estimate // 100) * TAX
                self.middle_result.set(estimate)
                self.bottom_result.set(tax)
        except Exception:
            tkmbox.showerror('Error', 'Input error.')

my_gui = MyGUI()
