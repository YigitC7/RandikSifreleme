import customtkinter as ctk
import anahtar_nedir

def start():
    win = ctk.CTk()
    win.geometry('700x200')
    win.title("Anahtar Nedir?")
    win.minsize(700,200)
    win.maxsize(800,230)
    aciklama_text = ctk.CTkLabel(win,text=anahtar_nedir.y,text_color="blue")
    aciklama_text.pack(pady=30,padx=1)
    win.mainloop()