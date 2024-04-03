#ödev3:bilgisayara 3 farklı sayı ürettiriniz.ilk ürettiği sayı 1.sayı,ikinci ürettiği sayı 2.sayı,3. ürettiği sayı tek ise 1. ve 2. sayıyı toplayın,çift ise çıkartın:

import random
for i in range(1):
    sayi1 = random.randrange(1,1000)
    sayi2 = random.randrange(1,1000)
    sayi3 = random.randrange(1,1000)
    if sayi1 != sayi2 and sayi1 != sayi3 or sayi2 != sayi1 and sayi2 != sayi3:
        print(f"sayı1 = {sayi1},sayı2 = {sayi2},sayi3 = {sayi3}")
        if sayi3 % 2 == 0:
            print(f"sayi1 den sayi2 yi çıkarırsak sonuç = {sayi1 - sayi2}")
        else:
            print(f"sayi1 ile sayi2 nin toplamı = {sayi1 + sayi2}")


