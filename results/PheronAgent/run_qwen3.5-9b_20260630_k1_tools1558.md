# Pheron Agent Kapsamlı Araç (Capabilities) Test Koşumu
Tarih:              2026-06-30 15:58
Model:              Qwen3.5 9B (Local)

## Özet
Toplam senaryo:     18
Toplam PASS:         1
Toplam FAIL:         17
Başarı Oranı:        5.6%

## Detaylı Sonuçlar
| ID | Prompt | Beklenen Araç | Kullanılan Araçlar | Durum | Süre (s) |
|---|---|---|---|---|---|
| L3-TOOL-01 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)/Aura di Luce (Aura of Light - Işık Hale) (1).mp3' dosyasındaki müziğin DNA analizini yap ve bana müzik türünü söyle | music_dna | music_dna, Analyzing audio & music structures... | 🟢 PASS | 149.83 |
| L3-TOOL-02 | çalan şarkıyı durdur ve bir sonraki şarkıya geç | media_control |  | 🔴 FAIL (HTTP request failed: timed out) | 180.01 |
| L3-TOOL-03 | bilgisayarın sesini %50 yap | system_volume | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'system_volume' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 4.51 |
| L3-TOOL-04 | ekran parlaklığını maksimuma getir | system_brightness |  | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| L3-TOOL-05 | bilgisayarı uyku moduna al | system_sleep | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'system_sleep' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 0.07 |
| L3-TOOL-06 | Safari'de yeni bir sekme aç ve google.com adresine git | safari_automation |  | 🔴 FAIL (HTTP request failed: timed out) | 180.05 |
| L3-TOOL-07 | Swift 6 dökümantasyon sayfasını tarayıcıda doğrudan aç | native_browser | app_launcher, Launching application... | 🔴 FAIL (Expected tool 'native_browser' not in called list: ['app_launcher', 'Launching application...']) | 117.37 |
| L3-TOOL-08 | proje performans analizini içeren bir markdown raporu tasarla | markdown_report | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'markdown_report' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 0.03 |
| L3-TOOL-09 | WhatsApp üzerinden Ahmet'e 'Toplantı saati 14:00 olarak güncellendi' yaz | whatsapp_message |  | 🔴 FAIL (Expected tool 'whatsapp_message' not in called list: []) | 73.91 |
| L3-TOOL-10 | Takvime yarın saat 10:00'da 'Haftalık Değerlendirme' adında bir etkinlik ekle | apple_calendar |  | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| L3-TOOL-11 | Ahmet'e 'Proje Son Durumu' konulu bir e-posta gönder | apple_mail |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-12 | Blender ile arka planda 3D küp modeli render et | blender_3d |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-13 | mevcut Swift projesini Xcode derleyicisi ile build et | xcode_builder |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-14 | sistemdeki mevcut kestirmeleri listele | shortcut_list |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-15 | Stripe üzerindeki son ödemeleri listele | stripe_tool |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-16 | GitHub reposundaki son açık pull request'leri listele | github_tool |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-17 | Notion'da yeni bir toplantı notu sayfası oluştur | notion_tool |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
| L3-TOOL-18 | Higgsfield kullanarak 'dalgalı denizde giden gemi' videosu üret | higgsfield_generate |  | 🔴 FAIL (HTTP request failed: <urlopen error [Errno 61] Connection refused>) | 0.00 |
