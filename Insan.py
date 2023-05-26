
class Insan():
    def __init__(self, tc_no:str, ad:str, soyad:str, yas:int, cinsiyet:str, uyruk:str) -> None:
        self._tc_no = tc_no
        self._ad = ad
        self._soyad = soyad
        self._yas = yas
        self._cinsiyet = cinsiyet
        self._uyruk = uyruk

    def get_tc_no(self): return self._tc_no
    def set_tc_no(self, tc_no): self._tc_no = tc_no
    def get_ad(self): return self._ad
    def set_ad(self, ad): self._ad = ad
    def get_soyad(self): return self._soyad
    def set_soyad(self, soyad): self._soyad = soyad
    def get_yas(self): return self._yas
    def set_yas(self, yas): self._yas = yas
    def get_cinsiyet(self): return self._cinsiyet
    def set_cinsiyet(self, cinsiyet): self._cinsiyet = cinsiyet
    def get_uyruk(self): return self._uyruk
    def set_uyruk(self, uyruk): self._uyruk = uyruk

    def __str__(self) -> str:
        return f"TC No: {self._tc_no}\nAd: {self._ad}\nSoyad: {self._soyad}\nYaş: {self._yas}\nCinsiyet: {self._cinsiyet}\nUyruk: {self._uyruk}"