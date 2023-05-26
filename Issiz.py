from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:str, uyruk:str, maviYaka:float = 0.0, beyazYaka:float = 0.0, yonetici:float=0.0) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self._tecrube = {"maviyaka" : maviYaka, "beyazyaka" : beyazYaka, "yonetici" : yonetici}
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
        if self._tecrube["maviyaka"] * 0.2 > self._tecrube["beyazyaka"] * 0.35 and self._tecrube["maviyaka"] * 0.2 > self._tecrube["yonetici"] * 0.45:
            return "maviyaka"
        elif self._tecrube["beyazyaka"] * 0.35 > self._tecrube["maviyaka"] * 0.2 and self._tecrube["beyazyaka"] * 0.35 > self._tecrube["yonetici"] * 0.45:
            return "beyazyaka"
        else:
            return "yonetici"

    def __str__(self) -> str:
        return f"Ad: {self._ad}\nSoyad: {self._soyad}\nStatü: {self.statu_bul()}\n"
