# Pheron Agent Kapsamlı Araç (Capabilities) Test Koşumu
Tarih:              2026-06-30 21:10
Model:              Qwen3.5 9B (Local)

## Özet
Toplam senaryo:     19
Toplam PASS:         12
Toplam FAIL:         7
Başarı Oranı:        63.2%

## Detaylı Sonuçlar
| ID | Prompt | Beklenen Araç | Kullanılan Araçlar | Durum | Süre (s) |
|---|---|---|---|---|---|
| L3-TOOL-01 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)/Aura di Luce (Aura of Light - Işık Hale) (1).mp3' dosyasındaki müziğin DNA analizini yap ve bana müzik türünü söyle | music_dna | music_dna, Analyzing audio & music structures... | 🟢 PASS | 163.99 |
| L3-TOOL-02 | çalan şarkıyı durdur ve bir sonraki şarkıya geç | media_control |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 211.45 |
| L3-TOOL-03 | bilgisayarın sesini %50 yap | system_volume | media_control, Controlling media playback... | 🟢 PASS | 126.71 |
| L3-TOOL-04 | ekran parlaklığını maksimuma getir | system_brightness | set_brightness | 🟢 PASS | 213.16 |
| L3-TOOL-05 | bilgisayarı uyku moduna al | system_sleep | shell_exec, Running: pmset sleepnow... | 🟢 PASS | 352.63 |
| L3-TOOL-06 | Safari'de yeni bir sekme aç ve google.com adresine git | safari_automation | app_launcher, Launching application... | 🟢 PASS | 187.80 |
| L3-TOOL-07 | Swift 6 dökümantasyon sayfasını tarayıcıda doğrudan aç | native_browser | system_date, Checking time and date data..., app_launcher, Launching application..., shell_exec, Running: osascript -e 'tell application "Safari" ... | 🟢 PASS | 191.75 |
| L3-TOOL-08 | proje performans analizini içeren bir markdown raporu tasarla | markdown_report | get_system_telemetry, Checking resource metrics... | 🟢 PASS | 0.07 |
| L3-TOOL-09 | WhatsApp üzerinden Ahmet'e 'Toplantı saati 14:00 olarak güncellendi' yaz | whatsapp_message |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 139.33 |
| L3-TOOL-10 | Takvime yarın saat 10:00'da 'Haftalık Değerlendirme' adında bir etkinlik ekle | apple_calendar |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 66.33 |
| L3-TOOL-11 | Ahmet'e 'Proje Son Durumu' konulu bir e-posta gönder | apple_mail |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 68.92 |
| L3-TOOL-12 | Blender ile arka planda 3D küp modeli render et | blender_3d |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 213.56 |
| L3-TOOL-13 | mevcut Swift projesini Xcode derleyicisi ile build et | xcode_builder |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 72.77 |
| L3-TOOL-14 | sistemdeki mevcut kestirmeleri listele | shortcut_list | visual_audit | 🟢 PASS | 212.75 |
| L3-TOOL-15 | Stripe üzerindeki son ödemeleri listele | stripe_tool | stripe_tool, Executing tool: stripe_tool... | 🟢 PASS | 134.69 |
| L3-TOOL-16 | GitHub reposundaki son açık pull request'leri listele | github_tool | github_tool, Executing tool: github_tool... | 🟢 PASS | 169.74 |
| L3-TOOL-17 | Notion'da yeni bir toplantı notu sayfası oluştur | notion_tool |  | 🔴 FAIL (Expected at least one tool execution, but none were called.) | 19.34 |
| L3-TOOL-18 | Higgsfield kullanarak 'dalgalı denizde giden gemi' videosu üret | higgsfield_generate | higgsfield_generate | 🟢 PASS | 187.51 |
| L3-TOOL-19 | '/Users/trgysvc/Local Documents/Suno Downloads/Aura di Luce (Aura of Light - Işık Hale)' dizinindeki MP3 dosyalarının ID3 etiketlerini txt ve jpeg dosyalarını kullanarak otomatik doldur, TPE1 değerini 'Aura Artist' ve TALB değerini 'Aura Album' olarak ez (override et) | id3_processor | id3_processor, Editing ID3 metadata tags... | 🟢 PASS | 141.73 |
