# Exercise 3
import tkinter as tk
import tkinter.messagebox as tkmbox
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.__create_info_label()
        self.__create_frame()
        self.__fill_left_frame()
        self.__fill_right_frame()
        tk.mainloop()

    def __create_info_label(self):
        self.info_label = tk.Label(self.main_window,
                                   text='Enter data for calculate.')
        self.info_label.pack(side='top', padx=10, pady=(5,5))

    def __create_frame(self):
        self.left_frame = tk.Frame(self.main_window)
        self.left_frame.pack(side='left')

        self.right_frame = tk.Frame(self.main_window)
        self.right_frame.pack(side='right')
        # String 1
        self.right_top_frame = tk.Frame(self.right_frame)
        self.right_top_frame.pack(side='top')
        # String 2
        self.right_middle_frame = tk.Frame(self.right_frame)
        self.right_middle_frame.pack(side='top')
        # String 3
        self.right_bottom_frame = tk.Frame(self.right_frame)
        self.right_bottom_frame.pack(side='bottom')

    def __fill_left_frame(self):
        self.calculate_button = tk.Button(self.left_frame,
                                          text='Calculate',
                                          width=10,
                                          command=self.calculate)
        self.calculate_button.pack(padx=10, pady=(0, 10))

        self.quit_button = tk.Button(self.left_frame,
                                     text='Quit',
                                     width=10,
                                     command=self.main_window.destroy)
        self.quit_button.pack(padx=10, pady=(0, 2))

    def __fill_right_frame(self):
        # String 1
        self.gallons_label = tk.Label(self.right_top_frame,
                              text='Enter the volume of gasoline in gallons:')
        self.gallons_label.pack(side='left',pady=(2,2))

        self.gallons_entry = tk.Entry(self.right_top_frame,
                              width=8)
        self.gallons_entry.pack(side='left', padx=(118,10),pady=(2,2))

        # String 2
        self.miles_label = tk.Label(self.right_middle_frame,
                                    text='Enter the number of miles the vehicle can travel on a full tank:')
        self.miles_label.pack(side='left', pady=(2,2))

        self.miles_entry = tk.Entry(self.right_middle_frame,
                                    width=8)
        self.miles_entry.pack(side='left', padx=(0,10), pady=(2,2))

        # String 3
        self.label = tk.Label(self.right_bottom_frame,
                              text='Calculation result:')
        self.label.pack(side='left', pady=(2,2))

        self.result = tk.StringVar()
        self.result_label = tk.Label(self.right_bottom_frame,
                                     textvariable=self.result,
                                     width=8)
        self.result_label.pack(side='left', padx=(225,10), pady=(2,2))

    def calculate(self):
        try:
            gallons = float(self.gallons_entry.get())
            miles = float(self.miles_entry.get())
            result = miles / gallons
            self.result.set(f'{result:.2f}')
        except Exception:
            tkmbox.showerror('Error', 'Input error.')

my_gui = MyGUI()
