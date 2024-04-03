#ödev2:bilgisayara n adet çift sayı ürettirerek,bu sayıların toplamını bulunuz:

import random
toplam = 0
tekrar = int(input("Kaç adet sayı istiyorsunuz = "))

for i in range(1,tekrar + 1):
    sayi = random.randrange(1,1000)
    print("Sayı =",sayi)
    if sayi % 2 == 0:
        print("Çift sayı =",sayi)
        toplam += sayi
        print("Toplam =",toplam)
