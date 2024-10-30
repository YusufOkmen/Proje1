"""
1. Çalışan Maaşı Hesaplama:
   - Bir şirkette çalışan bir kişinin aylık maaşını hesaplayan `maas` isimli bir fonksiyon yazın. Bu fonksiyon, `hammaas`, `mesai` ve `prim` olmak üzere üç parametre alacak. `hammaas`, çalışanın temel maaşını; `mesai`, fazla mesai saatlerine göre ek ücretini; ve `prim`, çalışanın performansına göre aldığı prim miktarını temsil etmektedir. Fonksiyon, çalışanın toplam maaşını (`hammaas + mesai + prim`) hesaplayarak geriye döndürecek. Kullanıcıdan ham maaş, mesai ücreti ve prim miktarını alarak fonksiyonu çağırın ve sonucu ekrana yazdırın.
"""

# Algoritma # Fonksiyon tanımla, hammaas = parametre, bir çalışan yaptığı ek mesai saatini sorgula, çalışan performansı ya iyi ya da kötü olsun eğer kötü ise 0 TL prim eğer iyi ise 1000 tl prim alsın.

def maas(hammaas, mesai, prim):

    mesaisaat = int(input("Kac saat mesai yaptiginizi giriniz: "))
    mesaikazanc = (mesai*mesaisaat)
    if prim == "iyi":
        primmiktar = 1000
    else:
        primmiktar = 0
    toplammaas = (hammaas + mesaikazanc + primmiktar)   
    print(toplammaas)

maas(10000, 200, "kötü")