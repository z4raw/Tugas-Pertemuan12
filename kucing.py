from Animal import *

class kucing(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, suara, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.suara = suara
        self.warna = warna
        
    def cetak_kucing(self):
        super().cetak()
        print("suara \t\t\t\t:", self.suara,
        "\nwarna \t\t\t\t:", self.warna)
        
Persia = kucing("persia", "daging", "darat", "melahirkan", "meonggmeong", "putih ke abuan")
Persia.cetak_kucing()
kampung = kucing("kampung", "daging dll", "darat", "melahirkan", "meongmeong", "kuning")
kampung.cetak_kucing()