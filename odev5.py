"""
5. İndirimli Fiyat Hesaplama:
   - "Bir ürünün indirimli fiyatını hesaplayan `indirimli_fiyat` isimli bir fonksiyon yazın. Bu fonksiyon, `fiyat` ve `indirim_orani` olmak üzere iki parametre alacak. `indirim_orani`, indirim yüzdesini temsil edecek ve bu oranı kullanarak ürünün indirimli fiyatını hesaplayacak (`fiyat - (fiyat * indirim_orani / 100)`). Fonksiyon sonucunu geriye döndürecek. Kullanıcıdan ürün fiyatı ve indirim oranını alarak, bu fonksiyonu çağırın ve sonucu ekrana yazdırın."
"""

# Algoritma => Yukaridaki yaziyi adim adim gerceklestir.

def indirimliFiyat(fiyat, indirim):
    yeniFiyat = fiyat - (fiyat * indirim / 100)
    print(yeniFiyat)

indirimliFiyat(100, 10)