# Exercise 6
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.__create_checkbutton()
        self.__create_frame_and_label()
        self.__create_button()
        tk.mainloop()

    def __create_checkbutton(self):
       # Create object IntVar
        self.cb_var1 = tk.IntVar()
        self.cb_var2 = tk.IntVar()
        self.cb_var3 = tk.IntVar()
        self.cb_var4 = tk.IntVar()
        self.cb_var5 = tk.IntVar()
        self.cb_var6 = tk.IntVar()
        self.cb_var7 = tk.IntVar()

        self.cb1 = tk.Checkbutton(self.main_window,
                                  text='Oil change - 30$',
                                  variable=self.cb_var1,
                                  onvalue=30, offvalue=0)
        self.cb2 = tk.Checkbutton(self.main_window,
                                  text='Lube job - 20$',
                                  variable=self.cb_var2,
                                  onvalue=20, offvalue=0)
        self.cb3 = tk.Checkbutton(self.main_window,
                                  text='Radiator flush - 40$',
                                  variable=self.cb_var3,
                                  onvalue=40, offvalue=0)
        self.cb4 = tk.Checkbutton(self.main_window,
                                  text='Transmissions flush - 100$',
                                  variable=self.cb_var4,
                                  onvalue=100, offvalue=0)
        self.cb5 = tk.Checkbutton(self.main_window,
                                  text='Inspection - 35$',
                                  variable=self.cb_var5,
                                  onvalue=35, offvalue=0)
        self.cb6 = tk.Checkbutton(self.main_window,
                                  text='Muffler replacement - 200$',
                                  variable=self.cb_var6,
                                  onvalue=200, offvalue=0)
        self.cb7 = tk.Checkbutton(self.main_window,
                                  text='Tire rotation - 30$',
                                  variable=self.cb_var7,
                                  onvalue=30, offvalue=0)
        self.cb1.grid(column=0, row=0, sticky='w')
        self.cb2.grid(column=0, row=1, sticky='w')
        self.cb3.grid(column=0, row=2, sticky='w')
        self.cb4.grid(column=0, row=3, sticky='w')
        self.cb5.grid(column=0, row=4, sticky='w')
        self.cb6.grid(column=0, row=5, sticky='w')
        self.cb7.grid(column=0, row=6, sticky='w')

    def __create_frame_and_label(self):
        self.frame = tk.Frame(self.main_window)
        self.frame.grid(column=0, row=7, sticky='w')

        self.label = tk.Label(self.frame,
                              text='Price:')
        self.label.pack(side='left')

        self.result = tk.StringVar()
        self.result_label = tk.Label(self.frame,
                                     textvariable=self.result)
        self.result_label.pack(side='left')

    def __create_button(self):
        self.show_button = tk.Button(self.main_window,
                                     text='Show costs',
                                     command=self.show_costs,
                                     width=10)
        self.show_button.grid(column=0, row=9, sticky='w')

        self.quit_button = tk.Button(self.main_window,
                                     text='Quit',
                                     command=self.main_window.destroy,
                                     width=10)
        self.quit_button.grid(column=0, row=10, sticky='w')

    def show_costs(self):
        result = (self.cb_var1.get() + self.cb_var2.get() + self.cb_var3.get()
                  + self.cb_var4.get() + self.cb_var5.get() + self.cb_var6.get()
                  + self.cb_var7.get())
        self.result.set(f'{result}$')

my_gui = MyGUI()
