"""
. Dikdörtgenin Alanı ve Çevresi Hesaplama:
   - Bir dikdörtgenin alanını ve çevresini hesaplayan iki ayrı fonksiyon yazın: `alan_hesapla` ve `cevre_hesapla`. Her iki fonksiyon da `uzunluk` ve `genislik` adında iki parametre alacak. `alan_hesapla`, dikdörtgenin alanını (`uzunluk * genislik`) hesaplayacak ve geri döndürecek. `cevre_hesapla` ise çevreyi (`2 * (uzunluk + genislik)`) hesaplayarak geri döndürecek. Kullanıcıdan uzunluk ve genişlik değerlerini alarak, her iki fonksiyonu çağırın ve alan ile çevreyi ekrana yazdırın.
"""

# Algoritma => main fonksiyonu tanımla, main fonksiyonun icine alanHesapla ve cevreHesapla fonksiyonalini tanimla, bu uc fonksiyonun parametreside uzun kenar ve kisa kenar olacak, alanHesapla fonksiyonunda dikdortgenin alanini ve cevreHesapla fonksyionunda dikdortgenin cevresini hesapla.


def main():

    uzunKenar = int(input("Dikdortgenin uzun kenarini giriniz: "))
    kisaKenar = int(input("Dikdortgenin kisa kenarini giriniz: "))

    def alanHesapla(uzunKenar, kisaKenar):
        alan = (uzunKenar * kisaKenar)
        print(f"Dikdortgeninizin alani: {alan}")
    def cevreHesapla(uzunKenar, kisaKenar):
        cevre = (2 * (kisaKenar + uzunKenar))
        print(f"Dikdortgeninizin cevresi: {cevre}")

    alanHesapla(uzunKenar, kisaKenar)
    cevreHesapla(uzunKenar, kisaKenar)

main()