import math

"""
4. Faktöriyel Hesaplama:
   - "Bir sayının faktöriyelini hesaplayan `faktoriyel` isimli bir fonksiyon yazın. Fonksiyon, bir `sayi` parametresi alacak ve bu sayının faktöriyelini hesaplayarak döndürecek. Faktöriyel, bir sayının kendisinden önceki pozitif tam sayılarla çarpımıdır. Örneğin, 5’in faktöriyeli 5! = 5 x 4 x 3 x 2 x 1 = 120'dir. Kullanıcıdan bir sayı alıp bu sayının faktöriyelini hesaplayan fonksiyonu çağırın ve sonucu ekrana yazdırın."
"""

# Algoritma => Oncelikle faktoriyelin sonucu olan toplami globalde 0 olarak tanimlariz, sonrasinde while dongusu kullanarak 'x' sayimiz 0 dan buyuk iken x * (x-1) ve esittir toplam sonrasinda x - 1 ve boyle 0 olana kadar devam.

toplam = 0

def faktoriyel(sayi):
    
    faktor = math.factorial(sayi)
    
    print(faktor)

faktoriyel(5)

# Kusura bakmayin hocam import etmek cok kolay geldi.

