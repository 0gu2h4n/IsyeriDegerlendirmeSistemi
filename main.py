from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

def main():
    while True:
        print("\n***Çalışan Bilgi Sistemi***\n")
        kayitlar = []
        secim = input("Kayıt türü seçiniz:\n1-İnsan\n2-İşsiz\n3-Çalışan\n4-Beyaz Yaka\n5-Mavi Yaka\n0-Çıkış\nSeçiminiz: ")
        if secim == "1":
            _tcno = input("TC Kimlik No: ")
            _ad = input("Ad: ")
            _soyad = input("Soyad: ")
            _yas = int(input("Yaş: "))
            _cinsiyet = input("Cinsiyet: ")
            _uyruk = input("Uyruk: ")
            insan = Insan(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk)
            kayitlar.append(insan)



if __name__ == "__main__": main()  