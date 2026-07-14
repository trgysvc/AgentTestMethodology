# Pheron Agent Kapsamlı Araç (Capabilities) Test Koşumu
Tarih:              2026-06-30 19:48
Model:              Qwen3.5 9B (Local)

## Özet
Toplam senaryo:     19
Toplam PASS:         4
Toplam FAIL:         15
Başarı Oranı:        21.1%

## Detaylı Sonuçlar
| ID | Prompt | Beklenen Araç | Kullanılan Araçlar | Durum | Süre (s) |
|---|---|---|---|---|---|
| L3-TOOL-01 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)/Aura di Luce (Aura of Light - Işık Hale) (1).mp3' dosyasındaki müziğin DNA analizini yap ve bana müzik türünü söyle | music_dna |  | 🔴 FAIL (HTTP request failed: timed out) | 240.02 |
| L3-TOOL-02 | çalan şarkıyı durdur ve bir sonraki şarkıya geç | media_control | media_control | 🟢 PASS | 212.68 |
| L3-TOOL-03 | bilgisayarın sesini %50 yap | system_volume | media_control, Controlling media playback... | 🔴 FAIL (Expected tool 'system_volume' not in called list: ['media_control', 'Controlling media playback...']) | 193.30 |
| L3-TOOL-04 | ekran parlaklığını maksimuma getir | system_brightness | set_brightness, shell_exec, Running: defaults write NSGlobalDomain AppleDispl... | 🔴 FAIL (Expected tool 'system_brightness' not in called list: ['set_brightness', 'shell_exec', 'Running: defaults write NSGlobalDomain AppleDispl...']) | 217.19 |
| L3-TOOL-05 | bilgisayarı uyku moduna al | system_sleep | shell_exec | 🔴 FAIL (Expected tool 'system_sleep' not in called list: ['shell_exec']) | 211.62 |
| L3-TOOL-06 | Safari'de yeni bir sekme aç ve google.com adresine git | safari_automation | app_launcher, Launching application... | 🔴 FAIL (Expected tool 'safari_automation' not in called list: ['app_launcher', 'Launching application...']) | 210.66 |
| L3-TOOL-07 | Swift 6 dökümantasyon sayfasını tarayıcıda doğrudan aç | native_browser | system_date, Checking time and date data... | 🔴 FAIL (Expected tool 'native_browser' not in called list: ['system_date', 'Checking time and date data...']) | 211.91 |
| L3-TOOL-08 | proje performans analizini içeren bir markdown raporu tasarla | markdown_report | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'markdown_report' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 5.18 |
| L3-TOOL-09 | WhatsApp üzerinden Ahmet'e 'Toplantı saati 14:00 olarak güncellendi' yaz | whatsapp_message |  | 🔴 FAIL (Expected tool 'whatsapp_message' not in called list: []) | 209.48 |
| L3-TOOL-10 | Takvime yarın saat 10:00'da 'Haftalık Değerlendirme' adında bir etkinlik ekle | apple_calendar |  | 🔴 FAIL (Expected tool 'apple_calendar' not in called list: []) | 81.11 |
| L3-TOOL-11 | Ahmet'e 'Proje Son Durumu' konulu bir e-posta gönder | apple_mail |  | 🔴 FAIL (Expected tool 'apple_mail' not in called list: []) | 77.37 |
| L3-TOOL-12 | Blender ile arka planda 3D küp modeli render et | blender_3d |  | 🔴 FAIL (Expected tool 'blender_3d' not in called list: []) | 210.87 |
| L3-TOOL-13 | mevcut Swift projesini Xcode derleyicisi ile build et | xcode_builder |  | 🔴 FAIL (Expected tool 'xcode_builder' not in called list: []) | 84.42 |
| L3-TOOL-14 | sistemdeki mevcut kestirmeleri listele | shortcut_list |  | 🔴 FAIL (Expected tool 'shortcut_list' not in called list: []) | 215.59 |
| L3-TOOL-15 | Stripe üzerindeki son ödemeleri listele | stripe_tool | stripe_tool, Executing tool: stripe_tool... | 🟢 PASS | 165.18 |
| L3-TOOL-16 | GitHub reposundaki son açık pull request'leri listele | github_tool | github_tool, Executing tool: github_tool... | 🟢 PASS | 127.53 |
| L3-TOOL-17 | Notion'da yeni bir toplantı notu sayfası oluştur | notion_tool |  | 🔴 FAIL (Expected tool 'notion_tool' not in called list: []) | 19.43 |
| L3-TOOL-18 | Higgsfield kullanarak 'dalgalı denizde giden gemi' videosu üret | higgsfield_generate | higgsfield_generate | 🟢 PASS | 214.41 |
| L3-TOOL-19 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)' dizinindeki MP3 dosyalarının ID3 etiketlerini txt ve jpeg dosyalarını kullanarak otomatik doldur, TPE1 değerini 'Aura Artist' ve TALB değerini 'Aura Album' olarak ez (override et) | id3_processor |  | 🔴 FAIL (Expected tool 'id3_processor' not in called list: []) | 214.22 |
