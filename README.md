# Secure-File-Transfer-System
AES-256-EAX şifreleme, RSA-2048 kimlik doğrulama ve düşük seviyeli IP işleme özelliklerine sahip gelişmiş güvenli dosya transfer sistemi.


# Gelişmiş Güvenli Dosya Transfer Sistemi (Advanced Secure File Transfer System)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/siracgezgin/Secure-File-Transfer-System?style=social)](https://github.com/siracgezgin/Secure-File-Transfer-System/stargazers)
[![GitHub forks](https://img.shields.io/badge/Forks-0-blue?style=social)](https://github.com/siracgezgin/Secure-File-Transfer-System/network/members)
[![GitHub watchers](https://img.shields.io/github/watchers/siracgezgin/Secure-File-Transfer-System?style=social)](https://github.com/siracgezgin/Secure-File-Transfer-System/watchers)

## 🌟 Proje Özeti

[cite_start]Bu proje, Bursa Teknik Üniversitesi Bilgisayar Mühendisliği Bölümü'nde `BLM0326 Bilgisayar Ağları Dersi` kapsamında **Siraç Gezgin** tarafından geliştirilmiş, gelişmiş bir güvenli dosya transfer sistemidir[cite: 1, 2]. [cite_start]Sistem, modern ağ güvenliği prensiplerini düşük seviyeli ağ programlama teknikleriyle birleştirerek, hem akademik hem de pratik değeri yüksek, tam fonksiyonel bir çözüm sunmaktadır[cite: 5, 7].

[cite_start]AES-256-EAX ve RSA-2048 tabanlı şifreleme ve kimlik doğrulama, manuel IP başlık manipülasyonu (Scapy ile [cite: 13, 25][cite_start]), gerçek zamanlı performans analizi (iPerf3, Wireshark, netem ile [cite: 16, 27][cite_start]) ve kapsamlı güvenlik testleri gibi özellikleriyle endüstriyel standartlarda güvenli dosya transferi gerçekleştirmektedir[cite: 4, 8]. [cite_start]Ayrıca adaptif TCP/UDP seçim mekanizması, dinamik sıkıştırma ve makine öğrenmesine dayalı anomali tespiti gibi bonus özelliklerle sistemin güvenlik, kararlılık ve performansı önemli ölçüde artırılmıştır[cite: 4].

## ✨ Ana Özellikler

[cite_start]Sistem, modüler bir yaklaşımla tasarlanmış olup dört ana modülden oluşmaktadır[cite: 4, 9]:

1.  [cite_start]**Güvenlik Katmanı**[cite: 4, 10]:
    * **Şifreleme:** AES-256-EAX modu kullanılarak dosyalar şifrelenir. [cite_start]Bu mod, hem gizliliği hem de bütünlüğü eş zamanlı garanti eder[cite: 10].
    * [cite_start]**Anahtar Yönetimi:** Kullanıcı parolasından SHA-256 ile 256-bit AES anahtarı türetilir[cite: 11]. [cite_start]Şifreleme anahtarları, RSA ile güvenli bir şekilde paylaşılır[cite: 12].
    * **Bütünlük ve Kimlik Doğrulama:** Transfer öncesi ve sonrası SHA-256 hash kontrolleri yapılır. [cite_start]Yetkisiz erişimleri engellemek için RSA sertifika tabanlı kimlik doğrulama (2048-bit RSA anahtar çiftleri) ve X.509 sertifika zincirleri ile güven ağı uygulanır[cite: 12, 23, 59].

2.  [cite_start]**Ağ İşlem Katmanı**[cite: 4, 13]:
    * [cite_start]**IP Başlık Manipülasyonu:** Scapy kütüphanesi kullanılarak bayraklar (flags), Time-To-Live (TTL) ve checksum gibi IP başlık alanları dinamik olarak ayarlanır[cite: 13, 24, 25].
    * **Paket Parçalama ve Yeniden Birleştirme:** 1 MB üzeri dosyalar, 1024 B'lık parçalar halinde iletilir. Alıcıda doğru sıra ve bütünlük kontrolü sağlanarak yeniden birleştirme yapılır. [cite_start]Sıralı paket numaralandırması, ACK/NACK mekanizması ile kayıp paket tespiti ve timeout/retry mekanizması ile otomatik yeniden gönderim sağlanır[cite: 14, 15, 25].

3.  [cite_start]**Performans İzleme Katmanı**[cite: 4, 16]:
    * [cite_start]**Araçlar:** iPerf3, Wireshark ve Linux'un `netem` komutu kullanılarak gerçek zamanlı ağ metrikleri toplanır[cite: 16, 58, 64, 65].
    * [cite_start]**Metrikler:** Bant genişliği, gecikme süresi (latency) ve paket kaybı gibi önemli ağ performans göstergeleri izlenir[cite: 4, 17].

4.  [cite_start]**Saldırı Simülasyonu Katmanı**[cite: 4, 18]:
    * [cite_start]**Senaryolar:** Man-in-the-Middle (MITM) ve paket enjeksiyonu saldırıları prototip üzerinde denenmiştir[cite: 18, 28].
    * [cite_start]**Savunma:** Şifreleme ile veri okunamaz hale gelir; bütünlük kontrolünde tutarsızlık algılandığında transfer anında durdurulur[cite: 19]. [cite_start]Tüm saldırı denemelerinde sistem, yetkisiz erişimi engelleyip hatalı transferi durdurarak doğru tepki vermiştir[cite: 21].

## 💡 Bonus Özellikler

[cite_start]Proje, temel gereksinimlerin ötesinde aşağıdaki bonus özelliklerle zenginleştirilmiştir[cite: 6, 37]:

* **Adaptif TCP/UDP Seçim Mekanizması:** Ağ koşullarına (gecikme, paket kaybı, bant genişliği) göre otomatik olarak en uygun protokol (TCP/UDP hibrit) seçimi yapılır. [cite_start]Bu, ortalama %23 performans artışı sağlamıştır[cite: 4, 29, 30, 37].
* [cite_start]**Dinamik Sıkıştırma:** Ağ koşullarına göre LZ4 (hızlı), ZSTD (dengeli) ve GZIP (maksimum sıkıştırma) algoritmaları arasında adaptif seçim yaparak %35 bant genişliği tasarrufu sağlamıştır[cite: 4, 31, 38].
* [cite_start]**Gerçek Zamanlı Anomali Tespiti:** Makine öğrenmesine dayalı anomali tespiti ile %96 doğrulukta tehdit algılama başarılmıştır[cite: 4, 31, 40].
* **Kullanıcı Dostu Grafik Arayüzü (GUI):** HTML, CSS ve JavaScript kullanılarak geliştirilen interaktif arayüz, dosya transferi, güvenlik durumu, ağ performansı ve sistem loglarını gerçek zamanlı olarak sunar. [cite_start]Bu arayüz, sistemin benimsenme oranını %90'a çıkarmıştır[cite: 31, 39].

## 📈 Performans ve Güvenlik Test Sonuçları

[cite_start]Final testlerinde sistemin performansı ve güvenliği detaylı olarak analiz edilmiştir[cite: 41, 42]:

| Test Senaryosu        | Ara Rapor   | Final Rapor   | İyileştirme |
| :-------------------- | :---------- | :------------ | :---------- |
| Wi-Fi Bandwidth       | 32 Mbps     | 45 Mbps       | +40.6%      |
| Kablolu Bandwidth     | 77 Mbps     | 94 Mbps       | +22.1%      |
| VPN Bandwidth         | 18 Mbps     | 28 Mbps       | +55.6%      |
| Wi-Fi Latency         | 6-9 ms      | 4-6 ms        | -33.3%      |
| Kablolu Latency       | 1-2 ms      | 0.8-1.5 ms    | -20%        |
| VPN Latency           | 27 ms       | 22 ms         | -18.5%      |
| Paket Kaybı (Wi-Fi)   | 0.3%        | 0.12%         | -60%        |
| Paket Kaybı (Kablolu) | 0.08%       | 0.03%         | -62.5%      |
| Paket Kaybı (VPN)     | 0.07%       | 0.05%         | -28.6%      |

[cite_start]**Güvenlik Testleri**[cite: 43]:
* **MITM Saldırı Tespiti:** %100 başarı oranı
* **Paket Enjeksiyonu Korunması:** %100 başarı oranı
* **Brute Force Saldırı Dayanıklılığı:** 2^128 bit güvenlik seviyesi
* **Side Channel Saldırı Korunması:** Timing attack korunması aktif

## 🛠️ Kurulum ve Çalıştırma

Bu projeyi yerel makinenizde kurmak ve çalıştırmak için aşağıdaki adımları takip edin.

### Önkoşullar

* Python 3.x yüklü olmalı.
* `pip` (Python paket yöneticisi) yüklü olmalı.
* [cite_start]Linux tabanlı bir işletim sistemi (Raw socket kullanımı nedeniyle Linux'ta optimal çalışır)[cite: 31].

### Gerekli Kütüphaneler

Projeyi çalıştırmak için aşağıdaki Python kütüphanelerini kurmanız gerekmektedir:

```bash
pip install scapy pycryptodome psutil iperf3
```
* [cite_start]`scapy`: Düşük seviyeli IP işleme ve paket manipülasyonu için[cite: 63].
* [cite_start]`pycryptodome`: AES ve RSA şifreleme/kimlik doğrulama işlemleri için[cite: 60].
* `psutil`: Sistem ve ağ performans metriklerini toplamak için.
* [cite_start]`iperf3`: Ağ bant genişliği ölçümleri için (Python sarmalayıcısı)[cite: 58].

### Proje Dosyaları

Proje dizin yapısı aşağıdaki gibidir:

```
Gelişmiş Güvenli Dosya Transfer Sistemi/
├── main.py                     # Ana uygulama mantığı ve GUI entegrasyonu (varsa)
├── ip_paket.py                 # Ağ İşlem Katmanı: IP başlık manipülasyonu
├── performans_izleme.py        # Performans İzleme Katmanı: Metrik toplama
├── mitm.py                     # Saldırı Simülasyonu: MITM saldırı tespiti
├── protokol.py                 # Bonus Özellik: Dinamik TCP/UDP protokol seçimi
├── index.html                  # Kullanıcı Arayüzü (HTML)
├── SiracGezgin_22360859058_BLM0326_Bilgisayar Ağları Dönem Projesi Final Raporu.docx # Final Raporu
└── README.md                   # Bu dosya
```

### Çalıştırma Adımları

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/siracgezgin/Secure-File-Transfer-System.git](https://github.com/siracgezgin/Secure-File-Transfer-System.git)
    cd Secure-File-Transfer-System
    ```
    *`siracgezgin` yerine kendi GitHub kullanıcı adınızı yazmayı unutmayın.*

2.  **Kullanıcı Arayüzünü Başlatın:**
    Web tabanlı kullanıcı arayüzünü (GUI) çalıştırmak için `index.html` dosyasını tercih ettiğiniz herhangi bir modern web tarayıcısında (Chrome, Firefox vb.) açmanız yeterlidir.
    ```bash
    # Linux/macOS
    xdg-open index.html 
    # Windows
    start index.html
    ```
    *Eğer Python kodu GUI ile entegre edilmişse, `main.py` dosyasını çalıştırmanız gerekebilir. Bu durumda, `main.py` dosyasında GUI'yi başlatan bir komut olması gerekir.*

3.  **Python Modüllerini Çalıştırın (Arka Uç İçin):**
    Projenin Python tabanlı arka uç modüllerini (şifreleme, ağ işleme, performans izleme vb.) çalıştırmak için `main.py` dosyasını terminalden başlatmanız gerekecektir.
    ```bash
    python main.py
    ```
    *Bu adım, GUI'nin arka uç servisleriyle iletişim kurabilmesi için önemlidir.*

## 🛣️ Gelecek Çalışma Önerileri

[cite_start]Projenin gelecekteki potansiyel geliştirmeleri ve araştırma alanları şunlardır[cite: 48]:

### Kısa Vadeli Geliştirmeler (3-6 Ay)
* **Mobil Platform Desteği:** Android/iOS için native uygulama geliştirme.
* **Bulut Entegrasyonu:** AWS/Azure gibi bulut depolama servisleriyle entegrasyon.
* **API Geliştirme:** Üçüncü taraf entegrasyonları için RESTful API sağlama.

### Orta Vadeli Araştırmalar (6-12 Ay)
* [cite_start]**Kuantum Kriptografisi:** Post-quantum algoritmalarının entegrasyonu[cite: 31, 49].
* **Yapay Zeka Destekli Güvenlik:** Makine öğrenmesi tabanlı tehdit tespiti için daha gelişmiş modeller.
* [cite_start]**Blockchain Entegrasyonu:** Merkezi olmayan güven yönetimi için dağıtık defter teknolojileri kullanımı[cite: 31, 49].

### Uzun Vadeli Vizyon (1-2 Yıl)
* **IoT Ekosistemi Entegrasyonu:** Nesnelerin İnterneti (IoT) cihazlarıyla güvenli iletişim.
* **5G Ağ Optimizasyonu:** Yeni nesil 5G ağ altyapısına özel optimizasyonlar.
* **Edge Computing Entegrasyonu:** Dağıtık işleme mimarileriyle uyumluluk.

## 🎓 Öğrenme Çıktıları ve Kazanımlar

Bu proje sürecinde elde edilen temel öğrenme çıktıları ve kazanımlar:

* [cite_start]**Teknik Kazanımlar:** Düşük seviyeli ağ programlama (raw socket, IP protokol manipülasyonu), kriptografik sistem tasarımı (hibrit şifreleme, anahtar yönetimi), performans optimizasyonu (ağ ayarlama, kaynak yönetimi) ve güvenlik testi (sızma testleri, güvenlik açığı değerlendirmesi)[cite: 45].
* [cite_start]**Araştırma ve Geliştirme Becerileri:** Sistematik problem çözme (modüler yaklaşım), test güdümlü geliştirme (kapsamlı test ve doğrulama metodolojileri) ve dokümantasyon (teknik raporlama standartları)[cite: 46].

## 🚀 Endüstriyel Uygulama Potansiyeli

[cite_start]Geliştirilen sistem, aşağıdaki sektörlerde pratik uygulanabilirlik potansiyeline sahiptir[cite: 47]:

* **Finansal Hizmetler:** Güvenli müşteri veri transferi.
* **Sağlık Sektörü:** HIPAA uyumlu hasta verisi iletimi.
* **Savunma Sanayii:** Gizli bilgilerin güvenli iletimi.
* **Eğitim Teknolojileri:** Öğrenci verilerinin korunması ve gizliliği.

## 🎥 Video Demonstrasyonu

Projenin çalışma prensiplerini ve özelliklerini daha iyi anlamak için hazırlanan 10 dakikalık demonstrasyon videosunu aşağıdan izleyebilirsiniz:

[Proje Demonstration Video - YouTube Linki]
[cite_start]*(Video yüklendikten sonra bu linki güncellemeyi unutmayın!)* [cite: 55]

## 🤝 Katkıda Bulunma

Projenin geliştirilmesine katkıda bulunmak isterseniz, lütfen bir `pull request` açmaktan veya bir `issue` oluşturmaktan çekinmeyin. Her türlü katkı takdirle karşılanır!

## 📜 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakınız.

## 📧 İletişim

* **Proje Sahibi:** Siraç Gezgin
* **E-posta:** (siracgezgin@gmail.com)
* **LinkedIn:** (linkedin.com/in/siracgezgin)

---
[cite_start]*Bursa Teknik Üniversitesi Bilgisayar Ağları Dersi Dönem Projesi* [cite: 1]
```
