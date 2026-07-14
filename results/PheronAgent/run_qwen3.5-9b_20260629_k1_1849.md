# Pheron Agent Test Koşumu
Tarih:              2026-06-29 18:49
Tester:             Antigravity AI
Uygulama sürümü:    Debug Build (2026-06-29)
Model:              Qwen3.5 9B
Git commit:         Local Working Directory

## Özet
Toplam senaryo:     31
Toplam PASS:         9
Toplam FAIL:         22
Başarı Oranı:        29.0%

## Detaylı Sonuçlar
| ID | Prompt | Beklenen Araç | Kullanılan Araçlar | Durum | Süre (s) |
|---|---|---|---|---|---|
| SOHBET-01 | merhaba, nasılsın? | None | None | 🟢 PASS | 6.41 |
| SOHBET-02 | yapay zeka nedir, 2-3 cümleyle anlat | None | None | 🟢 PASS | 14.27 |
| SOHBET-03 | sen kim olduğunu ve ne yapabileceğini anlat | None | None | 🟢 PASS | 14.37 |
| HESAP-01 | 1850 çarpı 0.18 nedir? | calculator_op | calculator_op, Performing mathematical calculations... | 🟢 PASS | 104.80 |
| HESAP-02 | 1847 çarpı 293 nedir? | calculator_op | calculator_op, Performing mathematical calculations... | 🟢 PASS | 147.96 |
| HESAP-03 | sqrt(144) + 3^4 hesapla | None | None | 🟢 PASS | 0.04 |
| SISTEM-01 | bilgisayarımın RAM ve CPU kullanımı nedir? | get_system_telemetry | None | 🔴 FAIL (Expected tool 'get_system_telemetry' not in called list: []) | 0.03 |
| SISTEM-02 | macOS versiyonum nedir? | get_system_info | None | 🔴 FAIL (HTTP request failed: timed out) | 0.00 |
| SISTEM-03 | diskte ne kadar boş alan var? | get_system_telemetry | None | 🔴 FAIL () | 0.00 |
| TARIH-01 | bugün günlerden ne? | None | None | 🔴 FAIL () | 0.00 |
| TARIH-02 | şu an saat kaç? | system_date | None | 🔴 FAIL (HTTP request failed: timed out) | 0.00 |
| DOSYA-01 | masaüstüne pheron_test.txt dosyası oluştur ve içine 'Pheron Agent çalışıyor - test başarılı' yaz | write_file | None | 🔴 FAIL () | 0.00 |
| DOSYA-02 | ~/Desktop/pheron_test.txt dosyasını oku | read_file | None | 🔴 FAIL (HTTP request failed: timed out) | 0.00 |
| DOSYA-03 | masaüstündeki dosyaları listele | file_manager_action | None | 🔴 FAIL () | 0.00 |
| DOSYA-04 | ~/Desktop/pheron_test.txt dosyasını sil | file_manager_action | None | 🔴 FAIL () | 0.00 |
| GIT-01 | bu projedeki son 5 commit'i göster | git_action | None | 🔴 FAIL (HTTP request failed: timed out) | 0.00 |
| GIT-02 | git durumunu kontrol et, hangi dosyalar değiştirilmiş? | git_action | None | 🔴 FAIL () | 0.00 |
| WEB-01 | Swift 6 concurrency ile ilgili en önemli değişiklikler neler? | web_search | None | 🔴 FAIL () | 0.00 |
| WEB-02 | Apple M4 chip özellikleri neler, kısaca araştır | web_search | web_search, Searching: Apple M4 chip özellikleri 2026... | 🟢 PASS | 170.52 |
| HAVA-01 | İstanbul'da bugün hava nasıl? | get_weather | None | 🔴 FAIL (Expected tool 'get_weather' not in called list: []) | 1.30 |
| HAVA-02 | Ankara'nın hava durumu ne? | get_weather | get_weather, Fetching meteorological data... | 🟢 PASS | 63.01 |
| UYGULAMA-01 | şu an hangi uygulamalar açık? | learn_application_ui | None | 🔴 FAIL (HTTP request failed: timed out) | 0.00 |
| UYGULAMA-02 | TextEdit uygulamasını aç | app_launcher | None | 🔴 FAIL () | 0.00 |
| CLARIFY-03 | dosyayı sil | None | None | 🟢 PASS | 82.18 |
| CLARIFY-04 | mesaj gönder | None | None | 🔴 FAIL (HTTP request failed: timed out) | 0.00 |
| ZINCIR-01 | masaüstüne rapor.md dosyası oluştur: bugünün tarihi ve RAM kullanımını içersin | write_file | None | 🔴 FAIL () | 0.00 |
| ZINCIR-02 | bu projedeki .swift dosya sayısını say ve sonucu bana söyle | shell_exec | None | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| ZINCIR-03 | masaüstünde swift_demo.swift dosyası oluştur: içine print('Merhaba Pheron Agent') yazan minimal bir Swift programı yaz | write_file | None | 🔴 FAIL () | 0.00 |
| ZINCIR-04 | sistem durumunu kontrol et: CPU, RAM, disk alanı ve macOS sürümünü tek seferde rapor et | get_system_telemetry | None | 🔴 FAIL () | 0.00 |
| SAF-01 | https://www.swift.org/documentation/ adresindeki içeriği oku ve 3 maddeyle özetle | None | None | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| EDGE-01 | bu konuşmada daha önce ne yaptık? | None | None | 🔴 FAIL () | 0.00 |
