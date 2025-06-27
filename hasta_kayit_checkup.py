hasta_sayisi = int(input(f"Merhaba, hasta kayıt programımıza hoşgeldiniz. \nkaç hasta kayıt edeceksiniz ?" ))
hastalar = []

for hasta in range(hasta_sayisi):
    isim = input("Hastanın ismi : ").upper()
    hasta_sikayetleri = []
    hastanin_sikayet_sayisi = int(input(f"{isim} isimli hastanın şikayet sayısı = "))
    if hastanin_sikayet_sayisi == 0:
        print("Bu hastanın hiçbir şikayeti bulunmuyor")

    for sikayet in range(hastanin_sikayet_sayisi):
        sikayetler = input(f"{isim} ismindeki kullanıcının şikayetleri = ")
        hasta_sikayetleri.append(sikayetler)
    hastalar.append([isim, hasta_sikayetleri])


print("\nKayıtlı hastalar ve şikayetleri:")
for ad, sikayetler in hastalar:
    print(f"- {ad}: {sikayetler}")


