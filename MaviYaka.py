from Calisan import Calisan

class MaviYaka(Calisan):
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor: str, tecrube: int, maas: float, yipranma:float) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma = yipranma

    def set_yipranma(self, yipranma:float) -> None:
        self.__yipranma = yipranma

    def get_yipranma(self) -> float:
        return self.__yipranma
    
    def zam_hakki(self) -> float:
        if self._Calisan__tecrube < 24:
            return self.__yipranma * 10
        elif self._Calisan__tecrube >= 24 and self._Calisan__tecrube < 48 and self._Calisan__maas < 15000:
            return (self._Calisan__maas % self._Calisan__tecrube) / 2 + self.__yipranma * 10
        elif self._Calisan__tecrube >= 48 and self._Calisan__maas < 25000:
            return (self._Calisan__maas % self._Calisan__tecrube) / 3 + self.__yipranma * 10
        else:
            return 0