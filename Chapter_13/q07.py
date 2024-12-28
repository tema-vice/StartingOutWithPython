# Exercise 7
import tkinter as tk
import tkinter.messagebox as tkmbox
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.__create_info_label()
        self.__create_radiobutton()
        self.__create_frame_and_entry()
        self.__create_frame_and_label()
        self.__create_button()
        tk.mainloop()

    def __create_info_label(self):
        self.info_label = tk.Label(self.main_window, text="Select tariff")
        self.info_label.grid(column=0, row=0)

    def __create_radiobutton(self):
        self.var = tk.IntVar()
        self.var.set(15)
        self.radiobutton1 = tk.Radiobutton(self.main_window,
                                           text='Daytime (6:00-17:59) - 0.15$',
                                           variable=self.var,
                                           value=15)
        self.radiobutton2 = tk.Radiobutton(self.main_window,
                                           text='Evening time (18:00-23:59) - 0.20$',
                                           variable=self.var,
                                           value=20)
        self.radiobutton3 = tk.Radiobutton(self.main_window,
                                           text='Night time (0:00-5:59) - 0.10$',
                                           variable=self.var,
                                           value=10)
        self.radiobutton1.grid(column=0, row=1, sticky=tk.W)
        self.radiobutton2.grid(column=0, row=2, sticky=tk.W)
        self.radiobutton3.grid(column=0, row=3, sticky=tk.W)

    def __create_frame_and_entry(self):
        self.top_frame = tk.Frame(self.main_window)
        self.top_frame.grid(column=0, row=4, sticky=tk.W)

        self.minute_label = tk.Label(self.top_frame,
                                     text='Enter minutes:')
        self.minute_label.pack(side=tk.LEFT)

        self.minute_entry = tk.Entry(self.top_frame,
                                     width=5)
        self.minute_entry.pack(side=tk.LEFT)

    def __create_frame_and_label(self):
        self.bottom_frame = tk.Frame(self.main_window)
        self.bottom_frame.grid(column=0, row=5, sticky=tk.W)

        self.label = tk.Label(self.bottom_frame,
                                     text="Result:")
        self.label.pack(side=tk.LEFT)

        self.result = tk.StringVar()
        self.result_label = tk.Label(self.bottom_frame,
                                     textvariable=self.result)
        self.result_label.pack(side=tk.LEFT)

    def __create_button(self):
        self.calculate_button = tk.Button(self.main_window,
                                     text='Show costs',
                                     command=self.calculate,
                                     width=10)
        self.calculate_button.grid(column=0, row=6)

        self.quit_button = tk.Button(self.main_window,
                                     text='Quit',
                                     command=self.main_window.destroy,
                                     width=10)
        self.quit_button.grid(column=0, row=7)

    def calculate(self):
        try:
            minutes = float(self.minute_entry.get())
            choice = float(self.var.get()/100)
            if (choice == 0.15) and (minutes > 719):
                tkmbox.showerror('Error','There cant be that many minutes.')
            elif (choice == 0.20) and (minutes > 359):
                tkmbox.showerror('Error', 'There cant be that many minutes.')
            elif (choice == 0.10) and (minutes > 359):
                tkmbox.showerror('Error', 'There cant be that many minutes.')
            elif minutes < 0:
                tk.messagebox.showerror('Error', 'Please enter a number greater than zero.')
            else:
                self.result.set(f'{choice*minutes:.2f}$')
        except Exception:
            tkmbox.showerror('Error', 'Input is not a number.')

my_gui = MyGUI()
