from Insan import Insan
_sektorler = ["Teknoloji", "Muhasebe", "İnşaat", "Diğer"]
class Calisan(Insan):
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor:str, tecrube:int, maas:float) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        if sektor in _sektorler:
            self.__sektor = sektor
        else:
            raise Exception("Sektör bilgisi hatalı.")
        self._Calisan__tecrube = tecrube
        self._Calisan__maas = maas

    def sektor_yap(self, sektor:str) -> None:
        if sektor in _sektorler:
            self.__sektor = sektor
        else:
            raise Exception("Sektör bilgisi hatalı.")
        
    def sektor_al(self) -> str:
        return self.__sektor

    def tecrube_yap(self, tecrube:int) -> None:
        self._Calisan__tecrube = tecrube

    def tecrube_al(self) -> int:
        return self._Calisan__tecrube

    def maas_yap(self, maas:float) -> None:
        self._Calisan__maas = maas

    def maas_al(self) -> float:
        return self._Calisan__maas
    
    def zam_hakki(self) -> float:
        if self._Calisan__tecrube < 24:
            return 0
        elif self._Calisan__tecrube >= 24 and self._Calisan__tecrube < 48 and self._Calisan__maas < 15000:
            return (self._Calisan__maas % self._Calisan__tecrube)
        elif self._Calisan__tecrube >= 48 and self._Calisan__maas < 25000:
            return (self._Calisan__maas % self._Calisan__tecrube) / 2
        else:
            return 0
        
    def yenimaas(self): return self._Calisan__maas * (1 + self.zam_hakki() / 100)
        
    def __str__(self) -> str:
        return f"Ad: {self._Insan__ad}\nSoyad: {self._Insan__soyad}\nTecrübe: {self._Calisan__tecrube}\nYeni Maaş: {self.yenimaas():.2f}\n"
