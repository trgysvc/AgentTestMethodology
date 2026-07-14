# Pheron Agent Test Koşumu
Tarih:              2026-06-29 22:21
Tester:             Antigravity AI
Uygulama sürümü:    Debug Build (2026-06-29)
Model:              Qwen3.5 9B
Git commit:         Local Working Directory

## Özet
Toplam senaryo:     31
Toplam PASS:         25
Toplam FAIL:         6
Başarı Oranı:        80.6%

## Detaylı Sonuçlar
| ID | Prompt | Beklenen Araç | Kullanılan Araçlar | Durum | Süre (s) |
|---|---|---|---|---|---|
| SOHBET-01 | merhaba, nasılsın? | None | None | 🟢 PASS | 7.45 |
| SOHBET-02 | yapay zeka nedir, 2-3 cümleyle anlat | None | None | 🟢 PASS | 17.63 |
| SOHBET-03 | sen kim olduğunu ve ne yapabileceğini anlat | None | None | 🟢 PASS | 15.49 |
| HESAP-01 | 1850 çarpı 0.18 nedir? | calculator_op | calculator_op, Performing mathematical calculations... | 🟢 PASS | 115.53 |
| HESAP-02 | 1847 çarpı 293 nedir? | calculator_op | calculator_op, Performing mathematical calculations... | 🟢 PASS | 115.46 |
| HESAP-03 | sqrt(144) + 3^4 hesapla | None | None | 🟢 PASS | 0.03 |
| SISTEM-01 | bilgisayarımın RAM ve CPU kullanımı nedir? | get_system_telemetry | get_system_telemetry, Checking resource metrics... | 🟢 PASS | 0.03 |
| SISTEM-02 | macOS versiyonum nedir? | get_system_info | get_system_telemetry, Checking resource metrics... | 🔴 FAIL (Expected tool 'get_system_info' not in called list: ['get_system_telemetry', 'Checking resource metrics...']) | 0.03 |
| SISTEM-03 | diskte ne kadar boş alan var? | get_system_telemetry | get_system_telemetry, Checking resource metrics... | 🟢 PASS | 0.03 |
| TARIH-01 | bugün günlerden ne? | None | None | 🟢 PASS | 0.03 |
| TARIH-02 | şu an saat kaç? | system_date | system_date, Checking time and date data... | 🟢 PASS | 109.57 |
| DOSYA-01 | masaüstüne pheron_test.txt dosyası oluştur ve içine 'Pheron Agent çalışıyor - test başarılı' yaz | write_file | write_file, Writing pheron_test.txt... | 🟢 PASS | 68.53 |
| DOSYA-02 | ~/Desktop/pheron_test.txt dosyasını oku | read_file | read_file, Reading pheron_test.txt... | 🟢 PASS | 69.07 |
| DOSYA-03 | masaüstündeki dosyaları listele | file_manager_action | file_manager_action, Listing Desktop/... | 🟢 PASS | 142.56 |
| DOSYA-04 | ~/Desktop/pheron_test.txt dosyasını sil | file_manager_action | file_manager_action, Deleting pheron_test.txt... | 🟢 PASS | 138.67 |
| GIT-01 | bu projedeki son 5 commit'i göster | git_action | None | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| GIT-02 | git durumunu kontrol et, hangi dosyalar değiştirilmiş? | git_action | git_action, Executing Git version control operations... | 🟢 PASS | 126.87 |
| WEB-01 | Swift 6 concurrency ile ilgili en önemli değişiklikler neler? | web_search | web_search, Searching: Swift 6 concurrency en önemli değişiklikler... | 🟢 PASS | 162.19 |
| WEB-02 | Apple M4 chip özellikleri neler, kısaca araştır | web_search | web_search, Searching: Apple M4 chip özellikleri... | 🟢 PASS | 170.36 |
| HAVA-01 | İstanbul'da bugün hava nasıl? | get_weather | get_weather, Fetching meteorological data... | 🟢 PASS | 1.07 |
| HAVA-02 | Ankara'nın hava durumu ne? | get_weather | get_weather, Fetching meteorological data... | 🟢 PASS | 82.75 |
| UYGULAMA-01 | şu an hangi uygulamalar açık? | learn_application_ui | None | 🔴 FAIL (HTTP request failed: timed out) | 180.03 |
| UYGULAMA-02 | TextEdit uygulamasını aç | app_launcher | None | 🔴 FAIL (HTTP request failed: timed out) | 180.02 |
| CLARIFY-03 | dosyayı sil | None | None | 🟢 PASS | 162.96 |
| CLARIFY-04 | mesaj gönder | None | None | 🟢 PASS | 71.09 |
| ZINCIR-01 | masaüstüne rapor.md dosyası oluştur: bugünün tarihi ve RAM kullanımını içersin | write_file | system_date, Checking time and date data..., write_file, Writing RAPOR.md... | 🟢 PASS | 90.15 |
| ZINCIR-02 | bu projedeki .swift dosya sayısını say ve sonucu bana söyle | shell_exec | None | 🔴 FAIL (Expected tool 'shell_exec' not in called list: []) | 133.41 |
| ZINCIR-03 | masaüstünde swift_demo.swift dosyası oluştur: içine print('Merhaba Pheron Agent') yazan minimal bir Swift programı yaz | write_file | write_file, Writing swift_demo.swift... | 🟢 PASS | 115.20 |
| ZINCIR-04 | sistem durumunu kontrol et: CPU, RAM, disk alanı ve macOS sürümünü tek seferde rapor et | get_system_telemetry | get_system_telemetry, Checking resource metrics... | 🟢 PASS | 0.07 |
| SAF-01 | https://www.swift.org/documentation/ adresindeki içeriği oku ve 3 maddeyle özetle | None | None | 🔴 FAIL (HTTP request failed: timed out) | 180.00 |
| EDGE-01 | bu konuşmada daha önce ne yaptık? | None | None | 🟢 PASS | 26.07 |
