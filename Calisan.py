from Insan import Insan
_sektorler = ["Teknoloji", "Muhasebe", "İnşaat", "Diğer"]
class Calisan(Insan):
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor:str, tecrube:int, maas:float) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        if sektor in _sektorler:
            self._sektor = sektor
        else:
            raise Exception("Sektör bilgisi hatalı.")
        self._tecrube = tecrube
        self._maas = maas

    def sektor_yap(self, sektor:str) -> None:
        if sektor in _sektorler:
            self._sektor = sektor
        else:
            raise Exception("Sektör bilgisi hatalı.")
        
    def sektor_al(self) -> str:
        return self._sektor

    def tecrube_yap(self, tecrube:int) -> None:
        self._tecrube = tecrube

    def tecrube_al(self) -> int:
        return self._tecrube

    def maas_yap(self, maas:float) -> None:
        self._maas = maas

    def maas_al(self) -> float:
        return self._maas
    
    def zam_hakki(self) -> float:
        if self._tecrube < 24:
            return self._maas * 0
        elif self._tecrube >= 24 and self._tecrube < 48 and sel._maas < 15000:
            return self._maas * (self._maas % self._tecrube)
        elif self._tecrube >= 48 and self._maas < 25000:
            return self._maas * (self._maas % self._tecrube) / 2
        else:
            return self._maas * 0
        
    def __str__(self) -> str:
        return f"Ad: {self._ad}\nSoyad: {self._soyad}\nTecrübe: {self._tecrube}\nMaaş: {self._maas + self.zam_hakki()}\n"
