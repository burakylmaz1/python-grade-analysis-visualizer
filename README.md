# python-grade-analysis-visualizer
A Python-based tool that processes student grades from text files, calculates weighted averages, and generates categorical performance visualizations using Matplotlib.

Bu proje, bir metin dosyası içerisinde yer alan öğrenci notlarını okuyarak harf notlarını hesaplayan, öğrencileri başarı durumlarına göre sınıflandıran ve elde edilen verileri grafiksel olarak sunan bir Python uygulamasıdır.

## Genel Özellikler

- Belirlenen formattaki metin dosyalarından (txt) veri okuma işlemi gerçekleştirir.
- Vize ve final notları üzerinde ağırlıklı hesaplama yaparak nihai başarı notunu belirler.
- Hesaplanan notları akademik standartlara göre harf notuna dönüştürür.
- Başarılı olan öğrencileri ve başarısız (FF) olan öğrencileri ayrı dosyalara (gecenler.txt, kalanlar.txt) raporlar.
- Sınıfın genel başarı dağılımını bar grafik (sütun grafiği) kullanarak görselleştirir.

## Teknik Detaylar

Program içerisinde aşağıdaki temel programlama teknikleri ve kütüphaneler kullanılmıştır:

- Dosya Yönetimi: Okuma ve yazma işlemleri için Python'un yerleşik dosya işleme metotları.
- Hata Yönetimi: Dosya bulunamaması veya hatalı veri girişi gibi durumlara karşı try-except blokları.
- Veri Görselleştirme: Grafik oluşturma süreçleri için Matplotlib kütüphanesi.
- Tip Dönüşümleri: Metin tabanlı verilerin matematiksel işlemlere uygun hale getirilmesi için map ve float fonksiyonları.

## Kurulum ve Kullanım

1. Proje dosyalarını bilgisayarınıza indirin veya klonlayın.
2. Gerekli kütüphaneyi yüklemek için terminale şu komutu yazın:
   pip install matplotlib
3. Veri girişi için "dosya.txt" dosyasının mevcut olduğundan ve "İsim,Not1,Not2,Not3" formatında olduğundan emin olun.
4. Programı çalıştırmak için:
   python grade_calculator.py

## Görsel Örnek
Program çalıştırıldığında oluşturulan başarı dağılım grafiği "basari_grafigi.png" adıyla kaydedilir ve otomatik olarak görüntülenir.
<img width="1000" height="600" alt="basari_grafigi" src="https://github.com/user-attachments/assets/3cae4016-383d-4f38-bafa-69118d7a075b" />

