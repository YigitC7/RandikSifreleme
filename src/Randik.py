import random
import json

def harf_haritasi_olustur(anahtar):
    random.seed(anahtar)
    orijinal_harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sifreli_harfler = list(orijinal_harfler)
    random.shuffle(sifreli_harfler)
    return dict(zip(orijinal_harfler, sifreli_harfler)), dict(zip(sifreli_harfler, orijinal_harfler))

def sifrele(metin, sifreleme_haritasi):
    return "".join(sifreleme_haritasi.get(harf, harf) for harf in metin)

def desifrele(sifreli_metin, desifreleme_haritasi):
    return "".join(desifreleme_haritasi.get(harf, harf) for harf in sifreli_metin)



