from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor: str, tecrube: int, maas: float, prim:int) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self._prim = prim

    def prim_yap(self, prim:int) -> None:
        self._prim = prim

    def prim_al(self) -> int:
        return self._prim
    
    def zam_hakki(self) -> float:
        if self._tecrube < 24:
            return self._prim
        elif self._tecrube >= 24 and self._tecrube < 48 and self._maas < 15000:
            return (self._maas % self._tecrube) * 5 + self._prim 
        elif self._tecrube >= 48 and self._maas < 25000:
            return (self._maas % self._tecrube) * 4 + self._prim
        else:
            return 0