# Exersice 2
import tkinter as tk
class MyGUI():
    def __init__(self):
        self.main_window = tk.Tk()
        self.__create_label()
        self.__create_frame()
        self.__fill_frame()
        tk.mainloop()

    def __create_label(self):
        self.var = tk.StringVar()
        self.label = tk.Label(self.main_window,
                              textvariable=self.var,
                              width=10)
        self.label.pack()

    def __create_frame(self):
        self.frame = tk.Frame(self.main_window)
        self.frame.pack()

    def __fill_frame(self):
        self.word_1_button = tk.Button(self.frame,
                                       text='sinister',
                                       command=lambda: self.__show_word(word='Left'))
        self.word_1_button.pack(side='left', padx=10, pady=5)
        self.word_2_button = tk.Button(self.frame,
                                       text='medium',
                                       command=lambda: self.__show_word(word='Central'))
        self.word_2_button.pack(side='left', padx=10, pady=5)
        self.word_3_button = tk.Button(self.frame,
                                       text='dexter',
                                       command=lambda: self.__show_word(word='Right'))
        self.word_3_button.pack(side='left', padx=10, pady=5)

    def __show_word(self, word):
        self.var.set(word)

my_gui = MyGUI()
