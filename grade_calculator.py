def not_hesapla(satır):
    satır = satır.strip()
    if not satır: return None

    liste = satır.split(",")
    isim = liste[0]
    n1, n2, n3 = map(float, liste[1:])

    son_not = n1 * 0.3 + n2 * 0.3 + n3 * 0.4


    if son_not >= 90:
        harf = "AA"

    elif son_not >= 85:
        harf = "BA"

    elif son_not >= 80:
        harf = "BB"

    elif son_not >= 75:
        harf = "CB"

    elif son_not >= 70:
        harf = "CC"

    elif son_not >= 65:
        harf = "DC"

    elif son_not >= 60:
        harf = "DD"

    elif son_not >= 55:
        harf = "FD"

    else:
        harf = "FF"

    return f"{isim} ---------> {harf}\n", harf



gecenler = []
kalanlar = []

try:
    with open("dosya.txt", "r", encoding="utf-8") as file:
        for satir in file:
            sonuc = not_hesapla(satir)

            if sonuc:
                metin, harf = sonuc
                if harf == "FF":
                    kalanlar.append(metin)
                else:
                    gecenler.append(metin)


    with open("gecenler.txt", "w", encoding="utf-8") as f1:
        f1.writelines(gecenler)

    with open("kalanlar.txt", "w", encoding="utf-8") as f2:
        f2.writelines(kalanlar)

    print("İşlem başarıyla tamamlandı. 'gecenler.txt' ve 'kalanlar.txt' oluşturuldu.")
    print(f"Toplam Öğrenci: {len(gecenler) + len(kalanlar)}")

except FileNotFoundError:
    print("Hata: 'dosya.txt' bulunamadı!")

import matplotlib.pyplot as plt


def grafik_olustur(gecenler, kalanlar):

    tum_notlar = []
    for satir in gecenler + kalanlar:
        harf = satir.split("--------->")[-1].strip()
        tum_notlar.append(harf)


    harf_siralamasi = ["AA", "BA", "BB", "CB", "CC", "DC", "DD", "FD", "FF"]
    sayilar = [tum_notlar.count(h) for h in harf_siralamasi]


    renkler = []
    for harf in harf_siralamasi:
        if harf in ["AA", "BA", "BB", "CB"]:
            renkler.append('green')
        elif harf in ["CC", "DC", "DD", "FD"]:
            renkler.append('yellow')
        else:
            renkler.append('red')


    plt.figure(figsize=(10, 6))
    bars = plt.bar(harf_siralamasi, sayilar, color=renkler, edgecolor='black', alpha=0.7)


    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, yval, ha='center', va='bottom')


    plt.title("Sınıf Başarı Dağılımı", fontsize=14, fontweight='bold')
    plt.xlabel("Harf Notları", fontsize=12)
    plt.ylabel("Öğrenci Sayısı", fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.6)


    plt.savefig("basari_grafigi.png")
    print("\nGrafik 'basari_grafigi.png' adıyla kaydedildi.")
    plt.show()

grafik_olustur(gecenler, kalanlar)










