import customtkinter as ctk
import Randik
import anahtar_aciklama

def widget(window):
    # Yazı alanı
    metin_paneli = ctk.CTkScrollableFrame(window,width=1000,height=1000)
    metin_paneli.pack(padx=10,pady=80)

    metin_paneli_giris_title = ctk.CTkLabel(metin_paneli,text="Şifrelemek veya çözmek istediğiniz metni girin",font=("italic",15))
    metin_paneli_giris_title.pack()

    metin_paneli_giris = ctk.CTkTextbox(metin_paneli,fg_color="#191970",text_color="white",width=900,height=400,font=("italic",25))
    metin_paneli_giris.pack()

    metin_paneli_cikis_title = ctk.CTkLabel(metin_paneli,text="Çıktı:",font=("italic",15))
    metin_paneli_cikis_title.pack()
    
    metin_paneli_cikis = ctk.CTkTextbox(metin_paneli,fg_color="#191970",text_color="white",width=900,height=400,font=("italic",25))
    metin_paneli_cikis.pack()


    # Anahtar girişi
    input_anahtar = ctk.CTkEntry(window,placeholder_text="Anahtar Girin")
    input_anahtar.place(x=280,y=10)


    # Buttonlar
    def sifrele():
        anahtar = input_anahtar.get()
        sifreleme_haritasi, desifreleme_haritasi = Randik.harf_haritasi_olustur(anahtar)
        sifre = Randik.sifrele(metin_paneli_giris.get("1.0","end-1c"),sifreleme_haritasi)
        
        metin_paneli_cikis.delete("1.0","end")
        metin_paneli_cikis.insert("0.0",sifre)

    buton_sifrele = ctk.CTkButton(window,text="Şifrele",width=50,command=sifrele,fg_color="#800080",hover_color="#4B0082")
    buton_sifrele.place(x=10,y=10)

    def Sifreyi_coz():
        anahtar = input_anahtar.get()
        sifreleme_haritasi, desifreleme_haritasi = Randik.harf_haritasi_olustur(anahtar)
        desifre = Randik.desifrele(metin_paneli_giris.get("1.0","end-1c"),desifreleme_haritasi)

        metin_paneli_cikis.delete("1.0","end")
        metin_paneli_cikis.insert("0.0",desifre)   

    buton_sifrele = ctk.CTkButton(window,text="Şifreyi Çöz",width=60,command=Sifreyi_coz,fg_color="#800080",hover_color="#4B0082")
    buton_sifrele.place(x=80,y=10)

    def temizle():
        metin_paneli_giris.delete("1.0","end")
        metin_paneli_cikis.delete("1.0","end")

    buton_temizle = ctk.CTkButton(window,text="Temizle",width=60,command=temizle,fg_color="#800080",hover_color="#4B0082")
    buton_temizle.place(x=180,y=10)

    def anahtar_acikla():
        anahtar_aciklama.start()

    buton_anahtarNedir = ctk.CTkButton(window,text="?",width=30,command=anahtar_acikla,fg_color="#7B68EE",hover_color="#483D8B")
    buton_anahtarNedir.place(x=430,y=10)

        