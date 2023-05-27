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
            while True:
                try:
                    _yas = int(input("Yaş: "))
                    if _yas < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Geçerli bir yaş giriniz.")
            _cinsiyet = input("Cinsiyet: ")
            _uyruk = input("Uyruk: ")
            _insan = Insan(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk)
            kayitlar.append(_insan)
        elif secim == "2":
            _tcno = input("TC Kimlik No: ")
            _ad = input("Ad: ")
            _soyad = input("Soyad: ")
            while True:
                try:
                    _yas = int(input("Yaş: "))
                    if _yas < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir yaş giriniz.")
            _cinsiyet = input("Cinsiyet: ")
            _uyruk = input("Uyruk: ")
            while True:
                try:
                    _maas = int(input("Maaş: "))
                    if _maas < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir maaş giriniz.")
            while True:
                try:
                    _maviyaka = int(input("Mavi Yaka Çalışma Geçmişi (Yıl): "))
                    if _maviyaka < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir mavi yaka çalışma geçmişi giriniz.")
            while True:
                try:
                    _beyazyaka = int(input("Beyaz Yaka Çalışma Geçmişi (Yıl): "))
                    if _beyazyaka < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir beyaz yaka çalışma geçmişi giriniz.")
            while True:
                try:
                    _yonetici = int(input("Yönetici çalışma geçmişi (Yıl): "))
                    if _yonetici < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir yönetici çalışma geçmişi giriniz.")
            _issiz = Issiz(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, _maas, _maviyaka, _beyazyaka, _yonetici)
            kayitlar.append(_issiz)


if __name__ == "__main__": main()  