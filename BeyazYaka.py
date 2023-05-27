from Calisan import Calisan

class BeyazYaka(Calisan):
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor: str, tecrube: int, maas: float, prim:int) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__prim = prim

    def set_prim(self, prim:int) -> None:
        self.__prim = prim

    def get_prim(self) -> int:
        return self.__prim
    
    def zam_hakki(self) -> float:
        if self._Calisan__tecrube < 24:
            return self.__prim
        elif self._Calisan__tecrube >= 24 and self._Calisan__tecrube < 48 and self._Calisan__maas < 15000:
            return (self._Calisan__maas % self._Calisan__tecrube) * 5 + self.__prim 
        elif self._Calisan__tecrube >= 48 and self._Calisan__maas < 25000:
            return (self._Calisan__maas % self._Calisan__tecrube) * 4 + self.__prim
        else:
            return 0
        
    def yenimaas(self):
        return self._Calisan__maas + self.zam_hakki()