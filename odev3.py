"""
3. Sıcaklık Dönüşümü (Fahrenheit to Celsius):
   - "Fahrenheit cinsinden bir sıcaklık değerini Celsius'a dönüştüren `fahrenheit_to_celsius` isimli bir fonksiyon yazın. Bu fonksiyon, `fahrenheit` adında bir parametre alacak ve verilen Fahrenheit değerini Celsius’a çevirecek. Dönüşüm formülü: `Celsius = (Fahrenheit - 32) * 5/9`. Fonksiyonun sonucunu geri döndürün ve kullanıcıdan bir Fahrenheit değeri alarak sonucu ekrana yazdırın."
"""

# Algoritma => Yukarida yazani adim adim gerceklestir.

def fahrenheitToCelsius(fahrenheit):
    celsius =round((fahrenheit - 32) * (5/9), 2)
    print(f"{fahrenheit} Fahrenheit, {celsius} Celsiusdur.")

fahrenheitToCelsius(100)