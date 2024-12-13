from Animal import *

class ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design,warna ):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.warna = warna
        
    def cetak_ikan(self):
        super().cetak()
        print("Design \t\t\t\t:", self.design,
        "\nwarna \t\t\t\t:", self.warna)
        
koi= ikan("koi", "pelet", "air", "Bertelur", "batik", "merah")
koi.cetak_ikan()
nemo= ikan("nemo", "pelet", "air", "Bertelur", "garis garis", "merah putih")
nemo.cetak_ikan()
