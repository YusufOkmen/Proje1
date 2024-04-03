#ödev1: bilgisayarın ürettiği 1 ile 5000 arasındaki rasgele 30 sayıdan 7 ye bölünenlerin toplamı 3 yada
#5 e bölünenlerin toplamından kaç fazla yada eksiktir:

import random
toplam1 = 0
toplam2 = 0
sayi = 1

for i in range(1,31):
    x =random.randrange(1,5000)
    if x % 7 == 0:
        toplam1 = toplam1 + x
        print(f"{sayi}. sayı :")
        print(f"{x} sayısı 7 ye tam bölünür.")
        sayi += 1
    if x % 3 == 0 or x % 5 == 0:
        toplam2 = toplam2 + x
        print(f"{sayi}. sayı :")
        print(f"{x} sayısı 3 e veya 5 e bölünür.")
        sayi += 1

if toplam1 > toplam2:
    print(f"toplam1 toplam2 den şu kadar büyüktür = {toplam1 - toplam2}")
elif toplam2 > toplam1:
    print(f"toplam2 toplam1 den şu kadar büyüktür = {toplam2 - toplam1}")
else:
    print(f"İki toplamda birbirine eşittir.")