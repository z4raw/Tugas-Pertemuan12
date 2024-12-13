from Animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
        
    def cetak_Ular(self):
        super().cetak()
        print("Design \t\t\t\t:", self.design,
        "\nRacun \t\t\t\t:", self.racun)
        
anaconda = Ular("anaconda", "Kambing", "Amazon", "Bertelur", "Batik solo", "Tidak berbisa")
anaconda.cetak_Ular()
kobra = Ular("kobra", "tikus", "hutan", "Bertelur", "garis hitam putih", "Tidak berbisa")
kobra.cetak_Ular()