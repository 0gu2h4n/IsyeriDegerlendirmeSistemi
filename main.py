from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

def main():
    kayitlar = []
    while True:
        print("\n***Çalışan Bilgi Sistemi***\n")
        secim = input("Kayıt türü seçiniz:\n1-İnsan\n2-İşsiz\n3-Çalışan\n4-Beyaz Yaka\n5-Mavi Yaka\n0-Menü Geç\nSeçiminiz: ")
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
        elif secim == "3":
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
            _sektor = input("Sektör: ")
            while True:
                try:
                    _tecrube = int(input("Tecrübe (Ay): "))
                    if _tecrube < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir tecrübe değeri giriniz.")
            while True:
                try:
                    _maas = int(input("Maaş: "))
                    if _maas < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir maaş giriniz.")
            while True:
                try:
                    _calisan = Calisan(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, _sektor, _tecrube, _maas)
                    break
                except Exception as e: 
                    print(e)
                    _calisan = Calisan(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, "Diğer", _tecrube, _maas)
                    print("Sektör bilgisi 'Diğer' olarak kaydedildi.")
                    degisiklik = input("Sektör bilgisi değişikliği için sektör bilgisini giriniz (Çıkmak için 0): ")
                    if degisiklik == "0": break
                    else: _calisan.sektor_yap(degisiklik)
            kayitlar.append(_calisan)
        elif secim == "4":
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
            _sektor = input("Sektör: ")
            while True:
                try:
                    _tecrube = int(input("Tecrübe (Ay): "))
                    if _tecrube < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir tecrübe değeri giriniz.")
            while True:
                try:
                    _maas = int(input("Maaş: "))
                    if _maas < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir maaş giriniz.")
            while True:
                try:
                    _prim = int(input("Prim: "))
                    if _prim < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir prim giriniz.")
            while True:
                try:
                    _beyazyaka = BeyazYaka(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, _sektor, _tecrube, _maas, _prim)
                    break
                except Exception as e:
                    print(e)
                    _beyazyaka = BeyazYaka(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, "Diğer", _tecrube, _maas, _prim)
                    print("Sektör bilgisi 'Diğer' olarak kaydedildi.")
                    degisiklik = input("Sektör bilgisi değişikliği için sektör bilgisini giriniz (Çıkmak için 0): ")
                    if degisiklik == "0": break
                    else: _beyazyaka.sektor_yap(degisiklik)
            kayitlar.append(_beyazyaka)
        elif secim == "5":
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
            _sektor = input("Sektör: ")
            while True:
                try:
                    _tecrube = int(input("Tecrübe (Ay): "))
                    if _tecrube < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir tecrübe değeri giriniz.")
            while True:
                try:
                    _maas = int(input("Maaş: "))
                    if _maas < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir maaş giriniz.")
            while True:
                try:
                    _yipranma = int(input("Yipranma: "))
                    if _yipranma < 0: raise ValueError
                    break
                except ValueError: print("Geçerli bir prim giriniz.")
            while True:
                try:
                    _maviyaka = MaviYaka(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, _sektor, _tecrube, _maas, _yipranma)
                    break
                except Exception as e:
                    print(e)
                    _maviyaka = MaviYaka(_tcno, _ad, _soyad, _yas, _cinsiyet, _uyruk, "Diğer", _tecrube, _maas, _yipranma)
                    print("Sektör bilgisi 'Diğer' olarak kaydedildi.")
                    degisiklik = input("Sektör bilgisi değişikliği için sektör bilgisini giriniz (Çıkmak için 0): ")
                    if degisiklik == "0": break
                    else: _maviyaka.sektor_yap(degisiklik)
            kayitlar.append(_maviyaka)
        elif secim == "0":
            print("Sonraki adıma geçiliyor yapılıyor...")
            break
        else:
            print("Geçerli bir seçim yapınız.")

if __name__ == "__main__": main()  