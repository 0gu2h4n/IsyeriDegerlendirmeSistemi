from Calisan import Calisan

class BeyazYaka(Calisan): # Calisan sınıfından kalıtım 
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor: str, tecrube: int, maas: float, prim:int) -> None: #BeyazYaka sınıfının yapıcı metodu
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas) #Calisan sınıfının yapıcı metodunu çağırır
        self.__prim = prim #prim niteliğini tanımlar

    def set_prim(self, prim:int) -> None: #prim niteliğinin değerini değiştiren metot
        self.__prim = prim

    def get_prim(self) -> int: #prim niteliğinin değerini döndüren metot
        return self.__prim
    
    def zam_hakki(self) -> float: # Calisan sınıfının zam_hakki niteliğinin değerini hesaplayan metot
        if self._Calisan__tecrube < 24: #Eğer tecrube bilgisi 24 aydan azsa
            return self.__prim
        elif self._Calisan__tecrube >= 24 and self._Calisan__tecrube < 48 and self._Calisan__maas < 15000: #Eğer tecrube bilgisi 24 aydan fazla ve 48 aydan azsa ve maaş bilgisi 15000'den azsa
            return (self._Calisan__maas % self._Calisan__tecrube) * 5 + self.__prim 
        elif self._Calisan__tecrube >= 48 and self._Calisan__maas < 25000: #Eğer tecrube bilgisi 48 aydan fazla ve maaş bilgisi 25000'den azsa
            return (self._Calisan__maas % self._Calisan__tecrube) * 4 + self.__prim
        else:
            return 0
        
    def yenimaas(self): # Calisan sınıfının maas niteliğinin değerini hesaplayan metot
        return self._Calisan__maas + self.zam_hakki()