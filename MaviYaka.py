from Calisan import Calisan

class MaviYaka(Calisan): # Calisan sınıfından kalıtım
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor: str, tecrube: int, maas: float, yipranma:float) -> None: #MaviYaka sınıfının yapıcı metodu
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) #Calisan sınıfının yapıcı metodunu çağırır
        self.__yipranma = yipranma #yipranma niteliğini tanımlar

    def set_yipranma(self, yipranma:float) -> None: #yipranma niteliğinin değerini değiştiren metot
        self.__yipranma = yipranma

    def get_yipranma(self) -> float: #yipranma niteliğinin değerini döndüren metot
        return self.__yipranma
    
    def zam_hakki(self) -> float: # Calisan sınıfının zam_hakki niteliğinin değerini hesaplayan metot
        if self._Calisan__tecrube < 24: #Eğer tecrube bilgisi 24 aydan azsa
            return self.__yipranma * 10
        elif self._Calisan__tecrube >= 24 and self._Calisan__tecrube < 48 and self._Calisan__maas < 15000: #Eğer tecrube bilgisi 24 aydan fazla ve 48 aydan azsa ve maaş bilgisi 15000'den azsa
            return (self._Calisan__maas % self._Calisan__tecrube) / 2 + self.__yipranma * 10
        elif self._Calisan__tecrube >= 48 and self._Calisan__maas < 25000: #Eğer tecrube bilgisi 48 aydan fazla ve maaş bilgisi 25000'den azsa
            return (self._Calisan__maas % self._Calisan__tecrube) / 3 + self.__yipranma * 10
        else:
            return 0