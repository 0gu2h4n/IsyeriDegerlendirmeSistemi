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



if __name__ == "__main__": main()  