from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

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


if __name__ == "__main__": main()  