from Insan import Insan

class Issiz(Insan): #Issiz sınıfı İnsan sınıfından kalıtım aldı
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:str, uyruk:str, maviYaka:float = 0.0, beyazYaka:float = 0.0, yonetici:float=0.0) -> None: #Issiz sınıfının yapıcı metodu
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk) #Kalıtım aldığı sınıfın yapıcı metodunu çağırdı
        self.__tecrube = {"maviyaka" : maviYaka, "beyazyaka" : beyazYaka, "yönetici" : yonetici} #Issiz sınıfının tecrübe niteliği
        self.statu = self.statu_bul() #Issiz sınıfının statü niteliği

    def tecrube_ekle(self, statu:str, yil:int) -> None: #Issiz sınıfının tecrübe ekleme metodu
        try: #Hata yakalama bloğu 
            self.__tecrube[statu] += yil #Tecrübe niteliğinin değerini arttırdı
            self.statu = self.statu_bul() #Statü niteliğinin değerini güncelledi
        except KeyError: 
            print("Hatalı statü girişi yapıldı. Lütfen statüyü kontrol ediniz.") 

    def tecrube_al(self, statu:str) -> float: #Issiz sınıfının tecrübe alma metodu
        try: #Hata yakalama bloğu
            return self.__tecrube[statu] #Tecrübe niteliğinin değerini döndürdü
        except KeyError:
            print("Hatalı statü girişi yapıldı. Lütfen statüyü kontrol ediniz.") 

    def statu_bul(self) -> str: #Issiz sınıfının statü bulma metodu
        if not self.__tecrube["yönetici"] and not self.__tecrube["beyazyaka"] and not self.__tecrube["maviyaka"]: #Tecrübe niteliğinin değerleri 0 ise
            return "Tecrübesiz"
        elif self.__tecrube["yönetici"] * 0.45 >= self.__tecrube["maviyaka"] * 0.2 and self.__tecrube["yönetici"] * 0.45 >= self.__tecrube["beyazyaka"] * 0.35: #Yönetici tecrübesi diğerlerinden fazla ise (Ağırlığına göre)
            return "Yönetici"
        elif self.__tecrube["beyazyaka"] * 0.35 > self.__tecrube["yönetici"] * 0.45 and self.__tecrube["beyazyaka"] * 0.35 >= self.__tecrube["maviyaka"] * 0.2: #Beyaz yaka tecrübesi diğerlerinden fazla ise (Ağırlığına göre)
            return "Beyaz Yaka"
        elif self.__tecrube["maviyaka"] * 0.2 > self.__tecrube["yönetici"] * 0.45 and self.__tecrube["maviyaka"] * 0.2 > self.__tecrube["beyazyaka"] * 0.35: #Mavi yaka tecrübesi diğerlerinden fazla ise (Ağırlığına göre)
            return "Mavi Yaka"
        
    def __str__(self) -> str: #Issiz sınıfının yazdırma metodu
        return f"Ad: {self._Insan__ad}\nSoyad: {self._Insan__soyad}\nStatü: {self.statu_bul()}\n" #Issiz sınıfının niteliklerini yazdırdı