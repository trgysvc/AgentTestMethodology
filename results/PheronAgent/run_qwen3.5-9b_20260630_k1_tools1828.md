# Pheron Agent Kapsamlı Araç (Capabilities) Test Koşumu
Tarih:              2026-06-30 18:28
Model:              Qwen3.5 9B (Local)

## Özet
Toplam senaryo:     19
Toplam PASS:         2
Toplam FAIL:         17
Başarı Oranı:        10.5%

## Detaylı Sonuçlar
| ID | Prompt | Beklenen Araç | Kullanılan Araçlar | Durum | Süre (s) |
|---|---|---|---|---|---|
| L3-TOOL-01 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)/Aura di Luce (Aura of Light - Işık Hale) (1).mp3' dosyasındaki müziğin DNA analizini yap ve bana müzik türünü söyle | music_dna | music_dna, Analyzing audio & music structures... | 🟢 PASS | 145.77 |
| L3-TOOL-02 | çalan şarkıyı durdur ve bir sonraki şarkıya geç | media_control |  | 🔴 FAIL (HTTP request failed: timed out) | 180.01 |
| L3-TOOL-03 | bilgisayarın sesini %50 yap | system_volume | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'system_volume' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 9.65 |
| L3-TOOL-04 | ekran parlaklığını maksimuma getir | system_brightness |  | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| L3-TOOL-05 | bilgisayarı uyku moduna al | system_sleep | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'system_sleep' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 0.06 |
| L3-TOOL-06 | Safari'de yeni bir sekme aç ve google.com adresine git | safari_automation |  | 🔴 FAIL (HTTP request failed: timed out) | 180.01 |
| L3-TOOL-07 | Swift 6 dökümantasyon sayfasını tarayıcıda doğrudan aç | native_browser |  | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| L3-TOOL-08 | proje performans analizini içeren bir markdown raporu tasarla | markdown_report | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'markdown_report' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 5.55 |
| L3-TOOL-09 | WhatsApp üzerinden Ahmet'e 'Toplantı saati 14:00 olarak güncellendi' yaz | whatsapp_message |  | 🔴 FAIL (Expected tool 'whatsapp_message' not in called list: []) | 174.33 |
| L3-TOOL-10 | Takvime yarın saat 10:00'da 'Haftalık Değerlendirme' adında bir etkinlik ekle | apple_calendar |  | 🔴 FAIL (Expected tool 'apple_calendar' not in called list: []) | 73.61 |
| L3-TOOL-11 | Ahmet'e 'Proje Son Durumu' konulu bir e-posta gönder | apple_mail |  | 🔴 FAIL (Expected tool 'apple_mail' not in called list: []) | 71.68 |
| L3-TOOL-12 | Blender ile arka planda 3D küp modeli render et | blender_3d |  | 🔴 FAIL (Expected tool 'blender_3d' not in called list: []) | 124.82 |
| L3-TOOL-13 | mevcut Swift projesini Xcode derleyicisi ile build et | xcode_builder |  | 🔴 FAIL (Expected tool 'xcode_builder' not in called list: []) | 93.46 |
| L3-TOOL-14 | sistemdeki mevcut kestirmeleri listele | shortcut_list |  | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| L3-TOOL-15 | Stripe üzerindeki son ödemeleri listele | stripe_tool |  | 🔴 FAIL (HTTP request failed: timed out) | 180.02 |
| L3-TOOL-16 | GitHub reposundaki son açık pull request'leri listele | github_tool | github_tool, Executing tool: github_tool... | 🟢 PASS | 173.93 |
| L3-TOOL-17 | Notion'da yeni bir toplantı notu sayfası oluştur | notion_tool |  | 🔴 FAIL (Expected tool 'notion_tool' not in called list: []) | 29.05 |
| L3-TOOL-18 | Higgsfield kullanarak 'dalgalı denizde giden gemi' videosu üret | higgsfield_generate |  | 🔴 FAIL (HTTP request failed: timed out) | 180.01 |
| L3-TOOL-19 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)' dizinindeki MP3 dosyalarının ID3 etiketlerini txt ve jpeg dosyalarını kullanarak otomatik doldur, TPE1 değerini 'Aura Artist' ve TALB değerini 'Aura Album' olarak ez (override et) | id3_processor |  | 🔴 FAIL (HTTP request failed: timed out) | 180.04 |
