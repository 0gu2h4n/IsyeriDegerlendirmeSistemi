from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:int, uyruk:str, maviYaka:float, beyazYaka:float, yonetici:float) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self._tecrube = {"maviyaka" : maviYaka, "beyazyaka" : beyazYaka, "yonetici" : yonetici}
        self.statu = self.statu_bul()

    def statu_bul(self) -> str:
        if self._tecrube["maviyaka"] * 0.2 > self._tecrube["beyazyaka"] * 0.35 and self._tecrube["maviyaka"] * 0.2 > self._tecrube["yonetici"] * 0.45:
            return "maviyaka"
        elif self._tecrube["beyazyaka"] * 0.35 > self._tecrube["maviyaka"] * 0.2 and self._tecrube["beyazyaka"] * 0.35 > self._tecrube["yonetici"] * 0.45:
            return "beyazyaka"
        else:
            return "yonetici"

    def __str__(self) -> str:
        return f"Ad: {self.ad}\nSoyad: {self.soyad}\nStatu: {self.statu_bul()}\n"
