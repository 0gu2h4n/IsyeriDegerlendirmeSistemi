from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:str, uyruk:str, maviYaka:float = 0.0, beyazYaka:float = 0.0, yonetici:float=0.0) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__tecrube = {"maviyaka" : maviYaka, "beyazyaka" : beyazYaka, "yönetici" : yonetici}
        self.statu = self.statu_bul()

    def tecrube_ekle(self, statu:str, yil:int) -> None:
        try:
            self.__tecrube[statu] += yil
            self.statu = self.statu_bul()
        except KeyError:
            print("Hatalı statü girişi yapıldı. Lütfen statüyü kontrol ediniz.")

    def tecrube_al(self, statu:str) -> float:
        try:
            return self.__tecrube[statu]
        except KeyError:
            print("Hatalı statü girişi yapıldı. Lütfen statüyü kontrol ediniz.")

    def statu_bul(self) -> str:
        if not self.__tecrube["yönetici"] and not self.__tecrube["beyazyaka"] and not self.__tecrube["maviyaka"]:
            return "Tecrübesiz"
        elif self.__tecrube["yönetici"] * 0.45 >= self.__tecrube["maviyaka"] * 0.2 and self.__tecrube["yönetici"] * 0.45 >= self.__tecrube["beyazyaka"] * 0.35:
            return "Yönetici"
        elif self.__tecrube["beyazyaka"] * 0.35 > self.__tecrube["yönetici"] * 0.45 and self.__tecrube["beyazyaka"] * 0.35 >= self.__tecrube["maviyaka"] * 0.2:
            return "Beyaz Yaka"
        elif self.__tecrube["maviyaka"] * 0.2 > self.__tecrube["yönetici"] * 0.45 and self.__tecrube["maviyaka"] * 0.2 > self.__tecrube["beyazyaka"] * 0.35:
            return "Mavi Yaka"
        
    def __str__(self) -> str:
        return f"Ad: {self._Insan__ad}\nSoyad: {self._Insan__soyad}\nStatü: {self.statu_bul()}\n"