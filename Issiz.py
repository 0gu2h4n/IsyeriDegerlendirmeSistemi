from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:int, uyruk:str, maviYaka:float, beyazYaka:float, yonetici:float) -> None:
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self._tecrube = {"maviyaka" : maviYaka, "beyazyaka" : beyazYaka, "yonetici" : yonetici}


