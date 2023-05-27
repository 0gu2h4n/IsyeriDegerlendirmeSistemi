from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka
import pandas as pd

def main():
    
    insan1 = Insan("10001", "Ali", "Yılmaz", 25, "Erkek", "Türk")
    insan2 = Insan("10002", "Veli", "Yılmaz", 31, "Erkek", "Türk")
    print(insan1)
    print(insan2)

    issiz1 = Issiz("10003", "Ayşe", "Aras", 28, "Kadın", "Türk", 6, 1, 0)
    issiz2 = Issiz("10004", "Selim", "Duran", 39, "Erkek", "Türk", 7, 4, 4)
    issiz3 = Issiz("10005", "Mehmet", "Diren", 25, "Erkek", "Türk", 3, 2, 2)
    print(issiz1)
    print(issiz2)
    print(issiz3)

    calisan1 = Calisan("10006", "Arda", "Dağ", 21, "Erkek", "Türk", "Teknoloji", 12, 9000)
    calisan2 = Calisan("10007", "Sevda", "Mari", 29, "Kadın", "Türk", "Diğer", 29, 14000)
    calisan3 = Calisan("10008", "Derin", "Üreten", 44, "Kadın", "Türk", "Muhasebe", 51, 22000)
    print(calisan1)
    print(calisan2)
    print(calisan3)

    maviyaka1 = MaviYaka("10009", "Durmuş", "Deniz", 25, "Erkek", "Türk", "Teknoloji", 5, 10000, 0.79)
    maviyaka2 = MaviYaka("10010", "Fasıl", "Kuru", 19, "Erkek", "Türk", "İnşaat", 11, 9000, 0.21)
    maviyaka3 = MaviYaka("10011", "Gülbahar", "Tandoğan", 34, "Kadın", "Türk", "Diğer", 60, 29000, 0.54)
    print(maviyaka1)
    print(maviyaka2)
    print(maviyaka3)

    beyazyaka1 = BeyazYaka("10012", "Güney", "Saygı", 21, "Erkek", "Türk", "Teknoloji", 13, 11000, 250)
    beyazyaka2 = BeyazYaka("10013", "Volkan", "Karahan", 33, "Erkek", "Türk", "İnşaat", 21, 13000, 1200)
    beyazyaka3 = BeyazYaka("10014", "Jale", "Türkmen", 34, "Kadın", "Türk", "Diğer", 31, 29000, 3650)
    print(beyazyaka1)
    print(beyazyaka2)
    print(beyazyaka3)

    data = {"tip": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
            "tc_no": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no(), beyazyaka1.get_tc_no(), beyazyaka2.get_tc_no(), beyazyaka3.get_tc_no()],
            "ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad(), beyazyaka1.get_ad(), beyazyaka2.get_ad(), beyazyaka3.get_ad()],
            "soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad(), beyazyaka1.get_soyad(), beyazyaka2.get_soyad(), beyazyaka3.get_soyad()],
            "yas": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas(), beyazyaka1.get_yas(), beyazyaka2.get_yas(), beyazyaka3.get_yas()],
            "cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet(), beyazyaka1.get_cinsiyet(), beyazyaka2.get_cinsiyet(), beyazyaka3.get_cinsiyet()],
            "uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk(), beyazyaka1.get_uyruk(), beyazyaka2.get_uyruk(), beyazyaka3.get_uyruk()],
            "sektor": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(), maviyaka2.get_sektor(), maviyaka3.get_sektor(), beyazyaka1.get_sektor(), beyazyaka2.get_sektor(), beyazyaka3.get_sektor()],
            "tecrube": [calisan1.get_tecrube()/12, calisan2.get_tecrube()/12, calisan3.get_tecrube()/12, maviyaka1.get_tecrube()/12, maviyaka2.get_tecrube()/12, maviyaka3.get_tecrube()/12, beyazyaka1.get_tecrube()/12, beyazyaka2.get_tecrube()/12, beyazyaka3.get_tecrube()/12],
            "maas": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas(), beyazyaka1.get_maas(), beyazyaka2.get_maas(), beyazyaka3.get_maas()],
            "yipranma": [0, 0, 0, maviyaka1.get_yipranma(), maviyaka2.get_yipranma(), maviyaka3.get_yipranma(), 0, 0, 0], 
            "prim": [0, 0, 0, 0, 0, 0, beyazyaka1.get_prim(), beyazyaka2.get_prim(), beyazyaka3.get_prim()],
            "yenimaas": [calisan1.yenimaas(), calisan2.yenimaas(), calisan3.yenimaas(), maviyaka1.yenimaas(), maviyaka2.yenimaas(), maviyaka3.yenimaas(), beyazyaka1.yenimaas(), beyazyaka2.yenimaas(), beyazyaka3.yenimaas()]}

    df = pd.DataFrame(data, columns=["tip", "tc_no", "ad", "soyad", "yas", "cinsiyet", "uyruk", "sektor", "tecrube", "maas", "yipranma", "prim", "yenimaas"])
    print(df.groupby("tip").agg(tecrubeOrtalama = pd.NamedAgg(column='tecrube', aggfunc='mean'), yenimaasOrtalama = pd.NamedAgg(column='yenimaas', aggfunc='mean')))

    print("\nMaaşı 15000 TL üzerinde olan kişi sayısı:", df[df.maas > 15000].count()["maas"])


if __name__ == "__main__": main()  