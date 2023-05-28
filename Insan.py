
class Insan():
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:str, uyruk:str) -> None: #İnsan sınıfının yapıcı metodu
        self.__tc_no = tc_no #İnsan sınıfının kimlik numarası niteliği
        self.__ad = ad #İnsan sınıfının ad niteliği
        self.__soyad = soyad #İnsan sınıfının soyad niteliği
        self.__yas = yas #İnsan sınıfının yaş niteliği
        self.__cinsiyet = cinsiyet #İnsan sınıfının cinsiyet niteliği
        self.__uyruk = uyruk #İnsan sınıfının uyruk niteliği

    def get_tc_no(self): return self.__tc_no #İnsan sınıfının kimlik numarası niteliğinin değerini döndüren metot
    def set_tc_no(self, tc_no): self.__tc_no = tc_no #İnsan sınıfının kimlik numarası niteliğinin değerini değiştiren metot
    def get_ad(self): return self.__ad #İnsan sınıfının ad niteliğinin değerini döndüren metot
    def set_ad(self, ad): self.__ad = ad #İnsan sınıfının ad niteliğinin değerini değiştiren metot 
    def get_soyad(self): return self.__soyad #İnsan sınıfının soyad niteliğinin değerini döndüren metot
    def set_soyad(self, soyad): self.__soyad = soyad #İnsan sınıfının soyad niteliğinin değerini değiştiren metot
    def get_yas(self): return self.__yas #İnsan sınıfının yaş niteliğinin değerini döndüren metot
    def set_yas(self, yas): self.__yas = yas #İnsan sınıfının yaş niteliğinin değerini değiştiren metot
    def get_cinsiyet(self): return self.__cinsiyet #İnsan sınıfının cinsiyet niteliğinin değerini döndüren metot
    def set_cinsiyet(self, cinsiyet): self.__cinsiyet = cinsiyet #İnsan sınıfının cinsiyet niteliğinin değerini değiştiren metot
    def get_uyruk(self): return self.__uyruk #İnsan sınıfının uyruk niteliğinin değerini döndüren metot
    def set_uyruk(self, uyruk): self.__uyruk = uyruk #İnsan sınıfının uyruk niteliğinin değerini değiştiren metot

    def __str__(self) -> str: #İnsan sınıfının string metodu (nesneyi yazdırırken çağrılır) 
        return f"TC No: {self.__tc_no}\nAd: {self.__ad}\nSoyad: {self.__soyad}\nYaş: {self.__yas}\nCinsiyet: {self.__cinsiyet}\nUyruk: {self.__uyruk}\n" #İnsan sınıfının niteliklerini yazdırır