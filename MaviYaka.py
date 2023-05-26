from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor: str, tecrube: int, maas: float, yipranma:float) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self._yipranma = yipranma

    def yipranma_yap(self, yipranma:float) -> None:
        self._yipranma = yipranma

    def yipranma_al(self) -> float:
        return self._yipranma
    
    def zam_hakki(self) -> float:
        if self._tecrube < 24:
            return self._yipranma * 10
        elif self._tecrube >= 24 and self._tecrube < 48 and self._maas < 15000:
            return self._maas * (self._maas % self._tecrube) / 2 + self._yipranma * 10
        elif self._tecrube >= 48 and self._maas < 25000:
            return self._maas * (self._maas % self._tecrube) / 3 + self._yipranma * 10
        else:
            return self._maas * 0