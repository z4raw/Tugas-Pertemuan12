from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak,jenis, warna, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna
        self.bunyi = bunyi
        
    def cetak_Burung(self):
        super().cetak()
        print("jenis \t\t\t\t:", self.jenis,
        "\nwarna \t\t\t\t:", self.warna,
        "\nbunyi \t\t\t\t:", self.bunyi)
kakatua = Burung("kakatua", "biji-bijian", "pohon", "Bertelur", "ordo Psittaciformes dan famili Cacatuidae", "pink","amammama")
kakatua.cetak_Burung()
gagak = Burung("gagak", "serangga", "hutan", "Bertelur", "passeriformes", "hitam","aerawwaaaaa")
gagak.cetak_Burung()