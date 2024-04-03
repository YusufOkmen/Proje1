kalemf = int(input("Kalemin adet fiyatı ne kadardır = "))
kalema = int(input("Kalemden kaç adet satın aldınız = "))
defterf = int(input("Defterin adet fiyatı ne kadardır = "))
deftera = int(input("Defterden kaç adet satın aldınız = "))
kitapf = int(input("Kitabın adet fiyatını giriniz = "))
kitapa = int(input("Kitaptan kaç adet satın aldınız = "))
silgif = int(input("Silginin adet fiyatı ne kadardır = "))
silgia = int(input("Silgiden kaç adet satın aldınız = "))
toplam_borc = (kalemf * kalema) + (kitapf * kitapa) + (defterf * deftera) + (silgif * silgia)
asil_borc = toplam_borc + toplam_borc * 8 / 100
if toplam_borc < 1000:
    print("İndirim kazanmadınız."),
    print(f"borcunuz {round(asil_borc,2)} TL kadardır.(KDV dahil)")
elif toplam_borc >= 1000 and toplam_borc < 2000:
    print("Tebrikler,%10 İndirim kazandınız.")
    print(f"İndirimsiz borcunuz {round(asil_borc,2)} TL kadardır.(KDV dahil)")
    indirim_a =toplam_borc - (toplam_borc * 10 / 100)
    print(f"İndirimli borcunuz {round(indirim_a + (indirim_a * 8 / 100),2)} TL kadardır.(KDV dahil)")
elif toplam_borc >= 2000 and toplam_borc < 3000:
    print("Tebrikler %20 inddirim kazandınız.")
    print(f"İndirimsiz borcunuz {round(asil_borc,2)} TL kadardır.(KDV dahil)")
    indirim_b = toplam_borc - (toplam_borc * 20 / 100)
    print(f"İndirimli borcunuz {round(indirim_b + (indirim_b * 8 / 100),2)} TL kadardır.(KDV dahil)")
elif toplam_borc >= 3000 :
    print("Tebrikler %30 indirim kazandınız.")
    print(f"İndirimsiz borcunuz {round(asil_borc,2)} TL kadardır.(KDV dahil)")
    indirim_c = toplam_borc - (toplam_borc * 30 / 100)
    print(f"İndirimli borcunuz {round(indirim_c + (indirim_c * 8 / 100),2)} TL kadardır.(KDV dahil)")
if (kitapa * kitapf) > 4000:
    print("Tebrikler.Ekstra %15 indirim kazandınız.")
    bonus_indirim = indirim_c - (indirim_c * 15 / 100)
    print(f"Ekstra indirimli borcunuz {round(bonus_indirim + bonus_indirim * 8 / 100,2)} TL kadardır.(KDV dahil)")
