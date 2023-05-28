from Insan import Insan
_sektorler = ["Teknoloji", "Muhasebe", "İnşaat", "Diğer"] # Sektörler
class Calisan(Insan): # Calisan sınıfı Insan sınıfından kalıtım alıyor.
    def __init__(self, tc_no: str, ad: str, soyad: str, yas: int, cinsiyet: str, uyruk: str, sektor:str, tecrube:int, maas:float) -> None: # Calisan sınıfının yapıcı metodu
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) # Insan sınıfının yapıcı metodunu çağırıyor
        if sektor in _sektorler: # Eğer sektor bilgisi _sektorler listesinde varsa
            self.__sektor = sektor # Calisan sınıfının sektor niteliğine sektor bilgisini ata
        else: # Eğer sektor bilgisi _sektorler listesinde yoksa
            raise Exception("Sektör bilgisi hatalı.") # Hata oluştur
        self._Calisan__tecrube = tecrube # Calisan sınıfının tecrube niteliğine tecrube bilgisini ata
        self._Calisan__maas = maas # Calisan sınıfının maas niteliğine maas bilgisini ata

    def set_sektor(self, sektor:str) -> None: # Calisan sınıfının sektor niteliğinin değerini değiştiren metot
        if sektor in _sektorler: # Eğer sektor bilgisi _sektorler listesinde varsa
            self.__sektor = sektor # Calisan sınıfının sektor niteliğine sektor bilgisini ata
        else: # Eğer sektor bilgisi _sektorler listesinde yoksa
            raise Exception("Sektör bilgisi hatalı.") # Hata oluştur
        
    def get_sektor(self) -> str: # Calisan sınıfının sektor niteliğinin değerini döndüren metot
        return self.__sektor

    def set_tecrube(self, tecrube:int) -> None: # Calisan sınıfının tecrube niteliğinin değerini değiştiren metot
        self._Calisan__tecrube = tecrube

    def get_tecrube(self) -> int: # Calisan sınıfının tecrube niteliğinin değerini döndüren metot
        return self._Calisan__tecrube

    def set_maas(self, maas:float) -> None: # Calisan sınıfının maas niteliğinin değerini değiştiren metot
        self._Calisan__maas = maas

    def get_maas(self) -> float: # Calisan sınıfının maas niteliğinin değerini döndüren metot
        return self._Calisan__maas
    
    def zam_hakki(self) -> float: # Calisan sınıfının zam_hakki niteliğinin değerini hesaplayan metot
        if self._Calisan__tecrube < 24: # Eğer tecrube bilgisi 24 aydan azsa
            return 0
        elif self._Calisan__tecrube >= 24 and self._Calisan__tecrube < 48 and self._Calisan__maas < 15000: # Eğer tecrube bilgisi 24 aydan fazla ve 48 aydan azsa ve maaş bilgisi 15000'den azsa
            return (self._Calisan__maas % self._Calisan__tecrube) # Zam hakkı maaşın tecrübeye bölümünden kalan
        elif self._Calisan__tecrube >= 48 and self._Calisan__maas < 25000: # Eğer tecrube bilgisi 48 aydan fazla ve maaş bilgisi 25000'den azsa
            return (self._Calisan__maas % self._Calisan__tecrube) / 2 # Zam hakkı maaşın tecrübeye bölümünden kalanın yarısı
        else: 
            return 0
        
    def yenimaas(self): return self._Calisan__maas * (1 + self.zam_hakki() / 100) # Calisan sınıfının yenimaas niteliğinin değerini hesaplayan metot 
        
    def __str__(self) -> str: # Calisan sınıfının string dönüş değerini hesaplayan metot
        return f"Ad: {self._Insan__ad}\nSoyad: {self._Insan__soyad}\nTecrübe: {self._Calisan__tecrube}\nYeni Maaş: {self.yenimaas():.2f}\n" # String dönüş değeri
