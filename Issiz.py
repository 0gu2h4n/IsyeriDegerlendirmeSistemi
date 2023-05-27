from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:str, uyruk:str, maviYaka:float = 0.0, beyazYaka:float = 0.0, yonetici:float=0.0) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self._tecrube = {"maviyaka" : maviYaka, "beyazyaka" : beyazYaka, "yönetici" : yonetici}
        self.statu = self.statu_bul()

    def tecrube_ekle(self, statu:str, yil:int) -> None:
        try:
            self._tecrube[statu] += yil
            self.statu = self.statu_bul()
        except KeyError:
            print("Hatalı statü girişi yapıldı. Lütfen statüyü kontrol ediniz.")

    def tecrube_al(self, statu:str) -> float:
        try:
            return self._tecrube[statu]
        except KeyError:
            print("Hatalı statü girişi yapıldı. Lütfen statüyü kontrol ediniz.")

    def statu_bul(self) -> str:
        if not self._tecrube["yönetici"] and not self._tecrube["beyazyaka"] and not self._tecrube["maviyaka"]:
            return "Tecrübesiz"
        elif self._tecrube["yönetici"] * 0.45 >= self._tecrube["maviyaka"] * 0.2 and self._tecrube["yönetici"] * 0.45 >= self._tecrube["beyazyaka"] * 0.35:
            return "Yönetici"
        elif self._tecrube["beyazyaka"] * 0.35 > self._tecrube["yönetici"] * 0.45 and self._tecrube["beyazyaka"] * 0.35 >= self._tecrube["maviyaka"] * 0.2:
            return "Beyaz Yaka"
        elif self._tecrube["maviyaka"] * 0.2 > self._tecrube["yönetici"] * 0.45 and self._tecrube["maviyaka"] * 0.2 > self._tecrube["beyazyaka"] * 0.35:
            return "Mavi Yaka"
        
    def __str__(self) -> str:
        return f"Ad: {self._ad}\nSoyad: {self._soyad}\nStatü: {self.statu_bul()}\n"