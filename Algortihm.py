from __future__ import division
import time
print("Python Hello World :D")
time.sleep(2)


print("Elma: 30TL")
print("Armut 40 TL")
print("Muz: 60 TL")

elma = (30/100) * (10) + (30)
armut = (40/100) * (10) + (40)
muz = (60/100) * (20) + (60)
elmak = (30/100) * (10)
armutk = (40/100) * (10)
muzk = (60/100) * (20)
time.sleep(3)


print("%10 Kar Elma Fiyatı:" , elma)
print("%10 Kar Armut Fiyatı:" , armut)
print("%20 Kar Muz Fiyatı:" , muz)

while True:
    miktar = int(input("Satılacak Elma Miktarını Giriniz:"))
    miktarx = int(input("Satılacak Armut Sayısını giriniz:"))
    miktarxx = int(input("Satılacak Muz sayısnı giriniz:"))
  
    
    print("Kar Miktarı:" , elmak * miktar + armutk * miktarx + muzk * miktarxx)
    print("Haftalık Ciro:" , (elma * miktar + armut * miktarx + muz * miktarxx) * 7)
    print("Aylık Ciro:" , (elma * miktar + armut * miktarx + muz * miktarxx) * 30)
    print("Yıllık Ciro:" , (elma * miktar + armut * miktarx + muz * miktarxx) *  365)
    
    
    