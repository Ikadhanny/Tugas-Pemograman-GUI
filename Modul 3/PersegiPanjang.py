class PersegiPanjang :

  # Variable biasa
  counter = 0

  # Constructor
  def __init__(self, p, l) :
    # mendefinisikan atribut kelas
    self.panjang = p
    self.lebar = l
  
# Encapsulation
  # Setter
  def ubahPanjang (self, p) :
    self.panjang = p
  
  def ubahLebar (self, l) :
    self.lebar = 1
#-- End Encapsulation

  def hitungLuas(self) :
    return self.panjang * self.lebar
  
  def hitungKeliling(self) :
    return 2 * (self.panjang + self.lebar)
  
  def cetakLuas(self) :
    print(f'Luas Persegi Panjang\t : {self.hitungLuas()} ')

  def cetakKeliling(self) :
    print(f'Keliling Persegi Panjang\t : {self.hitungKeliling()} ')

objekPP1 = PersegiPanjang(10, 8)

objekPP2 = PersegiPanjang(9. 8)

objekPP3 = persegiPanjang(8, 8)

# objekPP.cetakLuas()

# objekPP.cetakKeliling()

# objekPP.counter = 10

print (objekPP1.counter)
print (objekPP2.counter)
print (objekPP3.counter)



# main
# import PersegiPanjang

# objekPP = PersegiPanjang(10, 8)