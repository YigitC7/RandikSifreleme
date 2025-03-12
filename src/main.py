import customtkinter as ctk
from widgets import widget

class MainWin():
    def __init__(self,window):
        self.window = window
        self.window.title("Randik Şifreleme")
        self.window.geometry('800x500')
        self.window.minsize(800,500)

        widget(self.window)
        

if __name__ == '__main__':
    window = ctk.CTk()
    app = MainWin(window)
    window.mainloop()