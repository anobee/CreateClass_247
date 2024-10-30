class PersegiPanjang:
    def __init__(self, panjang, lebar):  
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
        return self.panjang * self.lebar

    def __str__(self):  
        return f"Persegi Panjang, panjang {self.panjang} cm, dan lebar {self.lebar} cm"

if __name__ == "__main__":  
    try:
       
        panjang = float(input("Masukkan panjang persegi panjang (cm): "))
        lebar = float(input("Masukkan lebar persegi panjang (cm): "))
        
    
        if panjang <= 0 or lebar <= 0:
            print("Error: Panjang dan lebar harus lebih besar dari 0.")
        else:
            persegi_panjang = PersegiPanjang(panjang, lebar)
            print(persegi_panjang)
            print("Keliling:", persegi_panjang.hitung_keliling(), "cm")
            print("Luas:", persegi_panjang.hitung_luas(), "cm^2")
    
    except ValueError:
        print("Error: Input harus berupa angka.")